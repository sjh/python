#!/usr/bin/env python
#_*_ coding: utf-8 _*_


u"""
A program to demonstrate printing exception line number for easier debug messages.
Inspired and copied mostly from http://pythonnote.blogspot.tw/2013/12/python-try-except.html.
"""

import logging
import sys


logging.basicConfig(level=logging.DEBUG)
LOGGER = logging.getLogger()


def print_exception_lineno():
    try:
        [][2]
    except IndexError as e:
        print u'Error', e, ' on line {}'.format(sys.exc_info()[-1].tb_lineno)
        LOGGER.exception(e)

if __name__ == '__main__':
    print_exception_lineno()
