import re

randStr = "cat cats"

regex = re.compile("[cat]+s?")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


randStr = "doctor doctors doctor's"

regex = re.compile("[doctor]+['s]*")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


randStr = '''Just some words
and some more
and more
'''

regex = re.compile("[\w\s]+[\r]?\n")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)



randStr = "<name>Life on Mars</name><name>Freaks and Greaks</name>"

regex = re.compile("<name>(.*?)</name>")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


# defining boundaries for regular expressions
randStr = "ape at the apex"

regex = re.compile(r"\bape\b")

matches = re.findall(regex, randStr)

print(len(matches))

for i in matches:
    print(i)


# match beginning of a string using the ^ symbol

randStr = "match everything upto @"

regex = re.compile(r"^.*[^@]")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


# match the end of a string using the $ symbol
randStr = "@ get this string"

regex = re.compile(r"[^@\s].*$")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


# get the first word in each sentence

randStr = '''Ape is big
Turtle is slow
Cheetah is fast
'''

regex = re.compile(r"(?m)^.*?\s")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


# new problem
    randStr = "my number is 412-555-1212"

    regex = re.compile(r"412-(.*)")

    matches = re.findall(regex, randStr)

    for i in matches:
        print(i)


# new problem
randStr = "my number is 412-555-1212  412-555-1213  412-555-1214"

regex = re.compile(r"412-(.{8})")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)


# new problem
randStr = "my number is 412-555-1212"

regex = re.compile(r"412-(.*)-(.*)")

matches = re.findall(regex, randStr)

for i in matches:
    print(i)
