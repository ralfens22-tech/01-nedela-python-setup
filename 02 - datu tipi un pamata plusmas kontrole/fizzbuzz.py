#Fizzbuzz
import sys

# =========================
# PARAMETRI
# =========================

# Dalītāji un atbilstošie vārdi
rules = [
    (3, "Fizz"),
    (5, "Buzz"),
    (7, "Jazz")
]


# =========================
# IEVADE UN PĀRBAUDE
# =========================

if len(sys.argv) < 2:
    print("❌ Kļūda: jāievada skaitlis")
    print("Lietošana: python fizzbuzz.py <N>")
    sys.exit(1)

try:
    N = int(sys.argv[1])
    if N <= 0:
        print(f"❌ Kļūda: '{N}' jābūt pozitīvam skaitlim")
        sys.exit(1)

except ValueError:
    print(f"❌ Kļūda: '{sys.argv[1]}' nav skaitlis")
    sys.exit(1)


# =========================
# FIZZBUZZ LOĢIKA
# =========================

results = []

for num in range(1, N + 1): # Iterē cauri visiem skaitļiem no 1 līdz N (ieskaitot)
    output = "" # Sākotnēji output ir tukšs, un mēs to aizpildīsim atkarībā no tā, vai num dalās ar kādu no divisor sarakstā rules
    
    # Pārbauda visus noteikumus
    for divisor, word in rules: # Pārbauda, vai num dalās ar divisor, un ja jā, tad pievieno atbilstošo word output mainīgajam
        if num % divisor == 0: # Ja num dalās ar divisor, tad pievieno atbilstošo word output mainīgajam
            output += word # Ja num dalās ar divisor, tad pievieno atbilstošo word output mainīgajam
    
    # Ja nedalās, tad izvada pašu skaitli
    if output == "": # Ja output ir tukšs, tas nozīmē, ka num nedalās ne ar vienu no divisor, tāpēc izvada pašu num
        output = str(num) # Ja output ir tukšs, tas nozīmē, ka num nedalās ne ar vienu no divisor, tāpēc izvada pašu num, konvertējot to uz string, lai varētu pievienot results sarakstam
    
    results.append(output) # Pievieno output rezultātu sarakstam, lai vēlāk varētu izvadīt visus rezultātus kopā


# =========================
# IZVADE
# =========================

print(", ".join(results))