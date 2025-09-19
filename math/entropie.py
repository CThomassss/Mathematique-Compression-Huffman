import math
from collections import Counter

# Fonction calcul entropie
def calculate_entropy(symbol_counts, total_count):
    entropy = 0
    for count in symbol_counts.values():
        p_i = count / total_count
        entropy -= p_i * math.log2(p_i)
    return entropy

# charge les trois textes du texte1
with open("texte1_premier-text.txt", "r") as file1:
    texte1_premier = file1.read()

with open("texte1_deuxieme-text.txt", "r") as file2:
    texte1_deuxieme = file2.read()

with open("texte1_troisieme-texte.txt", "r") as file3:
    texte1_troisieme = file3.read()

# charge les deux textes du texte1
with open("texte2_premier-texte.txt", "r") as file4:
    texte2_premier = file4.read()

with open("texte2_deuxieme-texte.txt", "r") as file5:
    texte2_deuxieme = file5.read()

# Fonction permettant de calculer l'entropie des lettres et des mots
def process_text(text, type_of_symbol="lettres"):
    if type_of_symbol == "lettres":
        symbol_counts = Counter(text) #compte la fréquence de chaque lettre
    elif type_of_symbol == "mots":
        symbol_counts = Counter(text.split()) #découpe le texte en fonction des espaces et compte la fréquence de chaque mot
    total_count = sum(symbol_counts.values())
    return calculate_entropy(symbol_counts, total_count) #calcule le nombre total de symboles

# Calcul de l'entropie du texte1 en termes de lettres
entropy_texte1_premier_letters = process_text(texte1_premier, "lettres")
entropy_texte1_deuxieme_letters = process_text(texte1_deuxieme, "lettres")
entropy_texte1_troisieme_letters = process_text(texte1_troisieme, "lettres")

# Calcul de l'entropie du texte2 en termes de lettres
entropy_texte2_premier_letters = process_text(texte2_premier, "lettres")
entropy_texte2_deuxieme_letters = process_text(texte2_deuxieme, "lettres")


# Calcule l'entropie du texte2 en termes de mots
entropy_texte2_premier_words = process_text(texte2_premier, "mots")
entropy_texte2_deuxieme_words = process_text(texte2_deuxieme, "mots")

# Resultats du texte1
print(f"Entropie des lettres dans texte1.txt premier texte : {entropy_texte1_premier_letters:.4f} bits")
print(f"Entropie des lettres dans texte1.txt deuxieme texte : {entropy_texte1_deuxieme_letters:.4f} bits")
print(f"Entropie des lettres dans texte1.txt troisieme texte : {entropy_texte1_troisieme_letters:.4f} bits\n")

# Resultats du texte2
print(f"Entropie des lettres dans texte2.txt premier texte : {entropy_texte2_premier_letters:.4f} bits")
print(f"Entropie des lettres dans texte2.txt deuxieme texte : {entropy_texte2_deuxieme_letters:.4f} bits")
print(f"Entropie des mots dans texte2.txt premier texte : {entropy_texte2_premier_words:.4f} bits")
print(f"Entropie des mots dans texte2.txt deuxieme texte : {entropy_texte2_deuxieme_words:.4f} bits\n")



# Texte long (Le Petit Prince')
long_text = """

Lorsque j’avais six ans j’ai vu, une fois, une magnifique image, dans un livre sur la Forêt Vierge qui s’appelait 
Histoires vécues. Ça représentait un serpent boa qui avalait un fauve. Voilà la copie du dessin. On disait dans 
le livre : « Les serpents boas avalent leur proie tout entière, sans la mâcher. Ensuite ils ne peuvent plus bouger 
et ils dorment pendant les six mois de leur digestion. » J’ai alors beaucoup réfléchi sur les aventures de la 
jungle et, à mon tour, j’ai réussi, avec un crayon de couleur, à tracer mon premier dessin. Mon dessin numéro 1. 
Il était comme ça :
    
"""

# Calcule l'entropie du texte long en termes de lettres & mots
entropy_long_text_letters = process_text(long_text, "lettres")
entropy_long_text_words = process_text(long_text, "mots")

# Résultats texte long
print(f"Entropie des lettres dans le texte long : {entropy_long_text_letters:.4f} bits")
print(f"Entropie des mots dans le texte long : {entropy_long_text_words:.4f} bits")
