one_To_10 = range(1, 11)


def dbl_num(num):
    return num * 2


print(list(map(dbl_num, one_To_10)))

print(list(map((lambda x: x * 3), one_To_10)))

alist = list(map((lambda x, y: x + y), [1, 2, 3], [1, 2, 3]))
print(alist)


# problem
multiples_of_9 = random.choice(1, 1000)


def multiples_9(num):
    return num * 9


print(list(map(multiples_9, multiples_of_9)))
