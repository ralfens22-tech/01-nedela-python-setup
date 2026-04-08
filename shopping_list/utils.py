def calc_line_total(item):
    """Atgriež vienas rindas summu: daudzums reiz cena par vienību."""
    return item["qty"] * item["price"]


def calc_grand_total(items):
    """Aprēķina visu produktu kopējo summu."""
    return sum(calc_line_total(item) for item in items)


def count_units(items):
    """Saskaita kopējo vienību skaitu sarakstā."""
    return sum(item["qty"] for item in items)