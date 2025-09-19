# Rapport — Dossier Compression

## Introduction

Ce dossier présente l’étude de la compression de données textuelles à travers le calcul d’entropie et l’implémentation du codage de Huffman. Les travaux réalisés respectent les consignes du sujet, qui demandent d’approfondir les notions de compression et d’information, de calculer l’entropie sur différents textes, et d’implémenter/tester le codage de Huffman.

---

## 1. Calcul de l’entropie des textes

**Fichier : `entropie.py`**

- Ce script charge plusieurs fichiers texte (`texte1_premier-text.txt`, `texte1_deuxieme-text.txt`, `texte1_troisieme-texte.txt`, `texte2_premier-texte.txt`, `texte2_deuxieme-texte.txt`).
- Il calcule l’entropie pour chaque texte :
  - En considérant chaque lettre (y compris les espaces) comme un symbole.
  - En considérant chaque mot comme un symbole (pour texte2).
- Il applique aussi le calcul sur un texte long trouvé à mon initiative (extrait du Petit Prince), pour les lettres et les mots.

**Objectif atteint :**  
- Calcul de l’entropie sur plusieurs textes, pour les lettres et les mots, comme demandé.

---

## 2. Codage de Huffman

**Fichiers : `huffman.py`, `test.py`**

- Ces scripts implémentent l’algorithme de Huffman :
  - Calcul des fréquences d’apparition des lettres dans un texte.
  - Construction de l’arbre de Huffman.
  - Génération des codes binaires pour chaque lettre.
  - Encodage et décodage du texte pour vérifier la fiabilité de la compression.

**Objectif atteint :**  
- Codage de Huffman pour un texte de n lettres, chaque lettre ayant une fréquence pi.

---

## 3. Application sur texte aléatoire (n=3 lettres, longueur=10000)

**Fichier : `huffman.py`**

- Génération d’un texte aléatoire de 10 000 caractères avec 3 lettres (A, B, C) et des fréquences différentes.
- Application du codage Huffman et vérification du décodage.
- Affichage du taux de compression obtenu.

**Exemple de résultat :**
```
--- Résultats pour le texte aléatoire ---
Texte original : 10000 caractères
Texte encodé : 14981 bits
Taux de compression : 0.19
```

**Objectif atteint :**  
- Test du codage Huffman sur un texte aléatoire avec différentes fréquences.

---

## 4. Application sur textes longs trouvés à mon initiative

**Fichiers : `huffman.py`, `test.py`**

- Utilisation de textes longs (extrait du Petit Prince, texte de film, etc.).
- Application du codage Huffman et vérification du décodage.
- Affichage du taux de compression.

**Exemple de résultat :**
```
--- Résultats pour le texte long ---
Texte original : 998 caractères
Texte encodé : 4284 bits
Taux de compression : 0.54
```

**Objectif atteint :**  
- Test du codage Huffman sur des textes réels et suffisamment longs.

---

## 5. Explication des fichiers

- **entropie.py** : Calcule l’entropie des textes (lettres et mots).
- **huffman.py** : Implémente et teste le codage Huffman sur textes aléatoires et réels.
- **test.py** : Variante de Huffman sur un autre texte long.
- **Fichiers texte** : Données d’entrée pour les calculs et tests.

---

## 6. Conclusion

L’ensemble des fichiers et scripts respecte le travail demandé :
- Calculs d’entropie sur différents textes et symboles.
- Implémentation et test du codage Huffman sur textes aléatoires et réels.
- Vérification de la fiabilité du décodage et mesure du taux de compression.

Ce rapport synthétise la démarche et les résultats obtenus, et peut être présenté au professeur pour justifier le travail réalisé.

---

## Annexes

- Résultats d’exécution (taux de compression, valeurs d’entropie).
- Explications détaillées des algorithmes utilisés.
