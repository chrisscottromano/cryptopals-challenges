import nltk
nltk.download('words')
from nltk.metrics.distance import edit_distance

# Load NLTK resources for language detection
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def xor_single_byte(ciphertext, key):
    """
    XOR a ciphertext with a single byte key.
    """
    plaintext = b''
    for byte in ciphertext:
        plaintext += bytes([byte ^ key])
    return plaintext


def score_plaintext(plaintext):
    """
    Score a plaintext based on character frequency.
    """
    # Define character frequencies for English language
    char_freq = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253,
        'e': 0.12702, 'f': 0.02228, 'g': 0.02015, 'h': 0.06094,
        'i': 0.06966, 'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
        'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 'p': 0.01929,
        'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
        'y': 0.01974, 'z': 0.00074, ' ': 0.13000
    }
    score = 0
    for char in plaintext:
        char = chr(char).lower()
        if char in char_freq:
            score += char_freq[char]
    return score


def brute_force_decrypt(ciphertext):
    """
    Decrypt a ciphertext using brute force.
    """
    results = []
    for key in range(256):
        plaintext = xor_single_byte(ciphertext, key)
        score = score_plaintext(plaintext)
        results.append((plaintext, score, key))
    # Sort results by score in descending order
    results.sort(key=lambda x: x[1], reverse=True)
    return results[:10]  # Return only the top 10 results


# Function to calculate English similarity score
def english_similarity_score(text):
    """
    Calculate an English similarity score for a given text.
    """
    english_words = set(nltk.corpus.words.words())
    tokens = nltk.word_tokenize(text)
    english_tokens = [token for token in tokens if token.isalpha() and token.lower() in english_words]
    english_score = len(english_tokens) / len(tokens)
    return english_score

# Function to perform stricter English similarity test
def strict_english_similarity_test(plaintext):
    """
    Perform a stricter English similarity test on a given plaintext.
    """
    return english_similarity_score(plaintext) > 0.1

# Perform brute force decryption and write results to output file
with open('4-ciphertext.txt', 'r') as file:
    ciphertexts = file.readlines()

with open('4-results.txt', 'w') as output_file:
    all_results = []
    for i, ciphertext in enumerate(ciphertexts):
        ciphertext = bytes.fromhex(ciphertext.strip())
        results = brute_force_decrypt(ciphertext)
        output_file.write(f"Results for Ciphertext {i + 1}:\n")
        for j, (plaintext, score, key) in enumerate(results[:10], start=1):
            if strict_english_similarity_test(plaintext.decode('utf-8', errors='replace')):
                all_results.append((i + 1, plaintext, score, key))
                output_file.write(f"  {j}. Plaintext: {plaintext.decode('utf-8', errors='replace')} | Score: {score:.2f} | Key: {key}\n")
        output_file.write("\n")

    # Sort and print top 50 results from all ciphertexts
    output_file.write(f"Top 50 Results from All Ciphertexts:\n")
    all_results.sort(key=lambda x: x[2], reverse=True)
    for k, (ciphertext_num, plaintext, score, key) in enumerate(all_results[:50], start=1):
        output_file.write(f"  {k}. Ciphertext {ciphertext_num}: Plaintext: {plaintext.decode('utf-8', errors='replace')} | Score: {score:.2f} | Key: {key}\n")
