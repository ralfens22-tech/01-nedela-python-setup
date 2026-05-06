# Izdevumu izsekotājs

Komandrindas Python lietojums personīgo izdevumu uzskaitei un analīzei.

## Uzstādīšana

```bash
git clone https://github.com/tavs-lietotajvards/expense-tracker.git
cd expense-tracker/expense_tracker
python app.py
```

Nav nepieciešamas papildus bibliotēkas — tikai Python 3.10+.

## Lietošana

Programma darbojas interaktīvā režīmā ar izvēlni:

```
═════════════════════════════════
  Izdevumu izsekotājs
═════════════════════════════════
1) Pievienot izdevumu
2) Parādīt izdevumus
3) Filtrēt pēc mēneša
4) Kopsavilkums pa kategorijām
5) Dzēst izdevumu
6) Eksportēt CSV
7) Iziet
```

### Komandas

**1) Pievienot izdevumu** — Reģistrē jaunu izdevumu ar datumu, kategoriju, summu un aprakstu

**2) Parādīt izdevumus** — Rāda visus reģistrētos izdevumus formatētas tabulā

**3) Filtrēt pēc mēneša** — Filtrē un rāda izdevumus konkrētam mēnesim

**4) Kopsavilkums pa kategorijām** — Parāda, cik iztērēts katrā kategorijā

**5) Dzēst izdevumu** — Dzēš izvēlētu izdevumu no saraksta

**6) Eksportēt CSV** — Eksportē visus izdevumus CSV failā (atvērti Excel)

**7) Iziet** — Pabeigt programmu

## Kategorijas

Programma pieļauj šādas kategorijas:
- Ēdiens
- Transports
- Izklaide
- Komunālie maksājumi
- Veselība
- Iepirkšanās
- Cits

## Datu formāts

Izdevumi saglabājas JSON failā `expenses.json`:

```json
[
  {
    "date": "2026-05-06",
    "amount": 25.50,
    "category": "Ēdiens",
    "description": "Pusdienojums restoranā"
  }
]
```

CSV eksportā dati izskatīsies:
```
Datums,Summa,Kategorija,Apraksts
2026-05-06,25.50,Ēdiens,Pusdienojums restoranā
```

## Autors

Tavs Vārds — Programmēšanas pamati, 2026
