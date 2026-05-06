"""
Datu glabāšanas modulis — darbs ar expenses.json failu.
"""

import json
import os
from pathlib import Path


EXPENSES_FILE = "expenses.json"


def load_expenses():
    """
    Nolasa izdevumus no expenses.json faila.
    
    Atgriež:
        list: Izdevumu masīvs (katrs ir dict ar datums, summa, kategorija, apraksts)
        Ja fails neeksistē, atgriež tukšu masīvu []
    """
    if os.path.exists(EXPENSES_FILE):
        try:
            with open(EXPENSES_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Kļūda nolasot failu: {e}")
            return []
    return []


def save_expenses(expenses):
    """
    Saglabā izdevumus expenses.json failā.
    
    Parametri:
        expenses (list): Izdevumu masīvs
    """
    try:
        with open(EXPENSES_FILE, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Kļūda saglabājot failu: {e}")
