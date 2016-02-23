#!/usr/bin/env python
# _*_ coding: utf-8 _*_

u""" One way of implementing default dictionary. """


class DefaultDict(dict):
    def __missing__(self, key):
        u""" Return default value as key if no value specified dictionary key. """
        return key


if __name__ == "__main__":
    d = DefaultDict()
    print d, type(d), d.keys()

    d['flop'] = 127
    print d, type(d), d.keys()

    d['flip'] = 130
    print d, type(d), d.keys()

    print d['no_value']
