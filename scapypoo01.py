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
   while q < ping:
   send(p, verbose=0)
   global count
   count = count + 1
   print(str(count) + " spikes sent")
#   comment out for testing... 
    p.show()

def build(d, s):
    p = IP(dst= d, src= s)/UDP(sport= 514, dport= 514)
    # pwd brute force
    p.payload = base64.b64decode(PWD)
    p.show()
    global q
    boingboing(q, p)
    # dns C2 request
    p.payload = base64.b64decode(DNSCC)
    boingboing(q, p)
    # dns ransomware payment site
    p.payload = base64.b64decode(DNSP)
    boingboing(q, p)
    # dns ransomware distribution site
    p.payload = base64.b64decode(DNSD)
    boingboing(q, p)
    # todo: make above into a loop..

# blob of base64 LEEFs
PWD = "PDEzPkRlYyAzMCAxMjo1NzowMiAxMC4wLjAuMSBBZ2VudERldmljZT1XaW5kb3dzTG9nICAgIEFnZW50TG9nRmlsZT1TZWN1cml0eSAgICBQbHVnaW5WZXJzaW9uPTEuMC4xNCBTb3VyY2U9TWljcm9zb2Z0LVdpbmRvd3MtU2VjdXJpdHktQXVkaXRpbmcgICAgQ29tcHV0ZXI9RENXMjAwOC5jb3N0Y28uY29tICAgIFVzZXI9ICAgICBEb21haW49ICAgICBFdmVudElEPTQ2MjUgICAgRXZlbnRJRENvZGU9NDYyNSAgICBFdmVudFR5cGU9MTYgICAgRXZlbnRDYXRlZ29yeT0xMjU0NCAgICBSZWNvcmROdW1iZXI9MjY1MDA1MjgzNiAgICBUaW1lR2VuZXJhdGVkPTE0ODMwNzc0MTYgICAgVGltZVdyaXR0ZW49MTQ4MzA3NzQxNiAgICBNZXNzYWdlPUFuIGFjY291bnQgZmFpbGVkIHRvIGxvZyBvbi4gIFN1YmplY3Q6ICBTZWN1cml0eSBJRDogIE5UIEFVVEhPUklUWVxTWVNURU0gIEFjY291bnQgTmFtZTogIERDVzIwMDggIEFjY291bnQgRG9tYWluOiAgVEVTVCAgTG9nb24gSUQ6ICAweDNlNyAgTG9nb24gVHlwZTogICAzICBBY2NvdW50IEZvciBXaGljaCBMb2dvbiBGYWlsZWQ6ICBTZWN1cml0eSBJRDogIE5VTEwgU0lEICBBY2NvdW50IE5hbWU6ICBSdWxlVGVzdEFjY291bnQgIEFjY291bnQgRG9tYWluOiAgVEVTVCAgRmFpbHVyZSBJbmZvcm1hdGlvbjogIEZhaWx1cmUgUmVhc29uOiAgVW5rbm93biB1c2VyIG5hbWUgb3IgYmFkIHBhc3N3b3JkLiAgIFN0YXR1czogICAweGMwMDAwMDZkICBTdWIgU3RhdHVzOiAgMHhjMDAwMDA2YSAgUHJvY2VzcyBJbmZvcm1hdGlvbjogIENhbGxlciBQcm9jZXNzIElEOiAweDM3MCAgQ2FsbGVyIFByb2Nlc3MgTmFtZTogQzpcV2luZG93c1xTeXN0ZW0zMlxsc2Fzcy5leGUgTmV0d29yayBJbmZvcm1hdGlvbjogIFdvcmtzdGF0aW9uIE5hbWU6IERDVzIwMDggIFNvdXJjZSBOZXR3b3JrIEFkZHJlc3M6IDEwLjAuMC4xICBTb3VyY2UgUG9ydDogIDQyMjI1ICBEZXRhaWxlZCBBdXRoZW50aWNhdGlvbiBJbmZvcm1hdGlvbjogIExvZ29uIFByb2Nlc3M6ICBBZHZhcGkgICAgQXV0aGVudGljYXRpbw=="

DNSCC = "PDEzPkRlYyAyOCAyMTo0OTo1MSAxMC4xMjAuMS4xMjMgQWdlbnREZXZpY2U9RmlsZUZvcndhcmRlcglBZ2VudExvZ0ZpbGU9ZG5zLnR4dAlQYXlsb2FkPTEyLzExLzIwMTcgOTo0OTozMCBQTSAwOTA4IFBBQ0tFVCAgMDAwMDAwNTE2NEY3MjEzMCBVRFAgUmN2IDEwLjEyMC43MC4zNCAgICA0NDI5ICAgUSBbMDAwMSAgIEQgICBOT0VSUk9SXSBBICAgICAgKDE2KWphZHdhbHBpYWxhZHVuaWEoMilpbigwKQ0="
DNSP = "PDEzPkRlYyAyOCAyMTo0OTo1MSAxMC4xMjAuMS4xMjMgQWdlbnREZXZpY2U9RmlsZUZvcndhcmRlcglBZ2VudExvZ0ZpbGU9ZG5zLnR4dAlQYXlsb2FkPTEyLzExLzIwMTcgOTo0OTozMCBQTSAwOTA4IFBBQ0tFVCAgMDAwMDAwNTE2NEY3MjEzMCBVRFAgUmN2IDEwLjEyMC43MC4zNCAgICA0NDI5ICAgUSBbMDAwMSAgIEQgICBOT0VSUk9SXSBBICAgICAgKDE2KXZ5b2hhY3h6b3VlMzJ2dmsoNilvMDhyYTYoMyl0b3AoMCkN="
DNSD = "PDEzPkRlYyAyOCAyMTo0OTo1MSAxMC4xMjAuMS4xMjMgQWdlbnREZXZpY2U9RmlsZUZvcndhcmRlcglBZ2VudExvZ0ZpbGU9ZG5zLnR4dAlQYXlsb2FkPTEyLzExLzIwMTcgOTo0OTozMCBQTSAwOTA4IFBBQ0tFVCAgMDAwMDAwNTE2NEY3MjEzMCBVRFAgUmN2IDEwLjEyMC43MC4zNCAgICA0NDI5ICAgUSBbMDAwMSAgIEQgICBOT0VSUk9SXSBBICAgICAgKDE2KW9wdGltYWxwb2xhbmQoMilwbCgwKQ0="

build(d, s)