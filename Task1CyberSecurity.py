def caesar_encrypt(message, shift):
    encrypted_text = ""
    for char in message:
        if char.isalpha():
            # Shift only alphabetical characters
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            
        elif char.isdigit():
            base=ord('0')
            shifted_char = chr((ord(char) - base + shift)%10 + base)
        encrypted_text += shifted_char
        
    return encrypted_text

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

def main():
    try:
        message = input("Enter the message to Encrypt or Decrypt: ")
        shift = int(input("Enter the shift value (positive integer): "))
        operation = input("Encrypt or decrypt? (E/D): ").lower()
        
        if operation == 'e':
            encrypted_message = caesar_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
            ext=input("Enter N to exit / Enter C to continue with Encryption and Decryption process:").lower()
            if ext=='n':
                quit()
            elif ext=='c':
                main()
        elif operation == 'd':
            decrypted_message = caesar_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
            ext=input("Enter N to exit / Enter C to continue with Encryption and Decryption process:").lower()
            if ext=='n':
                exit()
            elif ext=='c':
                main()
        else:
            print("Invalid operation. Please choose 'E' for encryption or 'D' for decryption.")
    except ValueError:
        print("Invalid input. Shift value must be a positive integer.")

if __name__ == "__main__":
    main()
