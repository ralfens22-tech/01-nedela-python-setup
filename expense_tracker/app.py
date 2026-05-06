"""
Galvenā programma — interaktīvā izvēlne un lietotāja vadības loģika.
"""

from datetime import date
from storage import load_expenses, save_expenses
from logic import sum_total


CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]


def is_valid_date(date_str):
    """Pārbauda, vai teksts ir derīgs datums YYYY-MM-DD formātā."""
    from datetime import datetime
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_amount(amount_str):
    """Pārbauda, vai teksts ir derīgs pozitīvs skaitlis."""
    try:
        amount = float(amount_str)
        return amount >= 0
    except ValueError:
        return False


def show_menu():
    """Parāda galveno izvēlni un atgriež lietotāja izvēli."""
    print("\n═════════════════════════════════")
    print("  Izdevumu izsekotājs")
    print("═════════════════════════════════")
    print("1) Pievienot izdevumu")
    print("2) Parādīt izdevumus")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ").strip()


def add_expense(expenses):
    """Pievieno jaunu izdevumu ar validāciju."""
    print("\n--- Pievienot izdevumu ---")
    
    # Datums
    while True:
        default_date = str(date.today())
        date_input = input(f"Datums (YYYY-MM-DD) [{default_date}]: ").strip()
        if not date_input:
            date_input = default_date
        
        if is_valid_date(date_input):
            break
        print("❌ Nepareizs datums! Izmanto formātu YYYY-MM-DD")
    
    # Kategorija
    print("\nKategorija:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}) {cat}")
    
    while True:
        cat_input = input("Izvēlies (1-7): ").strip()
        try:
            cat_idx = int(cat_input) - 1
            if 0 <= cat_idx < len(CATEGORIES):
                category = CATEGORIES[cat_idx]
                break
            else:
                print(f"❌ Lūdzu izvēlies numuru no 1 līdz {len(CATEGORIES)}")
        except ValueError:
            print("❌ Lūdzu ievadi numuru")
    
    # Summa
    while True:
        amount_input = input("Summa (EUR): ").strip()
        if is_valid_amount(amount_input):
            amount = float(amount_input)
            break
        print("❌ Lūdzu ievadi derīgu pozitīvu summu")
    
    # Apraksts
    description = input("Apraksts: ").strip()
    
    # Pievieno izdevumu
    expense = {
        "date": date_input,
        "amount": round(amount, 2),
        "category": category,
        "description": description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    
    print(f"\n✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")


def display_expenses(expenses):
    """Parāda visus izdevumus formatēti."""
    if not expenses:
        print("\n❌ Nav reģistrētu izdevumu")
        return
    
    print("\n" + "─" * 70)
    print(f"{'Datums':<12} {'Summa':>10} {'Kategorija':<18} {'Apraksts'}")
    print("─" * 70)
    
    for expense in expenses:
        date_str = expense["date"]
        amount_str = f"{expense['amount']:.2f} EUR"
        category = expense["category"]
        description = expense["description"][:20]  # Saīsina garu aprakstu
        
        print(f"{date_str:<12} {amount_str:>10} {category:<18} {description}")
    
    print("─" * 70)
    total = sum_total(expenses)
    print(f"  Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")
    print()


def main():
    """Galvenā programmas cilpa."""
    expenses = load_expenses()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_expense(expenses)
        
        elif choice == "2":
            display_expenses(expenses)
        
        elif choice == "7":
            print("\nUz redzēšanos!")
            break
        
        else:
            print("\n❌ Nepareiza izvēle. Lūdzu mēģini vēlreiz.")


if __name__ == "__main__":
    main()
