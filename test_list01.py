def sendTCP(d, p):
    flags = ["S","A","F","R"]
    for x in range (0, len(flags)):
        print("IP(dst="+d+")/TCP(flags="+flags[x]+", sport=RandShort(), dport="+p)

sendTCP("1.1.1.2", "2.2.2.1")
