import sys  # Sys modulis ļauj nolasīt komandrindas argumentus.

from storage import get_price, load_list, save_list, set_price  # Importē datu glabāšanas funkcijas.
from utils import calc_grand_total, calc_line_total, count_units  # Importē aprēķinu palīgfunkcijas.


def add_item(name, qty, price):
    """Pievieno produktu iepirkumu sarakstam."""
    items = load_list()  # Nolasa pašreizējo iepirkumu sarakstu.
    item = {"name": name, "qty": qty, "price": price}  # Izveido jaunu produkta ierakstu.
    items.append(item)  # Pievieno produktu sarakstam.
    save_list(items)  # Saglabā atjaunoto sarakstu failā.
    print(f"Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {calc_line_total(item):.2f} EUR")  # Parāda pievienošanas rezultātu.


def prompt_for_price(prompt_text):
    """Nolasa derīgu pozitīvu cenu no lietotāja ievades."""
    while True:  # Atkārto jautājumu, līdz lietotājs ievada derīgu cenu.
        raw_value = input(prompt_text).strip()  # Nolasa ievadi un noņem liekās atstarpes.

        try:  # Mēģina pārveidot ievadi uz skaitli.
            price = float(raw_value)
        except ValueError:  # Ja pārveidošana neizdodas, ievade nav derīga cena.
            print("Kļūda: cenai jābūt pozitīvam skaitlim.")
            continue

        if price <= 0:  # Pārbauda, vai cena ir lielāka par nulli.
            print("Kļūda: cenai jābūt pozitīvam skaitlim.")
            continue

        return price  # Atgriež pārbaudītu un derīgu cenu.


def resolve_price(name):
    """Nosaka produkta cenu no datubāzes vai interaktīvas ievades."""
    known_price = get_price(name)  # Mēģina atrast produkta cenu datubāzē.

    if known_price is None:  # Ja cena datubāzē vēl nav saglabāta.
        print("Cena nav zināma.")
        price = prompt_for_price("Ievadi cenu: ")  # Palūdz lietotājam ievadīt cenu.
        set_price(name, price)  # Saglabā jauno cenu datubāzē.
        print(f"Cena saglabāta: {name} ({price:.2f} EUR)")  # Informē, ka cena ir saglabāta.
        return price

    print(f"Atrasta cena: {known_price:.2f} EUR/gab.")  # Parāda jau zināmo cenu.

    while True:  # Atkārto izvēli, līdz lietotājs ievada A vai M.
        choice = input("[A]kceptēt / [M]ainīt? ").strip().lower()  # Nolasa izvēli un padara to nereģistrjutīgu.

        if choice == "a":  # Ja lietotājs pieņem atrasto cenu.
            return known_price

        if choice == "m":  # Ja lietotājs vēlas mainīt cenu.
            new_price = prompt_for_price("Jaunā cena: ")  # Palūdz ievadīt jauno cenu.
            set_price(name, new_price)  # Saglabā jauno cenu datubāzē.
            print(f"Cena atjaunināta: {name} → {new_price:.2f} EUR")  # Informē par cenu atjaunināšanu.
            return new_price

        print("Kļūda: ievadi A vai M.")  # Paziņo par nederīgu izvēli.


def list_items():
    """Parāda visus produktus no saraksta."""
    items = load_list()  # Nolasa visus saglabātos produktus.
    if not items:  # Pārbauda, vai sarakstā vispār ir ieraksti.
        print("Iepirkumu saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")  # Izvada saraksta virsrakstu.
    for index, item in enumerate(items, start=1):  # Iet cauri visiem produktiem ar numerāciju.
        line_total = calc_line_total(item)  # Aprēķina konkrētās rindas summu.
        print(f"{index}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")  # Izvada vienu produkta rindu.


def calculate_total():
    """Aprēķina iepirkumu saraksta kopsummu."""
    items = load_list()  # Nolasa visus produktus no faila.
    total = calc_grand_total(items)  # Aprēķina visu produktu kopējo cenu.
    units = count_units(items)  # Saskaita kopējo vienību skaitu.
    print(f"Kopā: {total:.2f} EUR ({units} vienības, {len(items)} produkti)")  # Parāda kopsavilkumu.


def clear_list():
    """Notīra visus produktus no saraksta."""
    save_list([])  # Saglabā tukšu sarakstu, izdzēšot visus ierakstus.
    print("Iepirkumu saraksts notīrīts.")  # Informē lietotāju par notīrīšanu.


def print_usage():
    """Parāda pieejamās komandas."""
    print("Lietošana:")  # Izvada palīdzības virsrakstu.
    print("python shop.py add Maize 3")  # Piemērs produkta pievienošanai.
    print("python shop.py list")  # Piemērs saraksta apskatei.
    print("python shop.py total")  # Piemērs kopsummas aprēķinam.
    print("python shop.py clear")  # Piemērs saraksta notīrīšanai.


def main():
    """Apstrādā CLI komandas iepirkumu sarakstam."""
    if len(sys.argv) < 2:  # Ja lietotājs nav norādījis komandu.
        print_usage()  # Parāda palīdzības tekstu.
        return

    command = sys.argv[1].lower()  # Nolasa komandu un pārvērš to mazajos burtos.

    if command == "add":  # Apstrādā produkta pievienošanas komandu.
        if len(sys.argv) not in (4, 5):  # Pārbauda atļauto argumentu skaitu.
            print("Kļūda: komandai add vajag nosaukumu, daudzumu un izvēles cenu.")
            print_usage()
            return

        try:  # Mēģina daudzumu pārvērst par veselu skaitli.
            qty = int(sys.argv[3])
        except ValueError:  # Ja tas neizdodas, daudzums nav derīgs.
            print("Kļūda: daudzumam jābūt veselam skaitlim.")
            return

        if qty <= 0:  # Pārbauda, vai daudzums ir lielāks par nulli.
            print("Kļūda: daudzumam jābūt pozitīvam skaitlim.")
            return

        if len(sys.argv) == 5:  # Ja cena padota uzreiz komandā.
            try:  # Mēģina cenu pārvērst par skaitli.
                price = float(sys.argv[4])
            except ValueError:  # Ja cena nav korekts skaitlis.
                print("Kļūda: cenai jābūt pozitīvam skaitlim.")
                return

            if price <= 0:  # Pārbauda, vai cena ir pozitīva.
                print("Kļūda: cenai jābūt pozitīvam skaitlim.")
                return
            set_price(sys.argv[2], price)  # Saglabā arī cenu datubāzē nākamajām reizēm.
        else:
            price = resolve_price(sys.argv[2])  # Nosaka cenu interaktīvi vai no datubāzes.

        add_item(sys.argv[2], qty, price)  # Pievieno produktu iepirkumu sarakstam.
        return

    if command == "list":  # Apstrādā saraksta apskates komandu.
        list_items()  # Izvada visus produktus.
        return

    if command == "total":  # Apstrādā kopsummas komandu.
        calculate_total()  # Aprēķina un izvada kopsummu.
        return

    if command == "clear":  # Apstrādā saraksta notīrīšanas komandu.
        clear_list()  # Izdzēš visus produktus no saraksta.
        return

    print_usage()  # Ja komanda nav atbalstīta, parāda palīdzību.


if __name__ == "__main__":  # Šis nosacījums pārbauda, vai fails tiek palaists tieši.
    main()  # Palaiž galveno programmas loģiku.