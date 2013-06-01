#!/usr/bin/env python
#_*_ coding:utf8 _*_

import subprocess


def debug_decorator(func, *args, **kwargs):
    def inner_debug_decorator(*args, **kwargs):
        try:
            import ipdb
        except ImportError as e_:
            print e_
            subprocess.call(["pip", "install", "ipdb"])

        print 'decorating'
        import ipdb
        ipdb.set_trace()
        return func(*args, **kwargs)
    return inner_debug_decorator


@debug_decorator
def print_function(input):
    a = 1
    b = 3
    print 'I need some debuggin decorating, input = {}'.format(a + b + input)


if __name__ == '__main__':
    print_function(10)
