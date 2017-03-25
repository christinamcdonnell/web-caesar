#from helpers import alphabet_position, rotate_character

def alphabet_position(letter):
    # input to this function is a string of one letter (apha character)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    low_letter = letter.lower() # assign lower case version of letter to low_letter
    # print("LOOK!!! letter.lower() yields =>", letter.lower())
    # returns the 0 based position of letter within alphabet
    position_in_alphabet = alphabet.find(low_letter)
    return position_in_alphabet

def rotate_character(char, rot):
    #input is a char of len one and an integer rotation, preserve upper/lower case    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not char.isalpha(): # or code as == False
        #print("This char is NOT alpha")
        newchar = char
    else: # It is aphabetic so find the rotated letter
        position = alphabet_position(char)
        #print("FOUND IT: position =", position)
        position += rot
        if position < 26:
            newchar = alphabet[position]######  mod 26 goes THIS !!!!!!!!
        else:
            newchar = alphabet[position % 26]

        #print("BEFORE CAP CHECK: char =", char, "newchar =", newchar)
        if char.isupper():
            #print("BRING BACK THE CAPS ")
            newchar = newchar.upper()
            #print("DONE")
        # print("AFTER CAP CHECK: char =", char, "newchar =", newchar)
    return newchar

def encrypt(text, rot):
    # text is a string to be encrypted, rot is the integer rotation amount
    encrypted_text = ''
    for char in text:
        rotatedChar = rotate_character(char, rot)
        encrypted_text = encrypted_text + rotatedChar
    return encrypted_text
