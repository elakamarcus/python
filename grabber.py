#!/usr/bin/python

import socket

class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))

    def read(self, lenght=1024):
        return self.socket.recv(lenght)

    def close(self):
        self.socket.close()

def main():
    grabber = Grabber('192.168.1.106', 22)
    print(grabber.read().strip())
    grabber.close()

if __name__ == '__main__':
    main()