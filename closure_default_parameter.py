#!/usr/bin/env python3


def create_multipliers_late_binding():
    """ https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make create closure
    with late binding effect. """

    return [lambda x: i * x for i in range(5)]


def create_multipliers():
    """ https://www.toptal.com/python/top-10-mistakes-that-python-programmers-make create closure
    with default parameters(i = i) to prevent late binding effect. """

    return [lambda x, i = i: i * x for i in range(5)]


if __name__ == "__main__":
    for mult in create_multipliers_late_binding():
        print(mult.__name__)
        print(mult.__defaults__)
        print(mult(2))

    for mult in create_multipliers():
        print(mult.__name__)
        print(mult.__defaults__)
        print(mult(2))
