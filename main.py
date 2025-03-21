import time

# Create function to encrypt and decrypt message
def reverse_message(message):
        reversed_message = ""
        for letter in message:
            if letter in cipher:
                reversed_message += cipher[letter]
            else:
                reversed_message += letter
        return reversed_message
# Greet user and explain what an enigma machine is and what cipher its using
print("Welcome to the Enigma Machine!")
time.sleep(1)
print("The Enigma Machine was a cipher machine used by the Germans during World War II.")
time.sleep(1)
print("This program uses the Atbash Cipher to encrypt and decrypt messages.")
time.sleep(1)
# Create a dictionary with the alphabet and its corresponding number
cipher = {"a": "z", "b": "y", "c": "x", "d": "w", "e": "v", "f": "u", "g": "t", "h": "s", "i": "r", "j": "q", "k": "p", "l": "o", "m": "n", "n": "m", "o": "l", "p": "k", "q": "j", "r": "i", "s": "h", "t": "g", "u": "f", "v": "e", "w": "d", "x": "c", "y": "b", "z": "a", "1": "0", "2": "9", "3": "8", "4": "7", "5": "6", "6": "5", "7": "4", "8": "3", "9": "2", "0": "1", "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V", "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q", "K": "P", "L": "O", "M": "N", "N": "M", "O": "L", "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G", "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B",}
# Ask user if they want to encrypt, decrypt, or quit
while True:
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
        reversed_message = reverse_message(message)
        time.sleep(2)
        print("Encrypted message:", reversed_message)

    # If they want to decrypt, ask for a message 
    elif choice == "d":
        message = input("What message would you like to encrypt? ")
        print("Encrypting message...")
        time.sleep(2)
        print("this could take days.......")
        time.sleep(2)
        print("im kidding.......")
    # Call the encrypt_message function and print the result
        reversed_message = reverse_message(message)
        time.sleep(2)
        print("Encrypted message:", reversed_message)

    # If they want to quit, say goodbye
    elif choice == "q":
        print("Goodbye!")
        break
    # If they enter an invalid choice, let them know
    else:
        print("Invalid choice. Please try again.")