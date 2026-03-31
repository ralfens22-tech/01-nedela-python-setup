from math import isqrt  # Importē kvadrātsaknes funkciju

Number = int | float  # Šeit definējam tipu: skaitlis var būt int vai float

# ---------- Virkņu funkcijas ----------
def capitalize(text: str = "") -> str:  # Padara pirmo burtu lielu
    """Padara pirmo burtu lielu.
    Args: text (str) - ievades teksts.
    Returns: str - teksts ar lielo sākumburtu.
    Example: capitalize("hello") -> "Hello"
    """
    if not isinstance(text, str):  # Pārbauda, vai ievade tiešām ir teksts
        raise TypeError("text jābūt virknei (str).")  # Ja nē, parāda kļūdu
    return "" if text == "" else text[0].upper() + text[1:]  # Ja tukšs, atgriež tukšu; citādi izmaina 1. burtu


def truncate(text: str, max_len: int = 20, suffix: str = "...") -> str:  # Saīsina tekstu
    """Saīsina tekstu un pievieno daudzpunkti.
    Args: text (str), max_len (int), suffix (str).
    Returns: str - oriģināls vai saīsināts teksts.
    Example: truncate("This is a very long text", 10) -> "This is..."
    """
    if not isinstance(text, str):  # Pārbauda text tipu
        raise TypeError("text jābūt virknei (str).")
    if not isinstance(max_len, int) or isinstance(max_len, bool):  # Pārbauda max_len tipu
        raise TypeError("max_len jābūt veselam skaitlim.")
    if not isinstance(suffix, str):  # Pārbauda suffix tipu
        raise TypeError("suffix jābūt virknei (str).")
    if max_len < 0:  # Neļauj negatīvu garumu
        raise ValueError("max_len nedrīkst būt negatīvs.")
    if len(text) <= max_len:  # Ja teksts jau ir pietiekami īss
        return text  # Atgriež oriģinālo tekstu
    if max_len <= len(suffix):  # Ja vietas ir ļoti maz
        return suffix[:max_len]  # Atgriež tikai daļu no sufiksa
    return text[: max_len - len(suffix)] + suffix  # Nogriež tekstu un pieliek ...


def count_words(text: str) -> int:  # Saskaita vārdus tekstā
    """Saskaita vārdus tekstā.
    Args: text (str) - pārbaudāmais teksts.
    Returns: int - vārdu skaits.
    Example: count_words("Python ir foršs") -> 3
    """
    if not isinstance(text, str):  # Pārbauda, vai padotais ir teksts
        raise TypeError("text jābūt virknei (str).")
    return 0 if text.strip() == "" else len(text.split())  # Ja tukšs, 0; citādi saskaita vārdus


# ---------- Skaitļu funkcijas ----------
def clamp(num: Number, low: Number, high: Number) -> Number:  # Ierobežo vērtību diapazonā
    """Ierobežo skaitli diapazonā.
    Args: num (int|float), low (int|float), high (int|float).
    Returns: int|float - ierobežotā vērtība.
    Example: clamp(15, 0, 10) -> 10
    """
    for value, name in ((num, "num"), (low, "low"), (high, "high")):  # Pārbauda visus 3 parametrus
        if not isinstance(value, (int, float)) or isinstance(value, bool):  # Tiem jābūt skaitļiem
            raise TypeError(f"{name} jābūt skaitlim.")
    if low > high:  # Pārbauda, vai robežas ir loģiskas
        raise ValueError("low nedrīkst būt lielāks par high.")
    return max(low, min(num, high))  # Iespiež skaitli starp low un high


def is_prime(num: int) -> bool:  # Pārbauda, vai skaitlis ir pirmskaitlis
    """Pārbauda, vai skaitlis ir pirmskaitlis.
    Args: num (int) - pārbaudāmais skaitlis.
    Returns: bool - True vai False.
    Example: is_prime(7) -> True
    """
    if not isinstance(num, int) or isinstance(num, bool):  # Pieņem tikai veselus skaitļus
        raise TypeError("num jābūt veselam skaitlim.")
    if num < 2:  # Skaitļi mazāki par 2 nav pirmskaitļi
        return False
    if num == 2:  # 2 ir pirmskaitlis
        return True
    if num % 2 == 0:  # Citi pāra skaitļi nav pirmskaitļi
        return False

    for dalitajs in range(3, isqrt(num) + 1, 2):  # Pārbauda iespējamos dalītājus
        if num % dalitajs == 0:  # Ja dalās bez atlikuma
            return False  # Tātad nav pirmskaitlis
    return True  # Ja neviens neder, tad ir pirmskaitlis


def factorial(n: int) -> int:  # Aprēķina n!
    """Aprēķina faktoriāli n!.
    Args: n (int) - nenegatīvs vesels skaitlis.
    Returns: int - faktoriāla vērtība.
    Example: factorial(5) -> 120
    """
    if not isinstance(n, int) or isinstance(n, bool):  # Pārbauda tipu
        raise TypeError("n jābūt veselam skaitlim.")
    if n < 0:  # Neļauj negatīvus skaitļus
        raise ValueError("n jābūt lielākam vai vienādam ar 0.")

    rezultats = 1  # Sāk ar 1
    for skaitlis in range(2, n + 1):  # Iet cauri skaitļiem no 2 līdz n
        rezultats *= skaitlis  # Reizina klāt nākamo skaitli
    return rezultats  # Atgriež gatavo faktoriāli


# ---------- Sarakstu funkcijas ----------
def total(numbers: list[Number]) -> Number:  # Saskaita visus elementus sarakstā
    """Saskaita saraksta elementus.
    Args: numbers (list) - skaitļu saraksts.
    Returns: int|float - visu elementu summa.
    Example: total([1, 2, 3, 4]) -> 10
    """
    if not isinstance(numbers, list):  # Pārbauda, vai ievade ir saraksts
        raise TypeError("numbers jābūt sarakstam (list).")

    summa = 0  # Sākuma summa ir 0
    for value in numbers:  # Iet cauri katram elementam
        if not isinstance(value, (int, float)) or isinstance(value, bool):  # Katram jābūt skaitlim
            raise TypeError("Visiem saraksta elementiem jābūt skaitļiem.")
        summa += value  # Pieskaita elementu summai
    return summa  # Atgriež gala summu


def average(numbers: list[Number]) -> float:  # Aprēķina vidējo vērtību
    """Aprēķina vidējo aritmētisko.
    Args: numbers (list) - skaitļu saraksts.
    Returns: float - vidējā vērtība.
    Example: average([2, 4, 6]) -> 4.0
    """
    if not isinstance(numbers, list):  # Pārbauda, vai ir saraksts
        raise TypeError("numbers jābūt sarakstam (list).")
    if not numbers:  # Pārbauda, vai saraksts nav tukšs
        raise ValueError("numbers saraksts nedrīkst būt tukšs.")

    skaits = 0  # Skaitīs, cik elementu ir sarakstā
    for _ in numbers:  # Iet cauri katram elementam
        skaits += 1  # Palielina elementu skaitu par 1
    return total(numbers) / skaits  # Summa dalīta ar elementu skaitu


# ---------- Demonstrācija ----------
if __name__ == "__main__":  # Šo daļu izpilda tikai tad, ja failu palaiž tieši
    print("--- Virkņu funkcijas ---")  # Virsraksts virkņu piemēriem
    print("capitalize:", capitalize("hello"))  # Parāda capitalize darbību
    print("truncate:", truncate("Šis ir ļoti garš demonstrācijas teksts", 18))  # Parāda truncate darbību
    print("count_words:", count_words("Python funkcijas ir ļoti noderīgas"))  # Parāda vārdu skaitu

    print("\n--- Skaitļu funkcijas ---")  # Virsraksts skaitļu piemēriem
    print("clamp:", clamp(15, 0, 10))  # Parāda clamp darbību
    print("is_prime:", is_prime(17))  # Parāda pirmskaitļa pārbaudi
    print("factorial:", factorial(5))  # Parāda faktoriāla aprēķinu

    print("\n--- Sarakstu funkcijas ---")  # Virsraksts sarakstu piemēriem
    demo_numbers = [4, 8, 15, 16, 23, 42]  # Piemēra saraksts
    print("total:", total(demo_numbers))  # Parāda summu
    print("average:", average(demo_numbers))  # Parāda vidējo vērtību
