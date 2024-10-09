def encrypt_string(main_string, symbol):
    encrypted_string = ""
    for char in main_string:
        encrypted_string += char + symbol
    return encrypted_string

def decrypt_string(encrypted_string, symbol):
    # Split the string by the symbol and filter out empty strings
    decrypted_string = ''.join(part for part in encrypted_string.split(symbol) if part)
    return decrypted_string

# Input from the user
main_string = input("Enter the main string: ")
symbol = input("Enter the symbol to embed: ")

# Encrypt the string
encrypted = encrypt_string(main_string, symbol)
print(f"Encrypted string: {encrypted}")

# Decrypt the string
decrypted = decrypt_string(encrypted, symbol)
print(f"Decrypted string: {decrypted}")
