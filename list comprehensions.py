print(list(map((lambda x: x * 2), range(1, 11))))

# list comprehension
print([2 * x for x in range(1, 11)])

print(list(filter((lambda x: x % 2 != 0), range(1, 11))))

# list comprehension
print([x for x in range(1, 11) if x % 2 != 0])


# Generate 50 values
# Take to the power of 2
# return multiples of 8

print([i ** 2 for i in range(50) if i % 8 == 0])

print([x * y for x in range(1, 3) for y in range(11, 16)])


# Generate a list of 10 values
# multiply by 2
# return multiples of 8

print([i * 2 for i in range(10) if i * 2 % 8 == 0])


# problem
# generate a list of 50 random values between 1 and 1000
# and return those that are multiples of 9
# you'll have to use a list comprehension in a list comprehension


import random

print([i for i in [random.randint(1, 1001) for i in range(50)] if i % 9 == 0])


multilist = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

print([col[1] for col in multilist])
print([multilist[i][i] for i in range(len(multilist))])
