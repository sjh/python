#!/usr/bin/env python3

import functools
import sys


# Two options for implementing printing without new line in print function of python3
printf = sys.stdout.write  # raw system io with sys.stdout.write
printf = functools.partial(print, end="")  # print with positional parameter of end=""


def print_crossed_rectangle():
    """

##########
##      ##
# #    # #
#  #  #  #
#   ##   #
#   ##   #
#  #  #  #
# #    # #
##      ##
##########

    """

    for y in range(10):
        for x in range(10):

            if (y == 0) or (y == 9) or (x == 0) or (x == 9) or (y == x) or ((y + x) == 9):
                printf("#")
            else:
                printf(" ")

        printf("\n")

    sys.stdout.flush()  # Make sure we flush the i/o buffer


if __name__ == "__main__":
    print_crossed_rectangle()
