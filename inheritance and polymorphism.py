# when we create a class we can inherit all  the fields and methods from another class
# this is called inheritance
# the class that inherits is called the subclass and the class we inherit from is the super class

# this will be our superclass
class Animal:
    def __init__(self, birthtype="unkown", appearance="unkown", blooded="unknown"):
        self.__birthtype = birthtype
        self.__appearance = appearance
        self.__blooded = blooded

    # The getter method
    @property
    def birthtype(self):
        # when using getters and setters don't forget the __
        return self.__birthtype

    @birthtype.setter
    def birthtype(self, birthtype):
        self.__birthtype = birthtype

    @property
    def appearance(self):
        return self.__appearance

    @appearance.setter
    def appearance(self, appearance):
        self.__appearance = appearance

    @property
    def blooded(self):
        return self.__blooded

    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    # can be used to cast our object as a string
    # type(self).__name__ returns the class name
    def __str__(self):
        return "A {} is {} it is {} it is {}".format(type(self).__name__,
                                                     self.__birthtype,
                                                     self.__appearance,
                                                     self.__blooded)


# Create a mammal class that inherits from animal
# you can inherit from multiple classes by separating the classes with a comma in the parentheses
class Mammal(Animal):
    def __init__(self, birthype="born alive", appearance="hair 0f fur", blooded="warm blooded", nurseYoung=True):
        # call for the super class to initialize fields
        Animal.__init__(self, birthype, appearance, blooded)
        self.__nurseYoung = nurseYoung

    # we can extend the subclasses
    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    # overwrite __str__
    # you can use super() to refer to the superclass
    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)


class Reptile(Animal):
    def __init__(self, birthtype="born in an egg or born alive", appearance="dry scales", blooded="cold blooded"):
        # call for the supper class to initialize fields
        Animal.__init__(self, birthtype, appearance, blooded)

    # operator overloading isn't necessary in python because
    # python allows you to enter unknown numbers of values
    # always make sure self is the first attribute in your class methods
    def sumAll(self, *args):
        sum = 0

        for i in args:
            sum += i
        return sum


def getbirthtype(theObject):
    print(" the {} is {}".format(type(theObject).__name__, theObject.birthtype))

def main():
    animal1 = Animal("born alive")
    print(animal1.birthtype)

    # call __str__()
    print(animal1)
    print()

    mammal1 = Mammal()
    print(mammal1)
    print(mammal1.birthtype)
    print(mammal1.appearance)
    print(mammal1.blooded)
    print(mammal1.nurseYoung)
    print()

    reptile1 = Reptile()
    print(reptile1.birthtype)
    print(reptile1.appearance)
    print(reptile1.blooded)
    print()

    # operator overloading in python
    print("sum : {}".format(reptile1.sumAll(1, 2, 3, 4, 5)))

    getbirthtype(mammal1)
    getbirthtype(reptile1)


main()
