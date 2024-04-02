def caesar_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        # Check if character is an uppercase letter
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Character is not a letter, keep it as is
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        # Check if character is an uppercase letter
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Check if character is a lowercase letter
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Character is not a letter, keep it as is
            decrypted_text += char
    return decrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the plaintext
    encrypted_text = caesar_encrypt(plaintext, shift)
    print("Encrypted text:", encrypted_text)
    
    # Decrypt the ciphertext
    decrypted_text = caesar_decrypt(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
