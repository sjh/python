#!/usr/bin/env python3


import socket
import sys

PINCODE_LIMIT = 10000
BUF_SIZE = 1000


def enumerate_pincode(host, port, prefix):
    ''' Enumerate the possible pincode to fuzz test the text input. '''

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    for i in range(PINCODE_LIMIT):
        read = sock.recv(BUF_SIZE)
        print('Read output = {}'.format(read))
        sent = sock.send("{} {:04d}\n".format(prefix, i).encode('utf-8'))


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Enumerate {} fuzzer usage: {} host port prefix'.format(PINCODE_LIMIT, sys.argv[0]))
        sys.exit(1)

    host, port, prefix = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    enumerate_pincode(host, port, prefix)
