def sarakstu_dala():
    # Izvada virsrakstu sarakstu uzdevuma daļai
    print("--- Saraksti ---")

    # Izveido sarakstu ar skaitļiem no 1 līdz 10
    skaitli = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Sākotnējais saraksts: {skaitli}")

    # Pievieno sarakstam jaunu elementu
    skaitli.append(11)
    # Izdzēš pēdējo elementu no saraksta un saglabā to mainīgajā
    iznemtais_elements = skaitli.pop()
    print(f"Pēc append() un pop(): {skaitli} (izņemts: {iznemtais_elements})")

    # Sagatavo mainīgos summas un elementu skaita aprēķinam
    summa = 0
    elementu_skaits = 0

    # Ar for ciklu saskaita visus elementus un to skaitu
    for skaitlis in skaitli:
        summa += skaitlis
        elementu_skaits += 1

    # Aprēķina vidējo vērtību
    videjais = summa / elementu_skaits

    # Izveido jaunu sarakstu tikai ar pāra skaitļiem
    para_skaitli = []
    for skaitlis in skaitli:
        if skaitlis % 2 == 0:
            para_skaitli.append(skaitlis)

    # Parāda dažādus saraksta slice piemērus
    pirmie_tris = skaitli[:3]
    pedejie_divi = skaitli[-2:]
    katrs_otrais = skaitli[::2]

    # Izvada iegūtos rezultātus
    print(f"Summa: {summa}, Vidējais: {videjais}")
    print(f"Pāra skaitļi: {para_skaitli}")
    print(f"Pirmie 3: {pirmie_tris}")
    print(f"Pēdējie 2: {pedejie_divi}")
    print(f"Katrs otrais elements: {katrs_otrais}")


# Funkcija darbam ar vārdnīcām
def vardnicu_dala():
    # Izvada virsrakstu vārdnīcu daļai
    print("\n--- Vārdnīcas ---")

    # Izveido vārdnīcu ar studentu vārdiem un atzīmēm
    studenti = {
        "Anna": 85,
        "Jānis": 72,
        "Līga": 95,
    }

    # Pievieno jaunu studentu
    studenti["Pēteris"] = 88
    # Maina esoša studenta atzīmi
    studenti["Jānis"] = 78

    # Izvada katru studentu un viņa atzīmi
    for vards, atzime in studenti.items(): # jo items() ļauj iegūt gan atslēgu (vārdu), gan vērtību (atzīmi)
        print(f"{vards}: {atzime}") # jo f-string ļauj ērti formatēt tekstu, ievietojot mainīgos tieši tekstā

    # Sagatavo mainīgos labākā studenta meklēšanai
    labakais_students = "" # jo vārds ir teksts, sākumā tas ir tukšs
    augstaka_atzime = -1 # jo atzīmes ir skaitļi, sākumā tas ir negatīvs, lai jebkura atzīme būtu lielāka

    # Atrod studentu ar augstāko atzīmi
    for vards, atzime in studenti.items(): # jo items() ļauj iegūt gan atslēgu (vārdu), gan vērtību (atzīmi)
        if atzime > augstaka_atzime: # jo, ja atzīme ir lielāka par pašreizējo augstāko, tad jāatjaunina augstākā atzīme un labākā studenta vārds
            augstaka_atzime = atzime # jo, ja atzīme ir lielāka par pašreizējo augstāko, tad atjaunojam augstāko atzīmi
            labakais_students = vards # jo, ja atzīme ir lielāka par pašreizējo augstāko, tad atjaunojam gan augstāko atzīmi, gan labākā studenta vārdu

    # Izvada labāko studentu un atgriež vārdnīcu tālākai izmantošanai
    print(f"Labākais students: {labakais_students} ({augstaka_atzime})")
    return studenti


# Funkcija, kas apvieno sarakstus un vārdnīcas
def kombinacijas_dala(studenti):
    # Izveido tukšu sarakstu studentu datu glabāšanai
    studentu_saraksts = []

    # Pārveido vārdnīcu par sarakstu ar vārdnīcām
    for vards, atzime in studenti.items(): # jo items() ļauj iegūt gan atslēgu (vārdu), gan vērtību (atzīmi)
        studentu_saraksts.append({"name": vards, "grade": atzime}) # jo, lai apvienotu vārdnīcu un sarakstu, izveidojam jaunu vārdnīcu ar atslēgām "name" un "grade", un pievienojam to sarakstam

    # Izveido sarakstu tikai ar tiem studentiem, kuriem atzīme ir vismaz 80
    labi_studenti = []
    for students in studentu_saraksts: # jo, lai atlasītu tikai labos studentus, iterējam cauri studentu_sarakstam, kur katrs elements ir vārdnīca ar atslēgām "name" un "grade"
        if students["grade"] >= 80: # jo, ja students["grade"] ir lielāka vai vienāda ar 80, tad pievienojam šo studentu labi_studenti sarakstam
            labi_studenti.append(students) # jo, ja students["grade"] ir lielāka vai vienāda ar 80, tad pievienojam šo studentu labi_studenti sarakstam

    # Formatēti izvada atlasītos studentus ar numerāciju
    print("\n--- Studenti ar atzīmi >= 80 ---")
    for indekss, students in enumerate(labi_studenti, start=1): # jo, lai izvadītu studentus ar numerāciju, izmantojam enumerate(), kas ļauj iegūt gan indeksu, gan studentu vārdnīcu, un start=1 nodrošina, ka numerācija sākas no 1
        print(f"{indekss}. {students['name']} — {students['grade']}") # jo, lai izvadītu studentu ar formatētu tekstu, izmantojam f-string, kur ievietojam indekss, students['name'] un students['grade'] tieši tekstā


# Galvenā funkcija, kas izsauc visas pārējās daļas
def main(): # jo, lai organizētu programmas izpildi, izveidojam galveno funkciju, kas izsauc visas pārējās daļas secīgi
    sarakstu_dala() # jo, lai izpildītu sarakstu daļu, izsaucam sarakstu_dala() funkciju
    studenti = vardnicu_dala() # jo, lai izpildītu vārdnīcu daļu un iegūtu studentu vārdnīcu tālākai izmantošanai, izsaucam vardnicu_dala() funkciju un saglabājam atgriezto vārdnīcu mainīgajā studenti
    kombinacijas_dala(studenti) # jo, lai izpildītu kombinācijas daļu, izsaucam kombinacijas_dala() funkciju, nododot tai studentu vārdnīcu kā argumentu


# Nodrošina, ka programma startējas tikai palaižot šo failu tieši
if __name__ == "__main__": # jo, lai nodrošinātu, ka programma startējas tikai palaižot šo failu tieši, un neizpildās, ja šo failu importē kā moduli citā skriptā, izmantojam if __name__ == "__main__": konstrukciju
    main() # jo, ja __name__ ir "__main__", tad izsaucam galveno funkciju main(), lai startētu programmu
