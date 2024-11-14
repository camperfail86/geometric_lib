from math import sqrt


def area(a, b, c):
    semiperimeter = (a + b + c) / 2
    return sqrt(
        semiperimeter * (semiperimeter - a) * (semiperimeter - b) * (semiperimeter - c)
    )


def perimeter(a, b, c):
    return a + b + c
