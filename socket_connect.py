import socket
import sys

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
        print "Failed to create socket. Error code: " + str(msg[0]) + ", Error message: " + str(msg[1])
        sys.exit();

print 'Socket Created'
host = 'www.google.com'
port = 8888

try:
        remote_ip = socket.gethostbyname( host )
except socket.gaierror:
        print 'Hostname could not be resolved. Terminating.'
        sys.exit();
print 'IP address of ' + host + ' is ' + remote_ip

try:
	s.connect((remote_ip, port))
except socket.error as msg:
	print "Failed connect to " + host + ". Error code: " + str(msg[0]) + ", Error message: " + str(msg[1])
	sys.exit();

print 'Socket connected to ' + host + ' on ip ' + remote_ip
