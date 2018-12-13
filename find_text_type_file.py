#!/usr/bin/env python3


import os
import subprocess
import sys


def find_text_files(directory):
    ''' , '''

    file_list = []
    abspath = os.path.abspath(directory)
    for i in os.listdir(directory):
        result = subprocess.run(['file', "{}/{}".format(abspath, i)], stdout=subprocess.PIPE)
        if 'text' in result.stdout.decode('utf-8').split(':')[-1]:
            file_list.append(i)

    return file_list


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error, should provide one parameter for program {}".format(sys.argv[0]))
        sys.exit(1)

    results = find_text_files(sys.argv[1])
    print(results)
