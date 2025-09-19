import heapq  # Pour utiliser une file de priorité
import random  # Pour générer du texte aléatoire
from collections import defaultdict

# Fonction pour calculer les fréquences
def calculate_frequencies(text):
    frequencies = defaultdict(int)
    for char in text:
        frequencies[char] += 1
    return frequencies

# Classe représentant un nœud de Huffman
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

# Fonction pour construire l'arbre de Huffman
def build_huffman_tree(frequencies):
    heap = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

# Fonction pour générer les codes de Huffman
def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}
    if root is None:
        return codes

    if root.char is not None:
        codes[root.char] = current_code
    generate_huffman_codes(root.left, current_code + "0", codes)
    generate_huffman_codes(root.right, current_code + "1", codes)
    
    return codes

# Fonction pour encoder un texte
def huffman_encode(text, codes):
    return ''.join(codes[char] for char in text)

# Fonction pour décoder un texte encodé
def huffman_decode(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        current_node = current_node.left if bit == "0" else current_node.right
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root
    return ''.join(decoded_text)

# Générer un texte aléatoire de longueur donnée avec des fréquences spécifiques
def generate_random_text(length, frequencies):
    letters = list(frequencies.keys())
    probabilities = list(frequencies.values())
    return ''.join(random.choices(letters, probabilities, k=length))

def main():
    # Question 1 : Texte aléatoire avec 3 lettres A, B, C et différentes fréquences
    frequencies_ABC = {'A': 0.5, 'B': 0.3, 'C': 0.2}
    random_text = generate_random_text(10000, frequencies_ABC)
    random_frequencies = calculate_frequencies(random_text)
    random_tree = build_huffman_tree(random_frequencies)
    random_codes = generate_huffman_codes(random_tree)
    encoded_random_text = huffman_encode(random_text, random_codes)
    decoded_random_text = huffman_decode(encoded_random_text, random_tree)

    print("\n--- Résultats pour le texte aléatoire ---")
    print(f"Texte original : {len(random_text)} caractères")
    print(f"Texte encodé : {len(encoded_random_text)} bits")
    print(f"Taux de compression : {len(encoded_random_text) / (len(random_text) * 8):.2f}")
    assert random_text == decoded_random_text, "Erreur dans le décodage du texte aléatoire."

    # Question 2 : Texte long trouvé à l'initiative
    long_text = """
    Il était une fois, dans un petit village, un jeune garçon nommé Pierre. Pierre avait un rêve: voyager à travers le monde et découvrir de nouvelles cultures. Chaque jour, il se tenait devant la fenêtre de sa maison, regardant les nuages passer, imaginant les aventures qui l'attendaient.

    Un jour, Pierre a décidé qu'il était temps de réaliser son rêve. Il a pris son sac à dos, a dit au revoir à sa famille et a commencé son voyage. Ses aventures l'ont conduit à des montagnes majestueuses, des forêts denses et des rivières scintillantes.

    Il a rencontré des gens fascinants, goûté des plats exotiques et appris des langues différentes. Chaque nouvelle expérience enrichissait son cœur et son esprit. Au fil du temps, Pierre est devenu un conteur, partageant ses histoires avec d'autres voyageurs.

    À son retour au village, Pierre a compris que le vrai voyage ne réside pas seulement dans les destinations, mais aussi dans les souvenirs et les leçons que l'on tire en chemin.
    """

    long_frequencies = calculate_frequencies(long_text)
    long_tree = build_huffman_tree(long_frequencies)
    long_codes = generate_huffman_codes(long_tree)
    encoded_long_text = huffman_encode(long_text, long_codes)
    decoded_long_text = huffman_decode(encoded_long_text, long_tree)

    print("\n--- Résultats pour le texte long ---")
    print(f"Texte original : {len(long_text)} caractères")
    print(f"Texte encodé : {len(encoded_long_text)} bits")
    print(f"Taux de compression : {len(encoded_long_text) / (len(long_text) * 8):.2f}")
    assert long_text == decoded_long_text, "Erreur dans le décodage du texte long."

    print("\nTous les tests sont passés avec succès !")

if __name__ == "__main__":
    main()
