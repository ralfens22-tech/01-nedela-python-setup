"""
Galvenā programma — interaktīvā izvēlne un lietotāja vadības loģika.
"""

# Šis modulis vada izvēlni un lietotāja ievadi.
# Tas lasa un saglabā izdevumus, izmantojot storage, aprēķina statistiku ar logic
# un eksportē CSV failu ar export moduļa palīdzību.
from datetime import date
from storage import load_expenses, save_expenses
from logic import sum_total, sum_by_category, filter_by_month, get_available_months
from export import export_to_csv


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
        # Mēģina pārvērst ievadi par datetime objektu
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_valid_amount(amount_str):
    """Pārbauda, vai teksts ir derīgs pozitīvs skaitlis."""
    try:
        amount = float(amount_str)
        # Atgriež True tikai tad, ja summa nav negatīva
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
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")
    return input("\nIzvēlies darbību (1-7): ").strip()


def add_expense(expenses):
    """Pievieno jaunu izdevumu ar validāciju."""
    print("\n--- Pievienot izdevumu ---")
    
    # Datuma ievade un validācija
    while True:
        default_date = str(date.today())
        date_input = input(f"Datums (YYYY-MM-DD) [{default_date}]: ").strip()
        if not date_input:
            date_input = default_date
        
        if is_valid_date(date_input):
            break
        print("❌ Nepareizs datums! Izmanto formātu YYYY-MM-DD")
    
    # Kategorijas izvēle no noteiktā saraksta
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
    
    # Summa un validācija
    while True:
        amount_input = input("Summa (EUR): ").strip()
        if is_valid_amount(amount_input):
            amount = float(amount_input)
            break
        print("❌ Lūdzu ievadi derīgu pozitīvu summu")
    
    # Apraksts
    description = input("Apraksts: ").strip()
    
    # Sagatavo izdevuma ierakstu un saglabā
    expense = {
        "date": date_input,
        "amount": round(amount, 2),
        "category": category,
        "description": description
    }
    
    expenses.append(expense)
    save_expenses(expenses)
    
    print(f"\n✓ Pievienots: {date_input} | {category} | {amount:.2f} EUR | {description}")


def display_expenses(expenses, title="Izdevumi"):
    """Parāda izdevumus formatēti."""
    if not expenses:
        print(f"\n❌ Nav reģistrētu {title.lower()}")
        return
    
    # Galvene ar kolonnu nosaukumiem
    print(f"\n{title}:")
    print("─" * 70)
    print(f"{'Datums':<12} {'Summa':>10} {'Kategorija':<18} {'Apraksts'}")
    print("─" * 70)
    
    for i, expense in enumerate(expenses, 1):
        date_str = expense["date"]
        amount_str = f"{expense['amount']:.2f} EUR"
        category = expense["category"]
        description = expense["description"][:20]
        
        # Rindas formatēta izvade ar platumu un līdzinājumu
        print(f"{date_str:<12} {amount_str:>10} {category:<18} {description}")
    
    print("─" * 70)
    total = sum_total(expenses)
    print(f"  Kopā: {total:.2f} EUR ({len(expenses)} ieraksti)")
    print()


def filter_and_display(expenses):
    """Filtrē izdevumus pēc mēneša un parāda tos."""
    if not expenses:
        print("\n❌ Nav reģistrētu izdevumu")
        return
    
    available_months = get_available_months(expenses)
    
    if not available_months:
        print("\n❌ Nav datu par jebkādu mēnesi")
        return
    
    # Parāda pieejamos mēnešus, pēc kuriem var filtrēt
    print("\nPieejamie mēneši:")
    for i, (year, month) in enumerate(available_months, 1):
        print(f"  {i}) {year}-{month:02d}")
    
    while True:
        choice = input("Izvēlies mēnesi (numurs): ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(available_months):
                year, month = available_months[idx]
                break
            else:
                print(f"❌ Lūdzu izvēlies numuru no 1 līdz {len(available_months)}")
        except ValueError:
            print("❌ Lūdzu ievadi numuru")
    
    filtered = filter_by_month(expenses, year, month)
    display_expenses(filtered, f"{year}-{month:02d} izdevumi")


def show_category_summary(expenses):
    """Parāda summas pa kategorijām."""
    if not expenses:
        print("\n❌ Nav reģistrētu izdevumu")
        return
    
    totals = sum_by_category(expenses)
    
    print("\nKopsavilkums pa kategorijām:")
    print("───────────────────────────")
    
    for category, total in sorted(totals.items()):
        # Parāda summu katrai kategorijai atsevišķi
        print(f"  {category:<20} {total:>10.2f} EUR")
    
    print("───────────────────────────")
    grand_total = sum_total(expenses)
    print(f"  KOPĀ: {grand_total:>26.2f} EUR")
    print()


def delete_expense(expenses):
    """Dzēš izdevumu pēc indeksa."""
    if not expenses:
        print("\n❌ Nav reģistrētu izdevumu")
        return
    
    display_expenses(expenses, "Izdevumi")
    
    while True:
        choice = input("Kuru dzēst? (numurs vai 0 lai atceltu): ").strip()
        try:
            idx = int(choice)
            if idx == 0:
                print("Dzēšana atcelta")
                return
            elif 1 <= idx <= len(expenses):
                deleted = expenses.pop(idx - 1)
                save_expenses(expenses)
                print(f"\n✓ Dzēsts: {deleted['date']} | {deleted['category']} | "
                      f"{deleted['amount']:.2f} EUR | {deleted['description']}")
                return
            else:
                print(f"❌ Lūdzu izvēlies numuru no 1 līdz {len(expenses)}")
        except ValueError:
            print("❌ Lūdzu ievadi numuru")


def export_expenses(expenses):
    """Eksportē izdevumus CSV failā."""
    if not expenses:
        print("\n❌ Nav reģistrētu izdevumu, ko eksportēt")
        return
    
    default_file = "izdevumi.csv"
    filename = input(f"Faila nosaukums [{default_file}]: ").strip()
    
    if not filename:
        filename = default_file
    
    # Izsauc eksportēšanas funkciju un paziņo par rezultātu
    if export_to_csv(expenses, filename):
        print(f"\n✓ Eksportēts: {len(expenses)} ieraksti -> {filename}")
    else:
        print(f"\n❌ Kļūda eksportējot failu")


def main():
    """Galvenā programmas cilpa."""
    # Ielādē iepriekš saglabātos izdevumus
    expenses = load_expenses()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            add_expense(expenses)
        
        elif choice == "2":
            display_expenses(expenses)
        
        elif choice == "3":
            filter_and_display(expenses)
        
        elif choice == "4":
            show_category_summary(expenses)
        
        elif choice == "5":
            delete_expense(expenses)
        
        elif choice == "6":
            export_expenses(expenses)
        
        elif choice == "7":
            print("\nUz redzēšanos!")
            break
        
        else:
            print("\n❌ Nepareiza izvēle. Lūdzu mēģini vēlreiz.")


if __name__ == "__main__":
    main()
