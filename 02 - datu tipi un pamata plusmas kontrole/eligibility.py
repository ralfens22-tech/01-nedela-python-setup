#Eligibility Checker
# =========================
# PALĪGFUNKCIJAS
# =========================

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("❌ Vecums nevar būt negatīvs!")
                continue
            return value
        except ValueError:
            print("❌ Kļūda: jāievada vesels skaitlis!")


def get_bool_input(prompt, age=None, min_age=None):
    if min_age is not None and age is not None and age < min_age:
        print(f"❌ Jābūt vismaz {min_age} gadi. Automātiski iestatīts 'Nē'.")
        return False
    
    while True:
        value = input(prompt).strip().lower()
        if value == "j":
            return True
        elif value == "n":
            return False
        else:
            print("❌ Kļūda: ievadi 'j' vai 'n'")


# =========================
# IEVADE
# =========================

age = get_int_input("Ievadi vecumu: ")
has_license = get_bool_input("Vai ir autovadītāja apliecība? (j/n): ", age, 18)
is_student = get_bool_input("Vai ir students? (j/n): ", age, 16)
is_veteran = get_bool_input("Vai ir veterāns? (j/n): ", age, 18)


# =========================
# LOĢIKA
# =========================

can_vote = age >= 18
can_rent = (age >= 21) and has_license
senior_discount = age >= 65
student_discount = (age >= 16) and (age <= 26) and is_student


# =========================
# IZVADE
# =========================

print("\n---\n")
print(f"Balsošana: {'Jā ✓' if can_vote else 'Nē ✗'}")
print(f"Auto īre: {'Jā ✓' if can_rent else 'Nē ✗'}")
print(f"Senioru atlaide: {'Jā ✓' if senior_discount else 'Nē ✗'}")
print(f"Studentu atlaide: {'Jā ✓' if student_discount else 'Nē ✗'}")