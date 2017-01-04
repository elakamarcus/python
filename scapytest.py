# Noisy script to trigger IDS/IPS alerts.
import sys
import random
import logging # This and the following line are used to omit the IPv6 error displayed by importing scapy.
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#using scapy as it is ages easier than raw socket e.g. import socket and then call AF_INET etc.
from scapy.all import *
import argparse
import os
import urllib2
if os.getuid() != 0: # Checks to see if the user running the script is root.
    print("You need to run this program as root for it to function correctly.")
    sys.exit(1)
parser = argparse.ArgumentParser(description='This tool sends requests to the target specified in the arguments.') # This and preceding 4 lines used to control the arguments entered in the CLI.
parser.add_argument('-d', action="store",dest='source', help='The destination IP address for the SYN packet')
parser.add_argument('-c', action="store",dest='count', help='The amount of packets to send. (enter X for unlimited)')
parser.add_argument('-p', action="store",dest='port', help='The destination port. Will be used except for ICMP')
args = parser.parse_args()
if len(sys.argv) == 1: # Forces the help text to be displayed if no arguments are entered
    parser.print_help()
    sys.exit(1)
args = vars(args) # converts the arguments into dictionary format for easier retrieval.
i = 0 # variable used to control the while loop for the amount of times a packet is sent.

#Function to send various flags. Each may trigger alert by IDS/IPS
def sendTCP(d, p):
    flags = ["S","A","F","R"]
    for x in range (0, len(flags)):
        a=IP(dst=d)/TCP(flags=flags[x], sport=RandShort(), dport=p)
    send(a, verbose=0) #transmit packet


def sendUDP(d, p):
    a=IP(dst=d)/UDP(sport=RandShort(), dport=p)
    send(a, verbose=0)

def spoofIP(i):
    #return the gateway of provided IP..~~
    b=i
    a=IP(dst= d, src= b)
    return b

def sendSMURF(d, p):
    print("tralalala~ smurf -->\r\n")
    s=spoofIP(d)
    
def sendFRAG(d, p):
    sekvens=[1,2,4,3,6,5,8,7,10,9]
    for x in range (0, len(sekvens)):
        a=IP(dst=d,src=s)/TCP(flags="S", sport=RandShort(), dport=p,seq=sekvens[x])
        send(a)

def sendAPT(d, p):
    #ip2b 8bit + 4bit + 5bit
    lurk=[0x4c,0x55,0x52,0x4b,0x30]
    ip2b=[0x12,0x34,0x56,0x78,0x10,0x00,0x10,0x00,0xFF,0xFF,0xFF,0xFF,0x00,0x18,0x09,0x07,0x20]
    qdigit=[0x51,0x31,0x39,0x21,0x00]
    rats=["Gh0st", lurk, ip2b, qdigit]
    for x in range (0, len(rats)):
        a=IP(dst=d)/TCP(flags="S", sport=RandShort(), dport=p)
        #add apt string to payload
        a.payload=str(rats[x])
        print("Sending rat: "+rats[x])
        send(a, verbose=0)


if args['count'] == "X" or args['count'] == "x": #x marks the spot
    while (1 == 1):
        sendTCP(args['source'], int(args['port']))
        i = i + 1
        print(str(i) + " Packet Sent")
else: # executed if the user defined an amount to send.
    while i < int(args['count']):
        sendTCP(args['source'], int(args['port']))
        i = i + 1
        print(str(i) + " Packet Sent")
print("All packets successfully sent.")
