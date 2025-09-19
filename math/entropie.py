# On importe les modules nécessaires,
import math  # Pour utiliser la fonction logarithme en base 2
from collections import Counter  # Pour compter facilement la fréquence des lettres ou mots

# -------------------------------
# Fonction pour calculer l'entropie
# -------------------------------
# L'entropie mesure l'incertitude ou la diversité des symboles dans un texte.
# Plus l'entropie est élevée, plus le texte est "imprévisible".
def calculate_entropy(symbol_counts, total_count):
    entropy = 0  # Initialisation de l'entropie
    # Pour chaque symbole (lettre ou mot) du texte
    for count in symbol_counts.values():
        p_i = count / total_count  # Probabilité du symbole
        entropy -= p_i * math.log2(p_i)  # Formule de Shannon pour l'entropie
    return entropy  # Retourne l'entropie en bits

# -------------------------------
# Lecture des fichiers textes
# -------------------------------
# On ouvre chaque fichier et on stocke son contenu dans une variable

# Texte 1 : trois versions différentes
with open("texte1_premier-text.txt", "r") as file1:
    texte1_premier = file1.read()

with open("texte1_deuxieme-text.txt", "r") as file2:
    texte1_deuxieme = file2.read()

with open("texte1_troisieme-texte.txt", "r") as file3:
    texte1_troisieme = file3.read()

# Texte 2 : deux versions différentes
with open("texte2_premier-texte.txt", "r") as file4:
    texte2_premier = file4.read()

with open("texte2_deuxieme-texte.txt", "r") as file5:
    texte2_deuxieme = file5.read()

# -------------------------------
# Fonction pour traiter le texte
# -------------------------------
# Cette fonction compte les symboles (lettres ou mots) et calcule leur entropie
def process_text(text, type_of_symbol="lettres"):
    if type_of_symbol == "lettres":
        # On compte chaque lettre individuellement
        symbol_counts = Counter(text)
    elif type_of_symbol == "mots":
        # On sépare le texte en mots et on compte leur fréquence
        symbol_counts = Counter(text.split())
    
    # Nombre total de symboles (lettres ou mots)
    total_count = sum(symbol_counts.values())
    
    # Calcul de l'entropie à partir des fréquences
    return calculate_entropy(symbol_counts, total_count)

# -------------------------------
# Calcul de l'entropie des lettres pour chaque texte
# -------------------------------
entropy_texte1_premier_letters = process_text(texte1_premier, "lettres")
entropy_texte1_deuxieme_letters = process_text(texte1_deuxieme, "lettres")
entropy_texte1_troisieme_letters = process_text(texte1_troisieme, "lettres")

entropy_texte2_premier_letters = process_text(texte2_premier, "lettres")
entropy_texte2_deuxieme_letters = process_text(texte2_deuxieme, "lettres")

# -------------------------------
# Calcul de l'entropie des mots pour le texte 2
# -------------------------------
entropy_texte2_premier_words = process_text(texte2_premier, "mots")
entropy_texte2_deuxieme_words = process_text(texte2_deuxieme, "mots")

# -------------------------------
# Affichage des résultats pour le texte 1
# -------------------------------
print(f"Entropie des lettres dans texte1.txt premier texte : {entropy_texte1_premier_letters:.4f} bits")
print(f"Entropie des lettres dans texte1.txt deuxieme texte : {entropy_texte1_deuxieme_letters:.4f} bits")
print(f"Entropie des lettres dans texte1.txt troisieme texte : {entropy_texte1_troisieme_letters:.4f} bits\n")

# -------------------------------
# Affichage des résultats pour le texte 2
# -------------------------------
print(f"Entropie des lettres dans texte2.txt premier texte : {entropy_texte2_premier_letters:.4f} bits")
print(f"Entropie des lettres dans texte2.txt deuxieme texte : {entropy_texte2_deuxieme_letters:.4f} bits")
print(f"Entropie des mots dans texte2.txt premier texte : {entropy_texte2_premier_words:.4f} bits")
print(f"Entropie des mots dans texte2.txt deuxieme texte : {entropy_texte2_deuxieme_words:.4f} bits\n")

# -------------------------------
# Exemple d'analyse sur un texte long
# -------------------------------
long_text = """
Lorsque j’avais six ans j’ai vu, une fois, une magnifique image, dans un livre sur la Forêt Vierge qui s’appelait 
Histoires vécues. Ça représentait un serpent boa qui avalait un fauve. Voilà la copie du dessin. On disait dans 
le livre : « Les serpents boas avalent leur proie tout entière, sans la mâcher. Ensuite ils ne peuvent plus bouger 
et ils dorment pendant les six mois de leur digestion. » J’ai alors beaucoup réfléchi sur les aventures de la 
jungle et, à mon tour, j’ai réussi, avec un crayon de couleur, à tracer mon premier dessin. Mon dessin numéro 1. 
Il était comme ça :
"""

# Entropie du texte long
entropy_long_text_letters = process_text(long_text, "lettres")
entropy_long_text_words = process_text(long_text, "mots")

# Résultats du texte long
print(f"Entropie des lettres dans le texte long : {entropy_long_text_letters:.4f} bits")
print(f"Entropie des mots dans le texte long : {entropy_long_text_words:.4f} bits")
