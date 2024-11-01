<<<<<<< HEAD

# HLAVIČKA souboru
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Luděk Šubrt
email: LSubrt@seznam.cz
discord: 001Marek#7313
"""
# import modulů do Python programu
import re # řádek importuje modul ´re´
import sys # řádek importuje modul ´sys´

# registrovaní uživatelé
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

# ověření uživatele (program vyžaduje jméno  a heslo)
uzivatelske_jmeno = input("Uživatelské jméno:")
heslo = input("Heslo:")

# definice čáry
cara = "=" * 40

# zjišťování jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if uzivatelske_jmeno in users and users[uzivatelske_jmeno]==heslo:
    print(cara)
    print(f"Vítejte v aplikaci, {uzivatelske_jmeno}")
    print("Máme 3 texty k analýze.")
    print(cara)
else: 
    print("Neregistrovaný uživatel, ukončuji program...")
    exit()

# VÝBĚR textu - Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# vlastní VÝBĚR TEXTu
try:
    volba_textu = int(input("Zadejte číslo mezi 1 a 3 pro výběr:"))
except ValueError:
    print("Neplatný vstup. Zadejte číslo.")
    sys.exit()

if not 1 <= volba_textu <= len(TEXTS): # Upravená kontrola rozsahu
    print("Neplatný vstup, ukončuji program...")
    sys.exit()

print(cara)

vybrany_text = TEXTS[volba_textu - 1] # ZÍSKÁME TEXT Z POLE TEXTS

# pomůcka - tisk vybraneho textu
print(vybrany_text)
print(cara)

# ANALÝZA vybraného textu
# 1. Počet slov:
words = re.findall(r'\b\w+\b', vybrany_text.lower())  # Najde všechna slova, ignoruje velká/malá písmena
word_count = len(words) # počet slov

# 2. Počet slov začínajících velkým písmenem:
titlecase_words = len([word for word in vybrany_text.split() if word[0].isupper()])

# 3. Počet slov psaných velkými písmeny:
uppercase_words = len([word for word in vybrany_text.split() if word.isupper()])

# 4. Počet slov psaných malými písmeny:
lowercase_words = len([word for word in vybrany_text.split() if word.islower()])

# 5. Počet a součet čísel:
numbers = re.findall(r'\b\d+\b', vybrany_text)  # Najde všechna čísla
numeric_count = len(numbers) # počet čísel
numeric_sum = sum(map(int, numbers)) # součet čísel

# Výstup ANALÝZY vybraného textu:
print("VYSTUP")
print(cara)
print("Počet slov:", word_count)
print("Počet slov s velkým počátečním písmenem:", titlecase_words)
print("Počet slov psaných velkými písmeny:", uppercase_words)
print("Počet slov psaných malými písmeny:", lowercase_words)
print("Počet čísel:", numeric_count)
print("Součet čísel:", numeric_sum)
print(cara)

# Program zobrazí jednoduchý TEXTOVÝ SLOUPCOVÝ GRAF s Hlavičkou, který bude reprezentovat četnost různých délek slov v textu
def create_text_bar_chart(word_lengths):
    length_counts = {}
    for length in word_lengths:
        length_counts[length] = length_counts.get(length, 0) + 1

    max_count = max(length_counts.values())
    max_length = max(length_counts.keys()) if length_counts else 0

    if max_length==0:
        print("Žádná slova v textu")
        return

    column_width = 20

    print("\nČetnost délek slov:") # HLAVIČKA GRAFU
    print("=" * 40) # HLAVIČKA GRAFU
    print(f"{'Délka':<{max_length+2}} {'Počet':>5}") # HLAVIČKA GRAFU
    print("=" * 40) # HLAVIČKA GRAFU

    for length, count in sorted(length_counts.items()):
        bar = "*" * int((count / max_count) * column_width)
        print(f"{length:{max_length}}: {bar} ({count})")

# Získání délek slov a vykreslení grafu
word_lengths = [len(word) for word in words]
=======

# HLAVIČKA souboru
"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Petr Svetr
email: petr.svetr@gmail.com
discord: Petr Svetr#4490
"""
# import modulů do Python programu
import re # řádek importuje modul ´re´
import sys # řádek importuje modul ´sys´

# registrovaní uživatelé
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

# ověření uživatele (program vyžaduje jméno  a heslo)
uzivatelske_jmeno = input("Uživatelské jméno:")
heslo = input("Heslo:")

# definice čáry
cara = "=" * 40

# zjišťování jestli zadané údaje odpovídají někomu z registrovaných uživatelů
if uzivatelske_jmeno in users and users[uzivatelske_jmeno]==heslo:
    print(cara)
    print(f"Vítejte v aplikaci, {uzivatelske_jmeno}")
    print("Máme 3 texty k analýze.")
    print(cara)
else: 
    print("Neregistrovaný uživatel, ukončuji program...")
    exit()

# VÝBĚR textu - Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# vlastní VÝBĚR TEXTu
try:
    volba_textu = int(input("Zadejte číslo mezi 1 a 3 pro výběr:"))
except ValueError:
    print("Neplatný vstup. Zadejte číslo.")
    sys.exit()

if not 1 <= volba_textu <= len(TEXTS): # Upravená kontrola rozsahu
    print("Neplatný vstup, ukončuji program...")
    sys.exit()

print(cara)

vybrany_text = TEXTS[volba_textu - 1] # ZÍSKÁME TEXT Z POLE TEXTS

# pomůcka - tisk vybraneho textu
print(vybrany_text)
print(cara)

# ANALÝZA vybraného textu
# 1. Počet slov:
words = re.findall(r'\b\w+\b', vybrany_text.lower())  # Najde všechna slova, ignoruje velká/malá písmena
word_count = len(words) # počet slov

# 2. Počet slov začínajících velkým písmenem:
titlecase_words = len([word for word in vybrany_text.split() if word[0].isupper()])

# 3. Počet slov psaných velkými písmeny:
uppercase_words = len([word for word in vybrany_text.split() if word.isupper()])

# 4. Počet slov psaných malými písmeny:
lowercase_words = len([word for word in vybrany_text.split() if word.islower()])

# 5. Počet a součet čísel:
numbers = re.findall(r'\b\d+\b', vybrany_text)  # Najde všechna čísla
numeric_count = len(numbers) # počet čísel
numeric_sum = sum(map(int, numbers)) # součet čísel

# Výstup ANALÝZY vybraného textu:
print("VYSTUP")
print(cara)
print("Počet slov:", word_count)
print("Počet slov s velkým počátečním písmenem:", titlecase_words)
print("Počet slov psaných velkými písmeny:", uppercase_words)
print("Počet slov psaných malými písmeny:", lowercase_words)
print("Počet čísel:", numeric_count)
print("Součet čísel:", numeric_sum)
print(cara)

# Program zobrazí jednoduchý TEXTOVÝ SLOUPCOVÝ GRAF s Hlavičkou, který bude reprezentovat četnost různých délek slov v textu
def create_text_bar_chart(word_lengths):
    length_counts = {}
    for length in word_lengths:
        length_counts[length] = length_counts.get(length, 0) + 1

    max_count = max(length_counts.values())
    max_length = max(length_counts.keys()) if length_counts else 0

    if max_length==0:
        print("Žádná slova v textu")
        return

    column_width = 20

    print("\nČetnost délek slov:") # HLAVIČKA GRAFU
    print("=" * 40) # HLAVIČKA GRAFU
    print(f"{'Délka':<{max_length+2}} {'Počet':>5}") # HLAVIČKA GRAFU
    print("=" * 40) # HLAVIČKA GRAFU

    for length, count in sorted(length_counts.items()):
        bar = "*" * int((count / max_count) * column_width)
        print(f"{length:{max_length}}: {bar} ({count})")

# Získání délek slov a vykreslení grafu
word_lengths = [len(word) for word in words]
>>>>>>> 9ed0a8be1ea9c7104e1c95937b579c0cbf6d2cb4
create_text_bar_chart(word_lengths)