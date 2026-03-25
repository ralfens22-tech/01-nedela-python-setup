# =========================
# KONSTANTES
# =========================

KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020


# =========================
# GALVENĀ PROGRAMMA
# =========================

print("Izvēlies konversiju:")
print("1) km <-> mi")
print("2) kg <-> lb")
print("3) L <-> gal")
print("4) USD <-> EUR")

choice = input("> ")


# =========================
# KM <-> MI
# =========================

if choice == "1":
    print("Virziens: 1) km -> mi 2) mi -> km")
    direction = input("> ")

    if direction not in ["1", "2"]:
        print("❌ Nepareizs virziens!")
    else:
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * KM_TO_MI
            print(f"{value:.2f} km = {result:.2f} mi")

        elif direction == "2":
            result = value / KM_TO_MI
            print(f"{value:.2f} mi = {result:.2f} km")

# =========================
# KG <-> LB
# =========================

elif choice == "2":
    print("Virziens: 1) kg -> lb 2) lb -> kg")
    direction = input("> ")

    if direction not in ["1", "2"]:
        print("❌ Nepareizs virziens!")
    else:
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * KG_TO_LB
            print(f"{value:.2f} kg = {result:.2f} lb")

        elif direction == "2":
            result = value / KG_TO_LB
            print(f"{value:.2f} lb = {result:.2f} kg")

# =========================
# L <-> GAL
# =========================

elif choice == "3":
    print("Virziens: 1) L -> gal 2) gal -> L")
    direction = input("> ")

    if direction not in ["1", "2"]:
        print("❌ Nepareizs virziens!")
    else:
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * L_TO_GAL
            print(f"{value:.2f} L = {result:.2f} gal")

        elif direction == "2":
            result = value / L_TO_GAL
            print(f"{value:.2f} gal = {result:.2f} L")

# =========================
# USD <-> EUR
# =========================

elif choice == "4":
    print("Virziens: 1) USD -> EUR 2) EUR -> USD")
    direction = input("> ")

    if direction not in ["1", "2"]:
        print("❌ Nepareizs virziens!")
    else:
        value = float(input("Ievadi vērtību: "))

        if direction == "1":
            result = value * USD_TO_EUR
            print(f"{value:.2f} USD = {result:.2f} EUR")

        elif direction == "2":
            result = value / USD_TO_EUR
            print(f"{value:.2f} EUR = {result:.2f} USD")

# =========================
# NEPAREIZA IZVĒLE
# =========================

else:
    print("❌ Nepareiza izvēle!")