import time
# Greet user and explain what an enigma machine is and what cipher its using
# Create function to encrypt message
def encrypt_message(message):
        encrypted_message = ""
        for letter in message:
            if letter in cipher:
                encrypted_message += cipher[letter]
            else:
                encrypted_message += letter
        return encrypted_message

# Create function to decrypt message
def decrypt_message(message):
    decrypted_message = ""    
    for letter in message:
        if letter in cipher:
            decrypted_message += cipher[letter]
        else:
            decrypted_message += letter
    return decrypted_message
print("Welcome to the Enigma Machine!")
time.sleep(1)
print("The Enigma Machine was a cipher machine used by the Germans during World War II.")
time.sleep(1)
print("This program uses the Atbash Cipher to encrypt and decrypt messages.")
time.sleep(1)
# Create a dictionary with the alphabet and its corresponding number
cipher = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}
# Ask user if they want to encrypt, decrypt, or quit
choice = input("Would you like to [e]ncrypt, [d]ecrypt, or [q]uit? ")
# If they want to encrypt, ask for a message
if choice == "e":
    message = input("What message would you like to encrypt? ")
    print("Encrypting message...")
    time.sleep(2)
    print("this could take days.......")
    time.sleep(2)
    print("im kidding.......")
# Call the encrypt_message function and print the result
    encrypted_message = encrypt_message(message)
    time.sleep(2)
    print("Encrypted message:", encrypted_message)

# If they want to decrypt, ask for a message 
elif choice == "d":
    message = input("What message would you like to decrypt? ")
    print("Decrypting message...")
    time.sleep(2)
    print("this could take days.......")
    time.sleep(2)
    print("im kidding.......")
    
    # Call the decrypt_message function and print the result
    decrypted_message = decrypt_message(message)
    time.sleep(2)
    print("Decrypted message:", decrypted_message)

# If they want to quit, say goodbye
elif choice == "q":
    print("Goodbye!")
else:
    print("Invalid choice. Please try again.")