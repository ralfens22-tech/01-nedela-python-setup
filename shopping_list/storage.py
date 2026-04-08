import json
import os


SHOPPING_FILE = os.path.join(os.path.dirname(__file__), "shopping.json")


def load_list():
    """Nolasa iepirkumu sarakstu no JSON faila."""
    if not os.path.exists(SHOPPING_FILE):
        return []

    with open(SHOPPING_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_list(items):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(SHOPPING_FILE, "w", encoding="utf-8") as file:
        json.dump(items, file, indent=2, ensure_ascii=False)