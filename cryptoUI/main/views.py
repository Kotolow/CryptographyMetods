from django.shortcuts import render
from .cryptography import Cipher, Decipher

def home(request):
    if request.method == 'POST':
        method = request.POST.get('method')
        text = request.POST.get('text')
        key = request.POST.get('key')
        if method == 'monoalphabetic_cipher':
            cipher = Cipher()
            ciphertext = cipher.monoalphabetic_cipher(text, int(key))
            return render(request, 'home.html', {'ciphertext': ciphertext})
        elif method == 'monoalphabetic_decipher':
            decipher = Decipher()
            plaintext = decipher.monoalphabetic_decipher(text, int(key))
            return render(request, 'home.html', {'plaintext': plaintext})
        elif method == 'autokey_cipher':
            cipher = Cipher()
            ciphertext = cipher.autokey_cipher(text, int(key))
            return render(request, 'home.html', {'ciphertext': ciphertext})
        elif method == 'autokey_decipher':
            decipher = Decipher()
            plaintext = decipher.autokey_decipher(text, int(key))
            return render(request, 'home.html', {'plaintext': plaintext})
        elif method == 'vigenere_cipher':
            cipher = Cipher()
            ciphertext = cipher.vigenere_cipher(text, key)
            return render(request, 'home.html', {'ciphertext': ciphertext})
        elif method == 'vigenere_decipher':
            decipher = Decipher()
            plaintext = decipher.vigenere_decipher(text, key)
            return render(request, 'home.html', {'plaintext': plaintext})
    return render(request, 'home.html')