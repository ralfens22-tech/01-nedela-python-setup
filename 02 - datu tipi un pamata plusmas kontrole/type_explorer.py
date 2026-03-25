# type_explorer.py

# =========================
# 1. PAMATA TIPI (katram vismaz 2 vērtības)
# =========================

# str
text1 = "Hello"
text2 = "123"

# int
num1 = 10
num2 = -5

# float
float1 = 3.14
float2 = -0.99

# bool
bool1 = True
bool2 = False

# None
none1 = None
none2 = None


# =========================
# 2. IZVADĪT TIPUS
# =========================

print("=== DATU TIPI ===")

variables = [
    text1, text2,
    num1, num2,
    float1, float2,
    bool1, bool2,
    none1, none2
]

for value in variables:
    print(value, "->", type(value))


# =========================
# 3. TRUTHY / FALSY
# =========================

print("\n=== TRUTHY / FALSY ===")

print(bool(""))     # False (tukša virkne)
print(bool(" "))    # True (atstarpe ir simbols)
print(bool("0"))    # True (jebkura netukša virkne ir True)
print(bool(0))      # False, jo 0 ir "falsy" value
print(bool([]))     # False (tukšs saraksts)
print(bool(None))   # False, jo None ir "falsy" value


# =========================
# 4. KONVERSIJAS
# =========================

print("\n=== KONVERSIJAS ===")

# Pareizas konversijas
print(int("123"))        # 123, jo INT ņem tikai veselo daļu. Ierakstot,piemēram, "3.14", vai "abc" tas izmetīs kļūdu, jo tas nav vesels skaitlis.
print(float(5))          # 5.0, jo FLOAT var saturēt decimāldaļu
print(str(999))          # 999, jo STR var saturēt jebkuru tekstu

# =========================
# 5. KĻŪDAS KONVERSIJĀS
# =========================

print("\n=== KĻŪDAS ===")

# String + int (TypeError)
# print("5" + 3)

# Nepareizi stringi
try:
    int("abc")
except ValueError as e:
    print('int("abc") ->', e)

try:
    float("xyz")
except ValueError as e:
    print('float("xyz") ->', e)

# Float string uz int
try:
    int("3.14")
except ValueError as e:
    print('int("3.14") ->', e)

# None uz int
try:
    int(None)
except TypeError as e:
    print("int(None) ->", e)


# =========================
# 6. INTERESANTI GADĪJUMI
# =========================

print("\n=== INTERESANTI GADĪJUMI ===")

# Virkņu savienošana vs skaitļi
print("5" + "3")          # "53", jo Python savieno virknes
print(int("5") + 3)       # 8, jo int("5") konvertē "5" uz 5, un tad saskaita ar 3

# Bool kā int
print(True + True)        # 2, jo True tiek interpretēts kā 1
print(True * 10)          # 10, jo True tiek interpretēts kā 1
print(False + 5)          # 5, jo False tiek interpretēts kā 0
print(10 / True)          # 10.0, jo True tiek interpretēts kā 1

# Float precizitāte
print(0.1 + 0.2 == 0.3)   # False, jo 0.1 un 0.2 nevar precīzi attēlot binārajā formātā, tāpēc rezultāts ir nedaudz mazāks par 0.3

# Apaļošana
print(round(2.5))         # 2, jo Python apaļo uz tuvāko pāra skaitli, tāpēc 2.5 tiek noapaļots uz 2, nevis 3
print(round(3.5))         # 4 , jo 3.5 tiek noapaļots uz 4, nevis 3

# Pareiza pieeja float -> int
print(int(float("3.14"))) # 3, jo vispirms konvertē "3.14" uz 3.14, un tad int() ņem tikai veselo daļu, rezultātā iegūstot 3