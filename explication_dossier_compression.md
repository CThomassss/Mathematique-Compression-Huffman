# Dossier Compression — Explication des fichiers

## 1. huffman.py

Ce fichier implémente l’algorithme de compression de Huffman.  
Il permet :
- De calculer la fréquence des caractères dans un texte.
- De construire l’arbre de Huffman à partir des fréquences.
- De générer les codes binaires pour chaque caractère.
- D’encoder un texte en utilisant ces codes.
- De décoder un texte compressé pour vérifier la fiabilité de la compression.
- D’afficher le taux de compression obtenu sur des exemples (texte aléatoire et texte long).

**Utilité :**  
Ce script montre comment la compression Huffman permet de réduire la taille d’un texte tout en garantissant la possibilité de le retrouver à l’identique après décodage.

---

## 2. entropie.py

Ce fichier calcule l’entropie d’un texte, c’est-à-dire la quantité moyenne d’information par symbole (lettre ou mot).  
Il :
- Charge plusieurs fichiers texte (texte1 et texte2).
- Calcule l’entropie pour chaque texte, en considérant les lettres ou les mots comme symboles.
- Affiche les résultats pour comparer la richesse informationnelle des différents textes.

**Utilité :**  
L’entropie permet d’évaluer la complexité ou la diversité d’un texte. Plus l’entropie est élevée, plus le texte est varié et difficile à compresser.

---

## 3. test.py

Ce fichier propose une autre implémentation de l’algorithme de Huffman, avec des noms de variables en français.  
Il :
- Calcule la fréquence des caractères d’un texte exemple.
- Construit l’arbre de Huffman.
- Génère les codes pour chaque caractère.
- Encode et décode le texte pour vérifier la validité de la compression.

**Utilité :**  
Ce script sert à illustrer le fonctionnement de Huffman sur un texte plus long et à montrer que l’algorithme fonctionne quel que soit le texte utilisé.

---

## 4. texte1_deuxieme-text.txt (et autres fichiers texte)

Ces fichiers contiennent les textes utilisés pour les calculs d’entropie et de compression.  
Ils servent de données d’entrée pour les scripts Python.

**Utilité :**  
Ils permettent de tester les algorithmes sur des exemples concrets et de comparer les résultats obtenus.

---

# Conclusion

Ce dossier montre comment :
- Calculer l’entropie d’un texte (entropie.py).
- Compresser et décompresser un texte avec Huffman (huffman.py, test.py).
- Utiliser des textes réels pour tester et illustrer les concepts de compression et d’information.

Chaque fichier a un rôle précis :  
- Les scripts Python réalisent les calculs et manipulations.
- Les fichiers texte servent de base de données pour les tests.

Pour toute question, il suffit de se référer à ce document pour comprendre la fonction de chaque fichier.
