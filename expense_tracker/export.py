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
        with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            
            # Virsraksti
            writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
            
            # Dati
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
