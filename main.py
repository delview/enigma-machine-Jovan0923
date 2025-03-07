# Greet user and explain what an enigma machine is and what cipher its using
print("Welcome to the Enigma Machine!")
print("The Enigma Machine was a cipher machine used by the Germans during World War II.")
print("This program uses the Atbash Cipher to encrypt and decrypt messages.")
# Create a dictionary with the alphabet and its corresponding number
sipher = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a"}
# Ask user if they want to encrypt, decrypt, or quit
choice = input("Would you like to [e]ncrypt, [d]ecrypt, or [q]uit? ")
# If they want to encrypt, ask for a message
if choice == "e":
    message = input("What message would you like to encrypt? ")
    print("Encrypting message... this could take days....... im kidding")
# Create function to encrypt message
def encrypt_message(message):
        encrypted_message = ""
        for letter in message:
            if letter in sipher:
                encrypted_message += sipher[letter]
            else:
                encrypted_message += letter
        return encrypted_message
# Call the encrypt_message function and print the result
encrypted_message = encrypt_message(message)
print("Encrypted message:", encrypted_message)
# If they want to decrypt, ask for a message 

# Create function to decrypt message

# If they want to quit, say goodbye