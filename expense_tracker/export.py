"""
CSV eksports modulis — izdevumu eksportēšana CSV failā.
"""

import csv


def export_to_csv(expenses, filepath):
    """
    Eksportē izdevumus CSV failā.
    
    Parametri:
        expenses (list): Izdevumu masīvs
        filepath (str): Ceļš, kur saglabāt CSV failu
    
    Atgriež:
        bool: True, ja eksports bija veiksmīgs, False citādi
    """
    if not expenses:
        return False
    
    try:
        # Atver CSV failu ar UTF-8 BOM kodējumu, lai tas labāk atvērtos Excel
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            
            # Galvenes rindā ieraksta kolonnas nosaukumus
            writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
            
            # Katru izdevumu ieraksta kā jaunu CSV rindu
            for expense in expenses:
                writer.writerow([
                    expense["date"],
                    f"{expense['amount']:.2f}",
                    expense["category"],
                    expense["description"],
                ])
        
        return True
    
    except IOError as e:
        print(f"Kļūda eksportējot: {e}")
        return False
