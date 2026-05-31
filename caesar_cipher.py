def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Enter your message: ")
shift = int(input("Enter shift key (1-25): "))

encrypted = encrypt(text, shift)
decrypted = decrypt(encrypted, shift)

print("Original:  ", text)
print("Encrypted: ", encrypted)
print("Decrypted: ", decrypted)