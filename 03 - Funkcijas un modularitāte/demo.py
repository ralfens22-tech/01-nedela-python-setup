"""Demonstracijas skripts utils un validators funkcijam."""

from utils import average, capitalize, clamp, count_words, factorial, is_prime, total, truncate
from validators import is_email, is_phone_number, is_strong_password, is_valid_age, is_valid_date


def run_demo():
    """Palaiz demonstracijas piemerus terminali."""
    print("=== Utils funkcijas ===")
    print("capitalize('python') ->", capitalize("python"))
    print("truncate('Sis ir loti gars teksts', 12) ->", truncate("Sis ir loti gars teksts", 12))
    print("count_words('Python ir loti noderigs') ->", count_words("Python ir loti noderigs"))
    print("clamp(15, 0, 10) ->", clamp(15, 0, 10))
    print("is_prime(29) ->", is_prime(29))
    print("factorial(5) ->", factorial(5))
    print("total([2, 4, 6]) ->", total([2, 4, 6]))
    print("average([2, 4, 6]) ->", average([2, 4, 6]))

    print("\n=== Validators funkcijas ===")
    print("is_email('anna@inbox.lv') ->", is_email("anna@inbox.lv"))
    print("is_email('anna@') ->", is_email("anna@"))
    print("is_phone_number('+371 26123456') ->", is_phone_number("+371 26123456"))
    print("is_phone_number('26123456') ->", is_phone_number("26123456"))
    print("is_valid_age(25) ->", is_valid_age(25))
    print("is_valid_age(151) ->", is_valid_age(151))
    print("is_strong_password('abc12345') ->", is_strong_password("abc12345"))
    print("is_strong_password('abcdefgh') ->", is_strong_password("abcdefgh"))
    print("is_valid_date('2026-04-01') ->", is_valid_date("2026-04-01"))
    print("is_valid_date('2026-02-30') ->", is_valid_date("2026-02-30"))


if __name__ == "__main__":
    run_demo()
