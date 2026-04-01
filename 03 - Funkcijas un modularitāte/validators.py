import re  # Importējam regulāro izteiksmju moduli teksta formātu pārbaudei.
from datetime import datetime  # Importējam datetime klasi datuma validācijai.


def is_email(text):  # Definējam funkciju, kas pārbauda vienkāršu e-pasta formātu.
	"""Pārbauda, vai teksts satur vienkāršu e-pasta struktūru ar '@' un '.'."""  # Funkcijas docstring apraksts.
	if not isinstance(text, str):  # Ja ievade nav virkne, e-pastu nevar validēt.
		return False  # Atgriežam False, jo ievade nav derīga.

	parts = text.split("@")  # Sadalām tekstu pa '@' simbolu.
	if len(parts) != 2:  # E-pastā jābūt tieši vienam '@'.
		return False  # Ja nav tieši divas daļas, formāts nav derīgs.

	local_part, domain_part = parts  # Piešķiram lokālo un domēna daļu atsevišķiem mainīgajiem.
	if not local_part or not domain_part:  # Pārbaudām, vai abas daļas nav tukšas.
		return False  # Ja kāda daļa ir tukša, e-pasts nav derīgs.

	if "." not in domain_part:  # Pārbaudām, vai domēna daļā ir punkts.
		return False  # Ja punkta nav, e-pasta formāts nav derīgs.

	if domain_part.startswith(".") or domain_part.endswith("."):  # Pārbaudām, vai domēns nesākas/beidzas ar punktu.
		return False  # Šāds domēna formāts nav derīgs.

	return True  # Ja visas pārbaudes izietas, atgriežam True.


def is_phone_number(text):  # Definējam funkciju Latvijas telefona numura validācijai.
	"""Pārbauda, vai numurs atbilst Latvijas formātam '+371 XXXXXXXX'."""  # Funkcijas docstring apraksts.
	if not isinstance(text, str):  # Ja ievade nav virkne, to nevar uzskatīt par derīgu numuru.
		return False  # Atgriežam False nederīgai ievadei.

	pattern = r"^\+371\s\d{8}$"  # Definējam precīzu formātu: +371, atstarpe, un 8 cipari.
	return bool(re.fullmatch(pattern, text))  # Atgriežam True/False atkarībā no pilnas atbilstības.


def is_valid_age(age):  # Definējam funkciju vecuma validācijai.
	"""Pārbauda, vai vecums ir vesels skaitlis intervālā no 0 līdz 150."""  # Funkcijas docstring apraksts.
	if isinstance(age, bool):  # bool Python valodā ir int apakštips, tāpēc to izslēdzam atsevišķi.
		return False  # True/False nav pieņemams vecums.

	if isinstance(age, int):  # Ja jau ir int tips, izmantojam to tālāk.
		value = age  # Saglabājam vecuma vērtību mainīgajā.
	elif isinstance(age, str):  # Ja vecums ir virkne, mēģinām to pārvērst par int.
		if age.strip() == "":  # Tukša vai tikai atstarpju virkne nav derīgs vecums.
			return False  # Atgriežam False tukšai ievadei.
		try:  # Mēģinām droši konvertēt virkni uz int.
			value = int(age)  # Konvertējam virkni uz veselu skaitli.
		except ValueError:  # Ja konvertācija neizdodas (piemēram, '12.5' vai 'abc').
			return False  # Atgriežam False, jo ievade nav vesels skaitlis.
	else:  # Ja tips nav ne int, ne str.
		return False  # Atgriežam False, jo netiek atbalstīts šis ievades tips.

	return 0 <= value <= 150  # Pārbaudām robežas un atgriežam bool rezultātu.


def is_strong_password(text):  # Definējam funkciju paroles stipruma pārbaudei.
	"""Pārbauda, vai parole ir vismaz 8 simbolus gara un satur burtus un ciparus."""  # Funkcijas docstring apraksts.
	if not isinstance(text, str):  # Ja parole nav virkne, to nevar validēt.
		return False  # Atgriežam False nederīgai ievadei.

	if len(text) < 8:  # Pārbaudām minimālo paroles garumu.
		return False  # Ja parole ir par īsu, tā nav stipra.

	has_letter = any(char.isalpha() for char in text)  # Pārbaudām, vai ir vismaz viens burts.
	has_digit = any(char.isdigit() for char in text)  # Pārbaudām, vai ir vismaz viens cipars.
	return has_letter and has_digit  # Atgriežam True tikai tad, ja izpildīti abi nosacījumi.


def is_valid_date(text):  # Definējam funkciju datuma validācijai formātā YYYY-MM-DD.
	"""Pārbauda, vai datums atbilst formātam 'YYYY-MM-DD' un ir kalendāri derīgs."""  # Funkcijas docstring apraksts.
	if not isinstance(text, str):  # Ja ievade nav virkne, datuma validācija nav iespējama.
		return False  # Atgriežam False nederīgai ievadei.

	if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", text):  # Pārbaudām pamatformatu ar 4-2-2 ciparu struktūru.
		return False  # Ja formāts neatbilst, datums nav derīgs.

	try:  # Mēģinām parsēt datumu, lai pārbaudītu, vai tas eksistē kalendārā.
		datetime.strptime(text, "%Y-%m-%d")  # Parsējam datumu pēc prasītā formāta.
	except ValueError:  # Ja datums neeksistē (piemēram, 2024-02-30).
		return False  # Atgriežam False nederīgam datumam.

	return True  # Ja formāts un datuma vērtība ir derīga, atgriežam True.


if __name__ == "__main__":  # Šis bloks izpildās tikai tad, ja failu palaiž tieši.
	print("is_email testi:")  # Izdrukājam sadaļas virsrakstu e-pasta testiem.
	print("anna@inbox.lv ->", is_email("anna@inbox.lv"))  # Derīgs e-pasts.
	print("anna ->", is_email("anna"))  # Trūkst '@' un domēna.
	print("anna@ ->", is_email("anna@"))  # Tukša domēna daļa.
	print()  # Tukša rinda labākai izvades lasāmībai.

	print("is_phone_number testi:")  # Izdrukājam sadaļas virsrakstu telefona testiem.
	print("+371 26123456 ->", is_phone_number("+371 26123456"))  # Derīgs Latvijas numurs.
	print("26123456 ->", is_phone_number("26123456"))  # Trūkst prefiksa un atstarpes.
	print("+371 2612345 ->", is_phone_number("+371 2612345"))  # Par maz ciparu.
	print()  # Tukša rinda labākai izvades lasāmībai.

	print("is_valid_age testi:")  # Izdrukājam sadaļas virsrakstu vecuma testiem.
	print("0 ->", is_valid_age(0))  # Robežgadījums: minimālā pieļaujamā vērtība.
	print("150 ->", is_valid_age(150))  # Robežgadījums: maksimālā pieļaujamā vērtība.
	print("151 ->", is_valid_age(151))  # Virs maksimālās robežas.
	print()  # Tukša rinda labākai izvades lasāmībai.

	print("is_strong_password testi:")  # Izdrukājam sadaļas virsrakstu paroles testiem.
	print("abc12345 ->", is_strong_password("abc12345"))  # Derīga parole: ir burti un cipari.
	print("abcdefgh ->", is_strong_password("abcdefgh"))  # Nav ciparu.
	print("12345678 ->", is_strong_password("12345678"))  # Nav burtu.
	print()  # Tukša rinda labākai izvades lasāmībai.

	print("is_valid_date testi:")  # Izdrukājam sadaļas virsrakstu datuma testiem.
	print("2024-02-29 ->", is_valid_date("2024-02-29"))  # Derīgs lēciengada datums.
	print("2024-02-30 ->", is_valid_date("2024-02-30"))  # Nederīgs datums kalendārā.
	print("2024/02/29 ->", is_valid_date("2024/02/29"))  # Nederīgs formāts (jālieto '-').
