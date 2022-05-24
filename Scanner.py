#!/usr/bin/python

import socket

class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f'Scanner {self.ip}'

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport+1):
            if(self.is_open(port)):
                self.add_port(port)
    
    def is_open(self, port):
        pass

    def write(self, filepath):
        pass

def main():
    ip = '192.168.1.106'
    scanner = Scanner(ip)
    print(repr(scanner))


if __name__ == '__main__':
    main()