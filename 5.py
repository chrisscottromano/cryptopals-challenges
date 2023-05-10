import base64

plaintext = b"Burning 'em, if you ain't quick and nimble\n I go crazy when I hear a cymbal"
key = b'ICE'

def xor_repeating_key(plaintext, key):
    """
    Encrypts the given plaintext using repeating-key XOR with the given key.
    """
    ciphertext = b''
    for i, c in enumerate(plaintext):
        ciphertext += bytes([c ^ key[i % len(key)]])
    return ciphertext

def write_ciphertext_to_file(ciphertext):
    """
    Writes the given ciphertext to a file.
    """
    with open('ciphertext5.txt', 'wb') as file:
        file.write(ciphertext)

ciphertext = xor_repeating_key(plaintext, key)
write_ciphertext_to_file(ciphertext)
