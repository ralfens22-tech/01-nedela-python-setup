"""
Biznesa loģika — izdevumu analīze, bez failu operācijām vai input/output.
"""


def sum_total(expenses):
    """
    Aprēķina kopējo izdevumu summu.
    
    Parametri:
        expenses (list): Izdevumu masīvs
    
    Atgriež:
        float: Kopējā summa noapaļota līdz 2 zīmēm aiz komata
    """
    if not expenses:
        return 0.0
    
    # Sastāda summu no visām izdevumu summām
    total = sum(exp["amount"] for exp in expenses)
    return round(total, 2)


def sum_by_category(expenses):
    """
    Grupē izdevumus pa kategorijām un aprēķina summu katrai.
    
    Parametri:
        expenses (list): Izdevumu masīvs
    
    Atgriež:
        dict: {kategorija: summa, ...}
    """
    totals = {}
    for expense in expenses:
        category = expense["category"]
        # Pievieno vai papildina summu konkrētajai kategorijai
        totals[category] = totals.get(category, 0) + expense["amount"]
    
    # Noapaļo rezultātu, lai izvade būtu tīra
    return {cat: round(total, 2) for cat, total in totals.items()}


def filter_by_month(expenses, year, month):
    """
    Filtrē izdevumus pēc gada un mēneša.
    
    Parametri:
        expenses (list): Izdevumu masīvs
        year (int): Gads (piemēram, 2025)
        month (int): Mēnesis (1-12)
    
    Atgriež:
        list: Izdevumi, kuri pieder norādītajam mēnesim
    """
    from datetime import datetime
    
    result = []
    for expense in expenses:
        # Pārvērš datuma virkni datuma objektā un salīdzina gadu un mēnesi
        date_obj = datetime.strptime(expense["date"], "%Y-%m-%d")
        if date_obj.year == year and date_obj.month == month:
            result.append(expense)
    
    return result


def get_available_months(expenses):
    """
    Atgriež mēnešu sarakstu, kuros ir izdevumi.
    
    Parametri:
        expenses (list): Izdevumu masīvs
    
    Atgriež:
        list: Kārtots (gads, mēnesis) tuples saraksts, piemēram: [(2025, 2), (2025, 3)]
    """
    from datetime import datetime
    
    months = set()
    for expense in expenses:
        date_obj = datetime.strptime(expense["date"], "%Y-%m-%d")
        # Saglabā unikālus gadus un mēnešus
        months.add((date_obj.year, date_obj.month))
    
    return sorted(list(months))
