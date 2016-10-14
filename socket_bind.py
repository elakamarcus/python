import socket
import sys

host = '' # all interfaces
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((host, port))
except socket.error as msg:
	print "[-] Failed bind socket. " + str(msg[0]) + ": " + str(msg[1])
	sys.exit();

try:
	s.listen(10)
	print "[+] Success. Socket in listening mode."
except socket.error as msg:
        print "[-] Failed set socket listening mode. " + str(msg[0]) + ": " + str(msg[1])
	sys.exit();

conn, addr = s.accept()
print "[+] Connection initiated from " + str(addr[0]) + ": " + str(addr[1])

data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()
