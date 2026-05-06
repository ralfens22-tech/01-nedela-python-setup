# Izstrādes žurnāls

## 1. solis: Plānošana

Sāku ar detāļu plānošanu. Uzskicēju programmas aprakstu, datu struktūru, moduļu 
sadalījumu un lietotāja scenārijus. Grūtākais bija izdomāt, kādas tieši funkcijas 
būtu katram modulim. Beigu beigās nolēmu, ka `logic.py` satur tikai "tīras" 
funkcijas bez IO, `storage.py` darbījas ar JSON, un `app.py` apstrādā 
lietotāja ievadi.

Mācījos: Plānošana pirms kodēšanas seko lielu laiku taupīšanu.

## 2. solis: Pamata darbības

Sāku ar `storage.py` — pārkopēju logiku no 4. nedēļas un pielāgoju jaunajam 
datu formātam. Pēc tam uzrakstīju `logic.py` ar `sum_total()` un citi vienkāršas 
funkcijas.

Visilgāk kavējos pie `app.py` — datuma un summas validācija. Sākumā nemaz 
nezināju par `datetime.strptime()`, bet Google palīdzēja. 

Mācījos: Validācija ir kritiski svarīga — programma nedrīkst avārijas no 
nepareiza ievada.

## 3. solis: Filtrēšana, kopsavilkums, dzēšana

Papildināju `logic.py` ar `filter_by_month()`, `sum_by_category()` un 
`get_available_months()`. Šīs funkcijas ir vienkāršas, bet efektīvas.

App.py papildinājums ar jaunām funkcijām (`filter_and_display()`, 
`show_category_summary()`, `delete_expense()`) bija tieši — katrai funkcijai 
sava loģika, bez pārklāšanās.

Pārbaudīšanas laikā atklāju, ka numurēts saraksts darbībai "Dzēst" ir ļoti 
ērts un intuitīvs.

Mācījos: Labu lietotāja saskarni ir svarīgi — cipari ir labāki par indeksiem.

## 4. solis: CSV eksports un dokumentācija

Izveidoju `export.py` ar `export_to_csv()` funkciju. Svarīgs detaļ ir 
`encoding="utf-8-sig"` — tas nodrošina, ka latviskie burti darbojas Excel 
bez problēmām (BOM marķieris).

Uzrakstīju `README.md` ar uzstādīšanas instrukcijām un lietošanas piemēriem. 
Bija svarīgi, lai tas būtu vienkāršs un saprotams.

Šis žurnāls (`DEVLOG.md`) dokumentē izstrādes procesu — ko dara, ko iemācījos, 
kur bija problēmas.

Mācījos: Dokumentācija ir tikpat svarīga kā pats kods. Labs README palīdz 
citiem lietotājiem (un pašam sev pēc mēneša!) saprast, kā lietot programmu.

---

**Kopumā**: Šis projekts bija lielisks veids, lai apvienotu visas 5. nedēļas 
prasmes — moduli, dati, validācija, git workflow. Būtu pēc iespējas izvairīties 
no ātrākodēšanas un vairāk laika veltīt plānošanai — tas būtu taupījis laiku 
vēlāk!
