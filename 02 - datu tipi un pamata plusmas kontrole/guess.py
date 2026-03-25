#Guessing Game
import random

# =========================
# ĀRĒJAIS CIKLS - SPĒLES ATKĀRTOŠANA
# =========================

while True:
    # =========================
    # SPĒLES SETUP
    # =========================
    
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("\n🎮 Laipni lūgts minēšanas spēlē!")
    print(f"Uzminēt skaitli no 1 līdz 100. Tev ir {max_attempts} mēģinājumi.\n")
    
    # =========================
    # IEKŠĒJAIS CIKLS - MINĒJUMI
    # =========================
    
    while True:
        try:
            guess = int(input(f"Tavs minējums ({max_attempts - attempts} palikusi): "))
            
            # Pārbaudi, vai skaitlis ir diapazonā
            if guess < 1 or guess > 100:
                print("❌ Skaitlis jābūt no 1 līdz 100!")
                continue
            
            attempts += 1 # Palielina mēģinājumu skaitu par 1
            
            # Pārbaudi minējumu
            if guess == secret_number:
                print(f"\n🎉 Pareizi! Skaitlis bija {secret_number}")
                print(f"📊 Tev bija nepieciešami {attempts} mēģinājumi!\n")
                break
            
            elif guess < secret_number:
                print(f"⬆️ Par mazu! Mēģini lielāku skaitli.")
            
            else:
                print(f"⬇️ Par lielu! Mēģini mazāku skaitli.")
            
            # Pārbaudi, vai beidzies mēģinājumu skaits
            if attempts >= max_attempts:
                print(f"\n❌ Beidzies mēģinājumu skaits!")
                print(f"📊 Pareizā atbilde bija: {secret_number}\n")
                break
        
        except ValueError:
            print("❌ Kļūda: jāievada vesels skaitlis!")
            continue
    
    # =========================
    # PIEDĀVĀ SPĒLĒT VĒLREIZ
    # =========================
    
    while True:
        play_again = input("Vai vēlies spēlēt vēlreiz? (j/n): ").strip().lower()
        if play_again == "j":
            break
        elif play_again == "n":
            print("\n👋 Paldies par spēlēšanu! Uz redzēšanos!")
            exit()
        else:
            print("❌ Lūdzu, ievadi 'j' vai 'n'")