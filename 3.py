import string
import re

def score_plaintext(plaintext):
    """
    Returns a score for the given plaintext based on the frequency of
    characters in the English language.
    """
    # Define the frequency of letters in the English language
    freq = {'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702, 
            'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153, 
            'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507, 
            'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056, 
            'u': 0.02758, 'v': 0.00978, 'w': 0.0236, 'x': 0.0015, 'y': 0.01974, 'z': 0.00074}
    
    # Count the frequency of each letter in the plaintext
    freq_plaintext = {}
    for c in plaintext.lower():
        if c in freq:
            freq_plaintext[c] = freq_plaintext.get(c, 0) + 1
    
    # Calculate the score based on the difference between the expected and actual frequencies
    score = 0
    for c in freq:
        if c in freq_plaintext:
            score += abs(freq[c] - (freq_plaintext[c] / len(plaintext)))
        else:
            score += freq[c]
    
    return score

def xor_single_byte(hex_string):
    """
    Decrypts a hex-encoded string that has been XOR'd against a single character.
    Returns a list of all possible plaintexts ranked by their score.
    """
    ciphertext = bytes.fromhex(hex_string)
    results = []
    for key in range(256):
        plaintext = ''.join([chr(b ^ key) for b in ciphertext])
        score = score_plaintext(plaintext)
        results.append((plaintext, score, chr(key)))
    return sorted(results, key=lambda x: x[1])

# Example usage
hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
results = xor_single_byte(hex_string)
with open('3-results.txt', 'w') as file:
    for plaintext, score, key in results:
        plaintext = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', plaintext)
        file.write(f"Plaintext: {plaintext.strip()} | Score: {score:.2f} | Key: {key}\n")
