def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    for number, letter in enumerate(plaintext):
        if keyword[number % len(keyword)].isupper():
            shift = ord(keyword[number % len(keyword)]) - ord("A")
        else:
            shift = ord(keyword[number % len(keyword)]) - ord("a")

        if not letter.isalpha():
            ciphertext += str(letter)
            continue

        if letter.isupper():
            ciphertext += str(chr(ord("A") + ((ord(letter) - ord("A") + shift) % 26)))
        else:
            ciphertext += str(chr(ord("a") + ((ord(letter) - ord("a") + shift) % 26)))
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for number, letter in enumerate(ciphertext):
        if keyword[number % len(keyword)].isupper():
            shift = ord(keyword[number % len(keyword)]) - ord("A")
        else:
            shift = ord(keyword[number % len(keyword)]) - ord("a")

        if not letter.isalpha():
            plaintext += str(letter)
            continue

        if letter.isupper():
            plaintext += str(chr(ord("A") + ((ord(letter) - (ord("A") - 26) - shift) % 26)))
        else:
            plaintext += str(chr(ord("a") + ((ord(letter) - (ord("a") - 26) - shift) % 26)))
    return plaintext
