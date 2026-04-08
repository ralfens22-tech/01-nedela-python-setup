import sys

from storage import load_list, save_list


def add_item(name, price):
    """Pievieno produktu iepirkumu sarakstam."""
    items = load_list()
    items.append({"name": name, "price": price})
    save_list(items)
    print(f"Pievienots: {name} ({price:.2f} EUR)")


def list_items():
    """Parāda visus produktus no saraksta."""
    items = load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return

    print("Iepirkumu saraksts:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item['name']} - {item['price']:.2f} EUR")


def calculate_total():
    """Aprēķina iepirkumu saraksta kopsummu."""
    items = load_list()
    total = sum(item["price"] for item in items)
    print(f"Kopā: {total:.2f} EUR ({len(items)} produkti)")


def clear_list():
    """Notīra visus produktus no saraksta."""
    save_list([])
    print("Iepirkumu saraksts notīrīts.")


def print_usage():
    """Parāda pieejamās komandas."""
    print("Lietošana:")
    print("python shop.py add Maize 1.20")
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
        if len(sys.argv) != 4:
            print_usage()
            return

        try:
            price = float(sys.argv[3])
        except ValueError:
            print("Cenai jābūt skaitlim.")
            return

        add_item(sys.argv[2], price)
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