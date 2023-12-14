import string

class Alphabet:
    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = string.ascii_uppercase
        self.alphabet = {letter: index for index, letter in enumerate(alphabet)}

class Cipher(Alphabet):
    def monoalphabetic_cipher(self, plaintext, key):
        ciphertext = ''
        for letter in plaintext:
            if letter.upper() in self.alphabet:
                plaintext_index = self.alphabet[letter.upper()]
                ciphertext_index = (plaintext_index + key) % 26
                ciphertext += list(self.alphabet.keys())[list(self.alphabet.values()).index(ciphertext_index)]
            else:
                ciphertext += letter
        return ciphertext

    def autokey_cipher(self, plaintext, key):
        ciphertext = ''
        subkey = key
        for letter in plaintext:
            if letter.upper() in self.alphabet:
                plaintext_index = self.alphabet[letter.upper()]
                ciphertext_index = (plaintext_index + subkey) % 26
                ciphertext += list(self.alphabet.keys())[list(self.alphabet.values()).index(ciphertext_index)]
                subkey = plaintext_index
            else:
                ciphertext += letter
        return ciphertext

    def vigenere_cipher(self, plaintext, key):
        ciphertext = ''
        key_list = [int(k) for k in key.split(',')]
        key_stream = ''
        for i in range(len(plaintext)):
            key_index = i % len(key_list)
            key_stream += list(self.alphabet.keys())[list(self.alphabet.values()).index(key_list[key_index])]
        for i in range(len(plaintext)):
            if plaintext[i].upper() in self.alphabet:
                plaintext_index = self.alphabet[plaintext[i].upper()]
                key_index = self.alphabet[key_stream[i].upper()]
                ciphertext_index = (plaintext_index + key_index) % 26
                ciphertext += list(self.alphabet.keys())[list(self.alphabet.values()).index(ciphertext_index)]
            else:
                ciphertext += plaintext[i]
        return ciphertext

class Decipher(Alphabet):
    def monoalphabetic_decipher(self, ciphertext, key):
        plaintext = ''
        for letter in ciphertext:
            if letter.upper() in self.alphabet:
                ciphertext_index = self.alphabet[letter.upper()]
                plaintext_index = (ciphertext_index - key) % 26
                plaintext += list(self.alphabet.keys())[list(self.alphabet.values()).index(plaintext_index)]
            else:
                plaintext += letter
        return plaintext

    def autokey_decipher(self, ciphertext, key):
        plaintext = ''
        subkey = key
        for letter in ciphertext:
            if letter.upper() in self.alphabet:
                ciphertext_index = self.alphabet[letter.upper()]
                plaintext_index = (ciphertext_index - subkey) % 26
                plaintext += list(self.alphabet.keys())[list(self.alphabet.values()).index(plaintext_index)]
                subkey = plaintext_index
            else:
                plaintext += letter
        return plaintext

    def vigenere_decipher(self, ciphertext, key):
        plaintext = ''
        key_list = [int(k) for k in key.split(',')]
        key_stream = ''
        for i in range(len(ciphertext)):
            key_index = i % len(key_list)
            key_stream += list(self.alphabet.keys())[list(self.alphabet.values()).index(key_list[key_index])]
        for i in range(len(ciphertext)):
            if ciphertext[i].upper() in self.alphabet:
                ciphertext_index = self.alphabet[ciphertext[i].upper()]
                key_index = self.alphabet[key_stream[i].upper()]
                plaintext_index = (ciphertext_index - key_index) % 26
                plaintext += list(self.alphabet.keys())[list(self.alphabet.values()).index(plaintext_index)]
            else:
                plaintext += ciphertext[i]
        return plaintext