# Izdevumu izsekotāja plāns

## A. Programmas apraksts

Izdevumu izsekotājs ir Python komandrindas lietojums, kas ļauj lietotājam reģistrēt un analizēt ikdienas izdevumus. Programma saglabā izdevumus JSON failā, ļauj tos filtrēt pēc mēneša, grupēt pa kategorijām, dzēst, un eksportēt CSV formātā. Galvenais mērķis ir sniegt lietotājam vienkāršu un ērti lietojamu rīku personīgo finanšu pārvaldībai caur komandrindi.

## B. Datu struktūra

### Izdevuma ieraksts (viens objekts)

```json
{
  "date": "2025-02-15",
  "amount": 12.50,
  "category": "Ēdiens",
  "description": "Pusdienas kafejnīcā"
}
```

### Pilna faila struktūra (expenses.json)

```json
[
  {
    "date": "2025-02-15",
    "amount": 12.50,
    "category": "Ēdiens",
    "description": "Pusdienas kafejnīcā"
  },
  {
    "date": "2025-02-16",
    "amount": 3.40,
    "category": "Transports",
    "description": "Autobusa biļete"
  }
]
```

### Kāpēc šāda struktūra?

- **JSON masīvs** — vienkārši saglabā un nolasa vairākus ierakstus
- **date** — string (YYYY-MM-DD) ļauj viegli filtrēt pēc mēneša
- **amount** — skaitlis izdevumu summai (citroni centi kā decimāldaļa)
- **category** — category valīdzības par iepriekš definētu sarakstu
- **description** — string lietotāja paskaidrojumam, ko viņš iztērēja

## C. Moduļu plāns

### Faili un to funkcijas

| Fails | Mērķis | Atbildību zona |
|-------|--------|-----------------|
| `storage.py` | JSON operācijas | Nolasīt un saglabāt expenses.json |
| `logic.py` | Biznesa loģika | Filtrēšana, grupēšana, summas (bez IO) |
| `app.py` | Galvenā programma | Izvēlne, lietotāja ievade, izvade |
| `export.py` | CSV eksports | Datu eksportēšana uz CSV failu |
| `expenses.json` | Datu kopa | Saglabāti izdevumi (tiek izveidots automātiski) |

### Funkcijas katram modulim

#### storage.py
- `load_expenses()` — nolasa expenses.json, atgriež masīvu
- `save_expenses(expenses)` — saglabā expenses masīvu JSON failā

#### logic.py
- `sum_total(expenses)` — atgriež kopējo summu
- `filter_by_month(expenses, year, month)` — atgriež izdevumus no konkrēta mēneša
- `sum_by_category(expenses)` — atgriež dict: kategorija → summa
- `get_available_months(expenses)` — atgriež pieejamos mēnešus [(2025, 2), (2025, 3), ...]

#### app.py
- `show_menu()` — parāda izvēlni, atgriež lietotāja izvēli
- `add_expense(expenses)` — pievieno jaunus izdevumus (ar input validāciju)
- `display_expenses(expenses)` — rāda visus izdevumus formatēti
- `filter_and_display(expenses)` — filtrē pēc mēneša un rāda
- `show_category_summary(expenses)` — parāda summas pa kategorijām
- `delete_expense(expenses)` — dzēš izdevumu pēc indeksa
- `main()` — galvenā cilpa

#### export.py
- `export_to_csv(expenses, filepath)` — eksportē uz CSV

## D. Lietotāja scenāriji

### Scenārijs 1: Jaunas ieraksta pievienošana

```
Lietotājs: Izvēlas "Pievienot izdevumu"
Programma: Pieprasa datumu (default — šodiena)
Lietotājs: Nospiedj Enter
Programma: Parāda kategoriju sarakstu
Lietotājs: Izvēlas 1 (Ēdiens)
Programma: Pieprasa summu
Lietotājs: Ievada 12.50
Programma: Pieprasa aprakstu
Lietotājs: Ievada "Pusdienojums"
Programma: ✓ Pievienots: 2025-02-25 | Ēdiens | 12.50 EUR | Pusdienojums
```

### Scenārijs 2: Izdevumu filtrēšana pēc mēneša

```
Lietotājs: Izvēlas "Filtrēt pēc mēneša"
Programma: Parāda pieejamos mēnešus (2025-02, 2025-03, ...)
Lietotājs: Izvēlas 2025-02
Programma: Parāda tikai februāra izdevumus ar kopsummu
```

### Scenārijs 3: Izdevuma dzēšana

```
Lietotājs: Izvēlas "Dzēst izdevumu"
Programma: Parāda numurētu sarakstu ar visiem izdevumiem
Lietotājs: Ievada 1 (dzēš pirmo)
Programma: ✓ Dzēsts: 2025-02-15 | Ēdiens | 12.50 EUR
```

## E. Robežgadījumi

### 1. Ja expenses.json neeksistē
- **Risinājums**: `load_expenses()` atgriež tukšu masīvu `[]`
- Failu automātiski izveido pie pirmā izdevuma pievienošanas

### 2. Ja lietotājs ievada negatīvu summu
- **Validācija**: `add_expense()` pārbauda `amount >= 0`
- Ja nepareizi — parāda kļūdas paziņojumu un ļauj mēģināt vēlreiz

### 3. Ja lietotājs ievada nepareizu datumu
- **Validācija**: Pārbauda vai datums atbilst YYYY-MM-DD formātam
- Pieļauj default (šodiena), ja lietotājs nespiedj Enter

### 4. Ja apraksts ir tukšs
- **Dēkstīt atļauja**: Lietotājs var atstāt tukšu (galvenais ir datums, summa, kategorija)

### 5. Ja saraksts ir tukšs un lietotājs izvēlas "Parādīt"
- **Ziņojums**: "Nav reģistrētu izdevumu" vai "Jums nav datu"

### 6. Ja lietotājs izvēlas nepareizu kategoriju numuru
- **Validācija**: Pārbauda vai numurs ir diapazonā 1-7
- Parāda kļūdas paziņojumu un ļauj atkārtoti izvēlēties

### 7. Ja lietotājs mēģina dzēst ierakstu, kuram nav tāda numura
- **Ziņojums**: "Nepareizs numurs. Mēģiniet vēlreiz."

### 8. Ja CSV eksporta failu nevar izveidot (permissions)
- **Error handling**: Parāda informāciju, ko dara vēl

---

**Piezīme**: Šis plāns var mainīties izstrādes gaitā — tas ir sākumpunkts, nevis galīgais līgums.
