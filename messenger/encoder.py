import string
import random

def generate_random_key(length):
    characters = string.printable[:-6] 
    return ''.join(random.choice(characters) for _ in range(length))

def encrypt(key, string):
    encoded = ''
    for i in range(len(string)):
        key_c = ord(key[i % len(key)])
        string_c = ord(string[i % len(string)])
        encoded += chr((key_c + string_c) % 127)
    return encoded

def decrypt(key, encoded):
    decoded = ''
    for i in range(len(encoded)):
        key_c = ord(key[i % len(key)])
        encoded_c = ord(encoded[i])
        decoded += chr((encoded_c - key_c + 127) % 127)
    return decoded