#!/usr/bin/env python3


from pathlib import Path
import os
import subprocess
import sys

LINE_LIMIT = 100


def find_text_files(directory):
    ''' find text files and look for file content less than 100 characters. '''

    file_list = []
    abspath = os.path.abspath(directory)
    files = [i[0] for i in os.walk(abspath)]
    for i in os.walk(abspath):
        for j in i[2]:
            file_abspath = '{}/{}'.format(i[0], j)
            path_obj = Path(file_abspath)
            if path_obj.is_file():
                result = subprocess.run(['file', "{}".format(file_abspath)], stdout=subprocess.PIPE)
                if 'text' in result.stdout.decode('UTF-8').split(':')[-1]:
                    print('** file path = {}'.format(file_abspath))
                    with open(file_abspath, mode='r', encoding='UTF-8', errors='ignore') as text_file:
                        for line in text_file.readlines():
                            if len(line) < LINE_LIMIT:
                                print(line)

                    file_list.append("{}".format(file_abspath))

    return file_list


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Error, should provide one parameter for program {}".format(sys.argv[0]))
        sys.exit(1)

    results = find_text_files(sys.argv[1])
