#!/usr/bin/env python
import socket
import ssl
import pprint

SSL_PORT = 443
SSL_HOST = 'www.verisign.com'

class DemoHttpsSslEncryptParts(object):
    def __init__(self):
        self.request_data = """GET /this/is/encrypted/uri HTTP/1.1\r\n\r\n"""

    def create_ssl_socket(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((SSL_HOST, SSL_PORT))
        self.ssl_socket = socket.ssl(s)

    def show_server_ca_info(self):
        print 'show server ca info'
        print repr(self.ssl_socket.server())
        print repr(self.ssl_socket.issuer())

    def send_encrypted_data(self):
        print 'send encrypted data ', self.request_data
        self.ssl_socket.write(self.request_data)

    def read_encrypted_data(self):
        print 'read encrypted data'
        data = self.ssl_socket.read()
        print data

if __name__ == '__main__':
    dhsep = DemoHttpsSslEncryptParts()
    dhsep.create_ssl_socket()
    dhsep.show_server_ca_info()
    dhsep.send_encrypted_data()
    dhsep.read_encrypted_data()



