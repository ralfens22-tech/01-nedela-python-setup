import json
import os


SHOPPING_FILE = os.path.join(os.path.dirname(__file__), "shopping.json")


def _normalize_item(item):
    """Pielāgo vecā un jaunā formāta ierakstus vienotai struktūrai."""
    return {
        "name": item["name"],
        "qty": int(item.get("qty", 1)),
        "price": float(item["price"]),
    }


def load_list():
    """Nolasa iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(SHOPPING_FILE):
        return []

    with open(SHOPPING_FILE, "r", encoding="utf-8") as file:
        items = json.load(file)

    return [_normalize_item(item) for item in items]


def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)