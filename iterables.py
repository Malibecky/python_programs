simple_str = iter("Sample")

print("char: ", next(simple_str))
print("Char: ", next(simple_str))
print("Char: ", next(simple_str))
print("Char: ", next(simple_str))
print("Char: ", next(simple_str))
print("Char: ", next(simple_str))


class Alphabet:

    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.letters) -1:
            raise StopIteration
        self.index += 1
        return self.letters[self.index]


alpha = Alphabet()

for letter in alpha:
    print(letter)


class Fib_Generator:

    def __init__(self):
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib_Num = self.first + self.second
        self.first = self.second
        self.second = fib_Num
        return  fib_Num


fibSeq = Fib_Generator()

for i in range(10):
    print("FIb: ", next(fibSeq))
