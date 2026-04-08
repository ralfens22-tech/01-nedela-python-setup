import os  # Failu ceļu veidošanai.
import sys  # Lai pievienotu projekta mapes importam.

# Pievienojam projekta saknes un shopping_list mapes ceļus,
# lai varētu importēt contacts.py, storage.py un utils.py.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Projekta sakne.
sys.path.insert(0, BASE_DIR)  # Ļauj importēt contacts.py.
sys.path.insert(0, os.path.join(BASE_DIR, "shopping_list"))  # Ļauj importēt storage.py, utils.py.

from flask import Flask, jsonify, render_template, request  # Flask web ietvars.

from contacts import load_contacts, save_contacts  # Kontaktu datu funkcijas.
from storage import get_price, load_list, save_list, set_price  # Iepirkumu un cenu datu funkcijas.
from utils import calc_grand_total, calc_line_total, count_units  # Aprēķinu palīgfunkcijas.

app = Flask(__name__)  # Izveido Flask lietotni.


# ─── Galvenā lapa ────────────────────────────────────────────────

@app.route("/")
def index():
    """Atgriež galveno HTML lapu."""
    return render_template("index.html")  # Renderē templates/index.html.


# ─── Kontaktu API ────────────────────────────────────────────────

@app.route("/api/contacts", methods=["GET"])
def api_list_contacts():
    """Atgriež visus kontaktus JSON formātā."""
    return jsonify(load_contacts())  # Nolasa kontaktus no faila un atgriež.


@app.route("/api/contacts/add", methods=["POST"])
def api_add_contact():
    """Pievieno jaunu kontaktu."""
    data = request.get_json()  # Nolasa JSON datus no pieprasījuma.
    name = data.get("name", "").strip()  # Iegūst vārdu un noņem atstarpes.
    phone = data.get("phone", "").strip()  # Iegūst tālruni.

    if not name or not phone:  # Pārbauda, vai abi lauki aizpildīti.
        return jsonify({"error": "Vārds un tālrunis ir obligāti."}), 400

    contacts = load_contacts()  # Nolasa esošos kontaktus.
    contacts.append({"name": name, "phone": phone})  # Pievieno jauno kontaktu.
    save_contacts(contacts)  # Saglabā atjaunoto sarakstu.
    return jsonify({"message": f"Pievienots: {name} ({phone})"})  # Atgriež apstiprinājumu.


@app.route("/api/contacts/search", methods=["GET"])
def api_search_contacts():
    """Meklē kontaktus pēc vārda daļas."""
    query = request.args.get("q", "").strip().lower()  # Nolasa meklēšanas tekstu.

    if not query:  # Ja meklēšanas lauks tukšs.
        return jsonify({"error": "Meklēšanas teksts ir tukšs."}), 400

    contacts = load_contacts()  # Nolasa visus kontaktus.
    matches = [c for c in contacts if query in c["name"].lower()]  # Filtrē atbilstošos.
    return jsonify(matches)  # Atgriež atrasto sarakstu.


# ─── Iepirkumu saraksta API ───────────────────────────────────────

@app.route("/api/shopping", methods=["GET"])
def api_list_items():
    """Atgriež iepirkumu sarakstu ar rindu summām."""
    items = load_list()  # Nolasa iepirkumu sarakstu.
    result = []
    for item in items:
        result.append({
            "name": item["name"],
            "qty": item["qty"],
            "price": item["price"],
            "line_total": calc_line_total(item),  # Aprēķina rindas summu.
        })
    return jsonify(result)  # Atgriež paplašināto sarakstu.


@app.route("/api/shopping/add", methods=["POST"])
def api_add_item():
    """Pievieno produktu iepirkumu sarakstam."""
    data = request.get_json()  # Nolasa JSON datus.
    name = data.get("name", "").strip()  # Produkta nosaukums.

    if not name:  # Pārbauda, vai nosaukums nav tukšs.
        return jsonify({"error": "Produkta nosaukums ir obligāts."}), 400

    try:
        qty = int(data.get("qty", 0))  # Pārvērš daudzumu par veselu skaitli.
    except (ValueError, TypeError):
        return jsonify({"error": "Daudzumam jābūt veselam skaitlim."}), 400

    if qty <= 0:  # Daudzumam jābūt pozitīvam.
        return jsonify({"error": "Daudzumam jābūt pozitīvam skaitlim."}), 400

    price_raw = data.get("price")  # Iegūst cenu, ja lietotājs to norādīja.

    if price_raw is not None and price_raw != "" and price_raw != 0:
        try:
            price = float(price_raw)  # Pārvērš cenu par skaitli.
        except (ValueError, TypeError):
            return jsonify({"error": "Cenai jābūt pozitīvam skaitlim."}), 400

        if price <= 0:  # Cena nedrīkst būt nulle vai negatīva.
            return jsonify({"error": "Cenai jābūt pozitīvam skaitlim."}), 400

        set_price(name, price)  # Saglabā arī cenu datubāzē nākamajām reizēm.
    else:
        price = get_price(name)  # Meklē cenu datubāzē.

        if price is None:  # Ja cena nav zināma, piedāvā to ievadīt.
            return jsonify({
                "error": "Cena nav zināma. Ievadi cenu laukā.",
                "need_price": True,
            }), 400

    item = {"name": name, "qty": qty, "price": price}  # Izveido produkta ierakstu.
    items = load_list()  # Nolasa pašreizējo sarakstu.
    items.append(item)  # Pievieno jauno produktu.
    save_list(items)  # Saglabā atjaunoto sarakstu.

    return jsonify({
        "message": f"Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {calc_line_total(item):.2f} EUR",
        "known_price": get_price(name),  # Informē, vai cena ir saglabāta datubāzē.
    })


@app.route("/api/shopping/total", methods=["GET"])
def api_shopping_total():
    """Aprēķina iepirkumu kopsummu."""
    items = load_list()  # Nolasa visus produktus.
    return jsonify({
        "total": calc_grand_total(items),  # Kopsumma EUR.
        "units": count_units(items),  # Kopējais vienību skaits.
        "products": len(items),  # Produktu veidu skaits.
    })


@app.route("/api/shopping/clear", methods=["POST"])
def api_shopping_clear():
    """Notīra visu iepirkumu sarakstu."""
    save_list([])  # Saglabā tukšu sarakstu.
    return jsonify({"message": "Iepirkumu saraksts notīrīts."})


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Palaiž serveri uz localhost:5000.
