class Sum:

    # this is a static method
    @staticmethod
    def get_sum(*args):

        sum = 0

        for i in args:
            sum += i

        return sum


def main():
    print("Sum: ", Sum.get_sum(1, 2, 3, 4, 5))


main()
