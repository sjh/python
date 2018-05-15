#!/usr/bin/env python3

from functools import reduce


def default_argument(value1, value2=[], value3={}):
    """ Showing that default argument function instance is evaluated only once. """

    value2.append(value1)
    value3[value1] = value1
    print("value2 = {}, value3 = {}".format(value2, value3))


def positional_keyword_arguments(arg1, args2 = -1, *args, **kwargs):
    """ argument 1, tuple arguments *args, positional arguments ** kwargs """

    print("args type = {}".format(type(args)))
    print("kwargs type = {}".format(type(kwargs)))
    print("arg1 = {}, args2 = {}, args = {}, kwargs = {}".format(arg1, args2, args, kwargs))

    """
    for k, v in kwargs.items():
        print("k = {}, v = {}".format(k, v))
    """


def multiply_args(*args):
    """ Multiply each one of args. """

    z = 1
    for a in args:
        z *= a

    print("product = {}".format(z))


def extend_list(val, alist=[]):
    alist.append(val)
    print("list = {}".format(alist))
    return alist


if __name__ == "__main__":
    default_argument(0)

    default_argument(1)

    default_argument(2)

    positional_keyword_arguments(1)
    positional_keyword_arguments(1, 2, 3, k=4, l=5, m=6)
    kwargs = {'k': 7, 'l': 8, 'm': 9}
    positional_keyword_arguments(1, 2, 3, kwargs)

    multiply_args(2, 3, 4, 5)
    print("reduced product = {}".format(reduce(lambda a, b: a*b, [2, 3, 4, 5])))

    args_tuple = (1, 2, 3, 4, 5, 6)

    extend_list(10)
    extend_list(123, [])
    extend_list('a')
