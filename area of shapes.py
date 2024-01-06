import math


def get_area(shape):
    shape = shape.lower()

    if shape == "rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "parallelogram":
        parallelogram_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "rhombus":
        rhombus_area()
    elif shape == "trapezoid":
        trapezoid_area()
    else:
        print("please enter circle, rectangle, triangle, rhombus, parallelogram or trapezoid")


def rectangle_area():
    length = float(input("enter the length: "))
    width = float(input("enter the width: "))
    area = length * width
    print("area of rectangle is: ", area)


def circle_area():
    radius = float(input("enter the radius: "))
    area = math.pi * math.pow(radius, 2)
    print("area of circle is {:.2f} " .format(area))


def parallelogram_area():
    base = int(input("enter the base: "))
    height = int(input("enter the height: "))
    area = base * height
    print("area of parallelogram is: ", area)


def triangle_area():
    base = int(input("enter the base: "))
    height = int(input("enter the height: "))
    area = (base * height) / 2
    print("area of triangle is: ", area)


def rhombus_area():
    diagonal1 = int(input("enter diagonal1: "))
    diagonal2 = int(input("enter diagonal2: "))
    area = (diagonal1 * diagonal2) / 2
    print("area of the rhombus is: ", area)


def trapezoid_area():
    a = int(input("enter length1: "))
    b = int(input("enter length2: "))
    h = int(input("enter the height: "))
    area = ((a + b) * h) * 0.5
    print("area of trapezoid is: ", area)


def main():
    shape = input("enter the shape: ")
    get_area(shape)


main()
