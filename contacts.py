import json
import os
import sys


CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")


def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):
        return []

    with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=2, ensure_ascii=False)


def add_contact(name, phone):
    """Pievieno jaunu kontaktu un saglabā failā."""
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"Pievienots: {name} ({phone})")


def list_contacts():
    """Parāda visus saglabātos kontaktus."""
    contacts = load_contacts()
    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return

    print("Kontakti:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")


def search_contacts(query):
    """Meklē kontaktus pēc vārda daļas."""
    contacts = load_contacts()
    query_lower = query.lower()
    matches = [contact for contact in contacts if query_lower in contact["name"].lower()]

    if not matches:
        print("Nekas netika atrasts.")
        return

    print(f"Atrasti {len(matches)} kontakti:")
    for index, contact in enumerate(matches, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")


def print_usage():
    """Parāda pieejamās komandas."""
    print("Lietošana:")
    print('python contacts.py add "Vards Uzvards" "+371 26123456"')
    print("python contacts.py list")
    print("python contacts.py search Anna")


def main():
    """Apstrādā komandrindas argumentus."""
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1].lower()

    if command == "add":
        if len(sys.argv) != 4:
            print_usage()
            return
        add_contact(sys.argv[2], sys.argv[3])
        return

    if command == "list":
        list_contacts()
        return

    if command == "search":
        if len(sys.argv) != 3:
            print_usage()
            return
        search_contacts(sys.argv[2])
        return

    print_usage()


if __name__ == "__main__":
    main()