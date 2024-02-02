num1, num2 = input("enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("you can't divide by zero")
else:
    print("you didn't raise an exception")
finally:
    print("I execute no matter what")
