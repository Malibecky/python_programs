class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

    try:
        dog_name = input("what is your dog name: ")

        if any(char.isdigit() for char in dog_name):
            raise NameError


    except NameError:
        print("your dog name can't contain a number")
