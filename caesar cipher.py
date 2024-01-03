# A-Z 65-90
# a-z 97-122
# ord(your_letter)
# char(your_code)

# Hints
# use isupper() to decide which unicodes to work with
# add the key (number of characters to shift) and if
# the key is bigger or smaller than the unicode for
# A, Z, a, z increase or decrease by 26

# receive the message to encrypt and
# characters to shift
original_message = input("enter the message to encrypt: ")
key = int(input('How many characters to shift(1-26): '))
# prepare the secret_message
secret_message = ""
# cycle through each character in the message
# cycle through each character in the message
for char in original_message:
    # if it isn't a letter then keep it as it is
    if char.isalpha():
        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
        # if uppercase then compare to uppercase unicodes
        if char.isupper():
            # if bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # if smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        # Do the same for lowercase
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        secret_message += chr(char_code)
    else:
        # if not a letter leave character as is
        secret_message += char

print("Encrypted:", secret_message)
# if not a letter leave character as is

# To decrypt the only thing that changes is the sign of the key
original_message = ""
key = -key

for char in secret_message:
    # if it isn't a letter then keep it as it is
    if char.isalpha():
        # Get the character code and add the shift amount
        char_code = ord(char)
        char_code += key
        # if uppercase then compare to uppercase unicodes
        if char.isupper():
            # if bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            # if smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        # Do the same for lowercase
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        # Convert from code to letter and add to message
        original_message += chr(char_code)
    else:
        # if not a letter leave character as is
        original_message += char

print("Decrypted:", original_message)
# The same as above
