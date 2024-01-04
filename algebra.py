# solve for x
# x + 4 = 9

# x will always be the first value received, and you
# will deal with addition

# receive the string and split the string into variables
# convert the string into ints
# perform the operation
# convert the result into a string and join it to the string "X ="
# print()

def algebraic_equation(equation):
    x, operator, b, equal, c = equation.split()
    b = int(b)
    c = int(c)
    if operator == '+':
        result = c - b
    equation_result = "X = " + str(result)
    return equation_result


equation = input("Enter the algebraic equation: ")
result_string = algebraic_equation(equation)
print(result_string)
