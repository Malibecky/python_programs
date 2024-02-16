import re

the_strg = "The ape was at the apex"

for i in re.finditer("ape.", the_strg):
    loc_Tuple = i.span()
    print(loc_Tuple)
    print(the_strg[loc_Tuple[0]: loc_Tuple[1]])


# problem 2
the_string = "Cat mat rat pat"

for i in re.findall("[Cmpr]at", the_string):
    print(i)

# find all strings starting with letters in the range c-m or C-M
for i in re.findall("[c-mC-M]at", the_string):
    print(i)

# find all strings that don't start with C or r
for i in re.findall("[^Cr]at", the_string):
    print(i)

# problem 3: replace strings
the_string = "Cat mat rat pat"

regex = re.compile("[Cm]at")
new_string = regex.sub("owl", the_string)
print(new_string)

# problem 4: solving backslash problems
randStr = "here is \\stuff"
# put an 'r' or double the number of backslashes
print("find \\stuff: ", re.search(r"\\stuff", randStr))

# problem 5: finding a period
random_string = "F.B.A.  I.R.S.  CIA"
print("matches: ", len(re.findall(".\..\..\.", random_string)))

# problem 6: finding matches for whitespace
rand_string = '''This is a long
string that goes
on for many lines
'''
print(rand_string)

regex = re.compile("\n")
rand_string = regex.sub(" ", rand_string)
print(rand_string)

# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab


# problem 7: matching numbers
# \d : [0-9]
# \D : [^0-9]

string_1 = "12345"
print("matches: ", len(re.findall("\d", string_1)))
print("matches: ", len(re.findall("\d{5}", string_1)))
print("matches: ", len(re.findall("\d{2}", string_1)))

# problem 8: matching characters
# \w : [a-zA-Z0-9]
# \W : [^ a-zA-Z0-9]

Phone_Num = "412-555-1212"

if re.search("\w{3}-\w{3}-\w{4}", Phone_Num):
    print("it is a phone number")


# \s :[\f\n\r\t\v]
# \S :[^\f\n\r\t\v]
if re.search("\w{2,20}\s\w{2,20}", "Toshio Muramatsu"):
    print("it is valid")

# (+) means followed by
print("matches: ", len(re.findall("a+", "a as ape bug")))


# Question problem

# 1. 1 to 20 lowercase uppercase letters, numbers, plus ._%+-
# 2. An @symbol
# 3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
# 4. A period
# 5. 2 to 3 lowercase and uppercase letters

email_list = "beckymali330@gmail.com, marthamatuu@yahoo.com, marthamatuu90@yahoo.com"
print("Email matches: ", len(re.findall("[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email_list)))
