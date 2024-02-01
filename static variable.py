class Dog:

    # this is a static variable
    num_of_dogs = 0

    def __init__(self, name="unknown"):
        self.name = name

        # reference the static variable by proceeding it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def get_num_of_dogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():

    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.get_num_of_dogs()
    doug.get_num_of_dogs()


main()
