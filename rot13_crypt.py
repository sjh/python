#!/usr/bin/env python3

''' Read file from first argument and print out the rot13 mapped file content in stdout. '''

import string
import sys


def create_rot13_map():
    ''' Create the dictionary map for rot13 decryption. '''

    original_string = string.ascii_uppercase + string.ascii_lowercase
    mapped_string = string.ascii_uppercase[13:] + string.ascii_uppercase[0:13] + string.ascii_lowercase[13:] + \
        string.ascii_lowercase[0:13]
    rot13_decryption = dict(zip(original_string, mapped_string))

    return rot13_decryption


def run_rot13(filename):
    ''' Decrypt the encrypted rot13 string and return the decrypted string. '''

    rot13ed_string = ''
    rot13_map = create_rot13_map()

    with open(filename, mode='r', encoding='UTF-8', errors='ignore') as f:
        for line in f.readlines():
            new_line = ''
            for original in line:
                if original in rot13_map.keys():
                    rot13ed = rot13_map[original]
                else:
                    rot13ed = original

                new_line = new_line + rot13ed

            rot13ed_string = ''.join([rot13ed_string, new_line])

    return rot13ed_string


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: {} rot13ed_filename'.format(sys.argv[0]))
        sys.exit(1)

    rot13ed = run_rot13(sys.argv[1])
    print(rot13ed)
