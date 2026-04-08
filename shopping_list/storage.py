import json  # JSON modulis ļauj nolasīt un saglabāt datus failos.
import os  # OS modulis ļauj strādāt ar failu ceļiem un eksistences pārbaudi.


SHOPPING_FILE = os.path.join(os.path.dirname(__file__), "shopping.json")  # Ceļš uz iepirkumu saraksta failu.
PRICES_FILE = os.path.join(os.path.dirname(__file__), "prices.json")  # Ceļš uz cenu datubāzes failu.


def _normalize_item(item):
    """Pielāgo vecā un jaunā formāta ierakstus vienotai struktūrai."""
    return {  # Atgriež vienotu vārdnīcas formātu visiem ierakstiem.
        "name": item["name"],  # Produkta nosaukums.
        "qty": int(item.get("qty", 1)),  # Daudzums; vecajiem ierakstiem pēc noklusējuma 1.
        "price": float(item["price"]),  # Cena par vienību kā skaitlis.
    }


def load_list():
    """Nolasa iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(SHOPPING_FILE):  # Ja saraksta faila nav, atgriež tukšu sarakstu.
        return []

    with open(SHOPPING_FILE, "r", encoding="utf-8") as file:  # Atver iepirkumu failu lasīšanai.
        items = json.load(file)  # Nolasa JSON datus Python sarakstā.

    return [_normalize_item(item) for item in items]  # Pielāgo katru ierakstu vienotam formātam.


def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:  # Atver failu rakstīšanai.
        json.dump(items, file, indent=2, ensure_ascii=False)  # Saglabā sarakstu lasāmā JSON formā.


def load_prices():
    """Nolasa cenu datubāzi no JSON faila."""
    if not os.path.exists(PRICES_FILE):  # Ja cenu faila nav, atgriež tukšu vārdnīcu.
        return {}

    with open(PRICES_FILE, "r", encoding="utf-8") as file:  # Atver cenu datubāzes failu lasīšanai.
        prices = json.load(file)  # Nolasa cenu datus kā Python vārdnīcu.

    return {name: float(price) for name, price in prices.items()}  # Pārvērš visas cenas par float tipa vērtībām.


def save_prices(prices):
    """Saglabā cenu datubāzi JSON failā."""
    with open(PRICES_FILE, "w", encoding="utf-8") as file:  # Atver cenu datubāzi rakstīšanai.
        json.dump(prices, file, indent=2, ensure_ascii=False)  # Saglabā cenas JSON formātā.


def get_price(name):
    """Atgriež saglabāto cenu vai None."""
    prices = load_prices()  # Nolasa visas zināmās cenas.
    return prices.get(name)  # Atgriež cenu konkrētajam produktam vai None.


def set_price(name, price):
    """Saglabā vai atjaunina produkta cenu datubāzē."""
    prices = load_prices()  # Nolasa esošo cenu vārdnīcu.
    prices[name] = float(price)  # Iestata jauno vai atjaunināto cenu produktam.
    save_prices(prices)  # Saglabā atjaunināto cenu datubāzi failā.