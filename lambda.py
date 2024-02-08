# problem 1

sum = lambda x, y: x + y

print("sum:", sum(4, 5))

can_vote = lambda age: True if age >= 18 else False

print("can vote:", can_vote(20))


# problem 2
power_list = [lambda x: x ** 2,
            lambda x: x ** 3,
            lambda x: x ** 4]

for func in power_list:
    print(func(4))

# problem 3
attack = {'quick': (lambda: print("Quick attack")),
          'power': (lambda: print("Power attack")),
          'miss': (lambda: print("Missed attack"))}

attack['quick']()

import random

attack_key = random.choice(list(attack.keys()))

attack[attack_key]()


# problem 4
# create a random list filled with the characters H and T
# for heads and tails. output  the number of Hs and Ts
# example output
# Heads: 46
# Tails: 54


import random

flip_list = []

for i in range(1, 101):
    flip_list += random.choice(['H', 'T'])


print("Heads :", flip_list.count('H'))
print("Tails :", flip_list.count('T'))