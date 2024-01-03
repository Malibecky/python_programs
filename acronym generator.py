# ask for a string
rand_string = input('enter a string: ')
# convert the string to uppercase
rand_string = rand_string.upper()
# convert the string to a list
a_list = rand_string.split()
# cycle through the list
for i in a_list:
    # Get the first letter of the word and eliminate the new line
    print(i[0], end='')
# add a new line
print()
