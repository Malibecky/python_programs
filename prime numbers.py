def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_prime(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes


max_number_to_check = int(input("check prime numbers up to: "))
result = get_prime(max_number_to_check)


for i in result:
    print(i)
