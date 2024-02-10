def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True


def gen_primes(max_number):
    for num1 in range(2, max_number):

        if isprime(num1):
            yield num1


prime = gen_primes(50)

print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))
print("Prime: ", next(prime))


double = ( x * 2 for x in range(10))

print("Double: ", next(double))
print("Double :", next(double))

for num in double:
    print(num)