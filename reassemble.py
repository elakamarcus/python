#Code from the document of
#https://www.sans.org/reading-room/whitepapers/detection/ip-fragment-reassembly-scapy-33969

def rfc791(listoffragments): 
    buffer=StringIO.StringIO()
    for pkt in listoffragments: 
        buffer.seek(pkt[IP].frag*8)
        buffer.write(pkt[IP].payload)
    return buffer.getvalue()

def first(listoffragments): 
    buffer=StringIO.StringIO()
    for pkt in listoffragments[::-1]: 
        buffer.seek(pkt[IP].frag*8)
        buffer.write(pkt[IP].payload)
    return buffer.getvalue()

def bsd(listoffragments): 
    buffer=StringIO.StringIO()
    for pkt in sorted(listoffragments, key=lambda x:x[IP].frag)[::-1]: 
        buffer.seek(pkt[IP].frag*8)
        buffer.write(pkt[IP].payload)
    return buffer.getvalue()

def linux(listoffragments): 
    buffer=StringIO.StringIO()
    for pkt in sorted(listoffragments, key= lambda x:x[IP].frag, reverse=True): 
        buffer.seek(pkt[IP].frag*8)
        buffer.write(pkt[IP].payload)
    return buffer.getvalue()

def genfragments(): 
    pkts=scapy.plist.PacketList()
    pkts.append(IP(flags="MF",frag=0)/("1"*24))
    pkts.append(IP(flags="MF",frag=4)/("2"*16))
    pkts.append(IP(flags="MF",frag=6)/("3"*24))
    pkts.append(IP(flags="MF",frag=1)/("4"*32))
    pkts.append(IP(flags="MF",frag=6)/("5"*24))
    pkts.append(IP(frag=9)/("6"*24))
    return pkts

print "First show the packet"
print genfragments()
print "Reassembled using policy: First" 
print first(genfragments())
print "Reassembled using policy: Last/RFC791" 
print rfc791(genfragments())
print "Reassembled using policy: Linux" 
print linux(genfragments())
print "Reassembled using policy: BSD" 
print bsd(genfragments())
print "Reassembled using policy: BSD-Right"
print bsdright(genfragments())