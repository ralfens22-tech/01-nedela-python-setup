import sys

from storage import load_list, save_list
from utils import calc_grand_total, calc_line_total, count_units


def add_item(name, qty, price):
    """Pievieno produktu iepirkumu sarakstam."""
    items = load_list()
    item = {"name": name, "qty": qty, "price": price}
    items.append(item)
    save_list(items)
    print(f"Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {calc_line_total(item):.2f} EUR")


def list_items():
    """Parāda visus produktus no saraksta."""
    items = load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")
    for index, item in enumerate(items, start=1):
        line_total = calc_line_total(item)
        print(f"{index}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")


def calculate_total():
    """Aprēķina iepirkumu saraksta kopsummu."""
    items = load_list()
    total = calc_grand_total(items)
    units = count_units(items)
    print(f"Kopā: {total:.2f} EUR ({units} vienības, {len(items)} produkti)")


def clear_list():
    """Notīra visus produktus no saraksta."""
    save_list([])
    print("Iepirkumu saraksts notīrīts.")


def print_usage():
    """Parāda pieejamās komandas."""
    print("Lietošana:")
    print("python shop.py add Maize 3 1.20")
    print("python shop.py list")
    print("python shop.py total")
    print("python shop.py clear")


def main():
    """Apstrādā CLI komandas iepirkumu sarakstam."""
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) != 5:
            print("Kļūda: komandai add vajag nosaukumu, daudzumu un cenu.")
            print_usage()
            return

        try:
            qty = int(sys.argv[3])
            price = float(sys.argv[4])
        except ValueError:
            print("Kļūda: daudzumam jābūt veselam skaitlim un cenai jābūt skaitlim.")
            return

        if qty <= 0:
            print("Kļūda: daudzumam jābūt pozitīvam skaitlim.")
            return

        if price < 0:
            print("Kļūda: cena nedrīkst būt negatīva.")
            return

        add_item(sys.argv[2], qty, price)
        return

    if command == "list":
        list_items()
        return

    if command == "total":
        calculate_total()
        return

    if command == "clear":
        clear_list()
        return

    print_usage()


if __name__ == "__main__":
    main()