# about back references using (\1)
# example 1
import re

randStr = "the cat cat fell out the window"
regex = re.compile(r"(\b\w+)\s+\1")
matches = re.findall(regex, randStr)
print("matches: ", len(matches))
for i in matches:
    print(i)


# example 2
rand_Str = "<a href='#'><b>The Link</b></a>"
regex = re.compile(r"<b>(.*?)</b>")
rand_Str = re.sub(regex, r"\1", rand_Str)
print(rand_Str)


# example 3
rand_Str = "412-555-1212"
regex = re.compile(r"([\d]{3})-([\d]{3}-[\d]{4})")
rand_Str = re.sub(regex, r"(\1)\2", rand_Str)
print(rand_Str)


# problem 1
random_str = "https://www.youtube.com http://www.google.com"
# <a href='https://www.youtube.com'>www.youtube.com</a>
# <a href='http://www.google.com'>www.google.com</a>

regex = re.compile(r"(https?://([\w.]+))")

random_str = re.sub(regex, r"<a href='\1'>\2</a>\n", random_str)

print(random_str)


# look ahead
random_str = "One Two Three four"

regex = re.compile(r"\w+(?=\b)")

matches = re.findall(regex, random_str)

for i in matches:
    print(i)


# look behind
# (?<=expression)
random_str = "1. Bread 2. Apples 3. lettuce"

regex = re.compile(r"(?<=\d.\s)\w+")

matches = re.findall(regex, random_str)

for i in matches:
    print(i)


# (?!expression) : Negative Look Ahead
# (?<!expression) : Negative Look Behind

randStr = "8 Apples $3, 1 Bread $1, 1 Cereal $4"
regex = re.compile(r"(?<!\$)\d+")
matches = re.findall(regex, randStr)
print(len(matches))
matches = [int(i) for i in matches]
from functools import reduce
print("Total Items {}".format(reduce((lambda x, y: x + y), matches)))
