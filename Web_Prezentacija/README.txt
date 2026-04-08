═══════════════════════════════════════════════════
  Python Projektu Prezentācija — Palaišanas pamācība
═══════════════════════════════════════════════════

PRASĪBAS
--------
  - Python 3.10 vai jaunāks  →  https://www.python.org/downloads/
  - Interneta savienojums (tikai pirmo reizi, Flask instalācijai)


PALAIŠANA — 3 SOĻI
-------------------

1. Atver termināli (PowerShell vai CMD) un pārvietojies uz šo mapi:

       cd ceļš\uz\01-nedela-python-setup\Web_Prezentacija

2. Instalē nepieciešamās bibliotēkas (tikai pirmo reizi):

       pip install -r requirements.txt

3. Palaiž serveri:

       python app.py

4. Atver pārlūkprogrammu un ievadi adresi:

       http://localhost:5000


APTURĒŠANA
----------
  Terminālī nospied  Ctrl + C


KAS NAV NEPIECIEŠAMS
--------------------
  - nginx, Apache vai XAMPP
  - Datu bāzes uzstādīšana (dati tiek glabāti JSON failos automātiski)


PROJEKTA STRUKTŪRA
------------------

  Web_Prezentacija/
  ├── app.py              ← Flask serveris (galvenā programma)
  ├── requirements.txt    ← Nepieciešamās bibliotēkas
  ├── README.txt          ← Šī pamācība
  └── templates/
      └── index.html      ← Web saskarne pārlūkā

  Dati tiek glabāti:
  ├── contacts.json       ← Kontaktu grāmatiņas dati
  └── shopping_list/
      ├── shopping.json   ← Iepirkumu saraksta dati
      └── prices.json     ← Cenu datubāze

═══════════════════════════════════════════════════
