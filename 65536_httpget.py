#!/bin/python

from scapy.all import *

stri = "GET / HTTP/1.1\r\n\Set-Cookie: whatever"

def sendTCP(d, p):
# flags = ["S", "A", "F", "R"]
# for x in range(0, len(flags)):
   flags = "S"
   a = IP(dst=d)/TCP(flags=flags, sport=1337, dport=p)/stri
   send(a, verbose=0) #transmit packet

q=int(65535)
i=int(0)
while (i < q):
#change these...
   sendTCP("10.0.0.2", int("80"))
   i = i + 1
   #below will spam the screen, be prepared or comment out
   print str(i) + " Packet Sent"
print "All packets successfully sent."
print "Going to sleep mode ~~~."
