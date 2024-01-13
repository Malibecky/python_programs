def fibonacci(num):

    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        result = fibonacci(num - 1) + fibonacci(num - 2)
        return result


values = int(input("how many values: "))
for i in range(values):
    print(fibonacci(i))

print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
