import json  # JSON modulis ļauj nolasīt un saglabāt datus failā.
import os  # OS modulis ļauj pārbaudīt, vai fails eksistē.
import sys  # Sys modulis dod pieeju komandrindas argumentiem.


CONTACTS_FILE = os.path.join(os.path.dirname(__file__), "contacts.json")  # Faila ceļš uz kontaktu datiem.


def load_contacts():
    """Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež []."""
    if not os.path.exists(CONTACTS_FILE):  # Ja faila vēl nav, atgriež tukšu sarakstu.
        return []

    with open(CONTACTS_FILE, "r", encoding="utf-8") as file:  # Atver failu lasīšanai UTF-8 kodējumā.
        return json.load(file)  # Pārvērš JSON saturu par Python sarakstu.


def save_contacts(contacts):
    """Saglabā kontaktu sarakstu JSON failā."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as file:  # Atver failu rakstīšanai.
        json.dump(contacts, file, indent=2, ensure_ascii=False)  # Saglabā kontaktus lasāmā JSON formātā.


def add_contact(name, phone):
    """Pievieno jaunu kontaktu un saglabā failā."""
    contacts = load_contacts()  # Nolasa jau saglabātos kontaktus.
    contacts.append({"name": name, "phone": phone})  # Pievieno jaunu kontaktu sarakstam.
    save_contacts(contacts)  # Saglabā atjaunoto sarakstu failā.
    print(f"Pievienots: {name} ({phone})")  # Parāda apstiprinājuma ziņu lietotājam.


def list_contacts():
    """Parāda visus saglabātos kontaktus."""
    contacts = load_contacts()  # Ielādē visus kontaktus no faila.
    if not contacts:  # Pārbauda, vai saraksts nav tukšs.
        print("Kontaktu saraksts ir tukšs.")
        return

    print("Kontakti:")  # Izvada saraksta virsrakstu.
    for index, contact in enumerate(contacts, start=1):  # Iet cauri kontaktiem ar numerāciju no 1.
        print(f"{index}. {contact['name']} - {contact['phone']}")  # Izvada vienu kontaktu rindā.


def search_contacts(query):
    """Meklē kontaktus pēc vārda daļas."""
    contacts = load_contacts()  # Nolasa visus kontaktus meklēšanai.
    query_lower = query.lower()  # Pārvērš meklējamo tekstu mazajos burtos.
    matches = [contact for contact in contacts if query_lower in contact["name"].lower()]  # Atrod atbilstošos kontaktus.

    if not matches:  # Ja neviena atbilstība nav atrasta.
        print("Nekas netika atrasts.")
        return

    print(f"Atrasti {len(matches)} kontakti:")  # Parāda, cik kontakti atrasti.
    for index, contact in enumerate(matches, start=1):  # Izvada atrastos kontaktus ar numerāciju.
        print(f"{index}. {contact['name']} - {contact['phone']}")


def print_usage():
    """Parāda pieejamās komandas."""
    print("Lietošana:")  # Izvada palīdzības virsrakstu.
    print('python contacts.py add "Vards Uzvards" "+371 26123456"')  # Piemērs kontakta pievienošanai.
    print("python contacts.py list")  # Piemērs visu kontaktu apskatei.
    print("python contacts.py search Anna")  # Piemērs meklēšanai pēc vārda.


def main():
    """Apstrādā komandrindas argumentus."""
    if len(sys.argv) < 2:  # Ja nav norādīta komanda.
        print_usage()  # Parāda palīdzību.
        return

    command = sys.argv[1].lower()  # Nolasa komandu un padara to nereģistrjutīgu.

    if command == "add":  # Apstrādā kontakta pievienošanu.
        if len(sys.argv) != 4:  # Pārbauda, vai padoti visi nepieciešamie argumenti.
            print_usage()
            return
        add_contact(sys.argv[2], sys.argv[3])  # Izsauc pievienošanas funkciju ar vārdu un tālruni.
        return

    if command == "list":  # Apstrādā saraksta parādīšanu.
        list_contacts()  # Izvada visus kontaktus.
        return

    if command == "search":  # Apstrādā meklēšanas komandu.
        if len(sys.argv) != 3:  # Pārbauda, vai dots meklējamais teksts.
            print_usage()
            return
        search_contacts(sys.argv[2])  # Meklē kontaktus pēc lietotāja ievadītā teksta.
        return

    print_usage()  # Ja komanda nav zināma, parāda palīdzību.


if __name__ == "__main__":  # Šis bloks izpildās tikai, ja failu palaiž tieši.
    main()  # Palaiž programmas galveno funkciju.