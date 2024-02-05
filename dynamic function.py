def multiply_by_2(num):
    return num * 2


times_two = multiply_by_2

print("4 * 2 = ", multiply_by_2(4))


def do_math(func, num):
    return func(num)


print("8 * 2=", do_math(multiply_by_2, 8))


def get_func_mult_by_num(num):

    def mult_by(value):
        return num * value

    return mult_by


generate_func = get_func_mult_by_num(5)

print("5 * 10=", generate_func(10))

lists_of_functions = [times_two, generate_func]
print("5 * 9=", lists_of_functions[1](9))
