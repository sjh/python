#!/usr/bin/env python3

import sys


def find_unique_line(file_name):
    ''' Find the unique line in file content. '''

    line_dict = {}
    with open(file_name, mode='r', encoding='UTF-8', errors='ignore') as f:
        for line in f.readlines():
            if line in line_dict.keys():
                line_dict[line] = line_dict[line] + 1
            else:
                line_dict[line] = 1

    for line, count in line_dict.items():
        if count == 1:
            print('unique line = {}'.format(line))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage {} filename'.format(sys.argv[0]))
        sys.exit(1)

    find_unique_line(sys.argv[1])
