from scapy.all import *
import base64

if len(sys.argv) < 2:
    print "Too few arguments. Don't be cheap."
    exit()
if len(sys.argv) > 5:
    print "Too many arguments. Don't be greedy."
    exit()

s = sys.argv[1]
d = sys.argv[2]
q = 5
if sys.argv[3]:
   count = int(sys.argv[3])
else:
   count = 1

if len(sys.argv) > 2:
    ping = sys.argv[3]
else:
    ping = q + 1

def boingboing(q, p):
#   while q < ping:
    send(p, verbose=0)
    global count
#   count = count + 1
    print(str(count) + " spikes sent")

def build(d, s):
    p = IP(dst= d, src= s)/UDP(sport= 514, dport= 514)
    p.payload = base64.b64decode(PWD)
    p.show()
    global q
    boingboing(q, p)


PWD = "PDEzPkRlYyAzMCAxMjo1NzowMiAxMC4xMjEuMzMuMTAwIEFnZW50RGV2aWNlPVdpbmRvd3NMb2cgICAgQWdlbnRMb2dGaWxlPVNlY3VyaXR5ICAgIFBsdWdpblZlcnNpb249MS4wLjE0ICAgIFNvdXJjZT1NaWNyb3NvZnQtV2luZG93cy1TZWN1cml0eS1BdWRpdGluZyAgICBDb21wdXRlcj1ISy1SV0RDLTIwMDMuYWdvZGEubG9jYWwgICAgVXNlcj0gICAgIERvbWFpbj0gICAgIEV2ZW50SUQ9NDYyNSAgICBFdmVudElEQ29kZT00NjI1ICAgIEV2ZW50VHlwZT0xNiAgICBFdmVudENhdGVnb3J5PTEyNTQ0ICAgIFJlY29yZE51bWJlcj0yNjUwMDUyODM2ICAgIFRpbWVHZW5lcmF0ZWQ9MTQ4MzA3NzQxNiAgICBUaW1lV3JpdHRlbj0xNDgzMDc3NDE2ICAgIE1lc3NhZ2U9QW4gYWNjb3VudCBmYWlsZWQgdG8gbG9nIG9uLiAgU3ViamVjdDogIFNlY3VyaXR5IElEOiAgTlQgQVVUSE9SSVRZXFNZU1RFTSAgQWNjb3VudCBOYW1lOiAgSEstUldEQy0yMDAzJCAgQWNjb3VudCBEb21haW46ICBURVNUICBMb2dvbiBJRDogIDB4M2U3ICBMb2dvbiBUeXBlOiAgIDMgIEFjY291bnQgRm9yIFdoaWNoIExvZ29uIEZhaWxlZDogIFNlY3VyaXR5IElEOiAgTlVMTCBTSUQgIEFjY291bnQgTmFtZTogIFJ1bGVUZXN0QWNjb3VudCAgQWNjb3VudCBEb21haW46ICBURVNUICBGYWlsdXJlIEluZm9ybWF0aW9uOiAgRmFpbHVyZSBSZWFzb246ICBVbmtub3duIHVzZXIgbmFtZSBvciBiYWQgcGFzc3dvcmQuICAgU3RhdHVzOiAgIDB4YzAwMDAwNmQgIFN1YiBTdGF0dXM6ICAweGMwMDAwMDZhICBQcm9jZXNzIEluZm9ybWF0aW9uOiAgQ2FsbGVyIFByb2Nlc3MgSUQ6IDB4MzcwICBDYWxsZXIgUHJvY2VzcyBOYW1lOiBDOlxXaW5kb3dzXFN5c3RlbTMyXGxzYXNzLmV4ZSAgTmV0d29yayBJbmZvcm1hdGlvbjogIFdvcmtzdGF0aW9uIE5hbWU6IEhLLVJXREMtMjAwMyAgU291cmNlIE5ldHdvcmsgQWRkcmVzczogMTAuMTIxLjMzLjExNiAgU291cmNlIFBvcnQ6ICA0MjIyNSAgRGV0YWlsZWQgQXV0aGVudGljYXRpb24gSW5mb3JtYXRpb246ICBMb2dvbiBQcm9jZXNzOiAgQWR2YXBpICAgIEF1dGhlbnRpY2F0aW8="
DNS = "PDEzPkRlYyAyOCAyMTo0OTo1MSAxMC4xMjAuMS4xMjMgQWdlbnREZXZpY2U9RmlsZUZvcndhcmRlcglBZ2VudExvZ0ZpbGU9ZG5zLnR4dAlQYXlsb2FkPTEyLzI4LzIwMTYgOTo0OTozMCBQTSAwOTA4IFBBQ0tFVCAgMDAwMDAwNTE2NEY3MjEzMCBVRFAgUmN2IDEwLjEyMC43MC4zNCAgICA0NDI5ICAgUSBbMDAwMSAgIEQgICBOT0VSUk9SXSBBICAgICAgKDE2KXZpbnRhZ2VwcmludGFibGUoMyljb20oMCkN="

build(d, s)