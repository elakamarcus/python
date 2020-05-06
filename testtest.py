import sys

def webserver(a, b):
    if a=="yes" and b=="yes":
        return 10
    elif b=="yes" and a=="no":
        return 5
    elif a=="yes" and b=="no":
        return 5

def vulnerability(vuln):
    if(vuln=="extweb"):
        print("Require controls in place:")
        print('\x1b[6;30;41m' + "~Confidentiality~")
        auth = raw_input("Part of site require authentication? Yes:No?")
        if(auth=="yes"):
            print('\x1b[6;30;41m' + "Authentication where applicable")
            print("++ If some part of the website require authentication")
            print("++ ensure there are solid authentication controls.")
        comm = raw_input('\x1b[6;30;42m' + "Site handle with ecommerce or other sensitive online?Yes:No")
        if(comm=="yes"):
            print('\x1b[6;30;41m' + "HTTPS/ valid ssl certificate")
            print("++ Valid ssl certificate is essential to establish")
            print("++ online trust. Especially for ecommerce.")
        print("Vetting of data published to public site")
        print("++ information posted on the public part of the site")
        print("++ should undergo initial vetting and review." + '\x1b[0m')
#        print("~Integrity~")
#        print("Code reviewi")
#        print("Penetration test")
#        print("Vulnerability scan")
#        print("Log monitoring")
#        print("++ Ensure there is continuous log monitoring")
#        print("++ and process in place for reporting events.")
#        print("~Availability~")
#        print("DDoS")
#        print("Backup power")
#        print("Hot/Warm secondary site")
    elif(vuln=="intweb"):
        print('\x1b[6;30;42m' + "Site internal"+ '\x1b[0m')

try:
 #   var = input("Unit one criticality [0-10]: ")
 #   print("Criticality: {}".format(var))
 #   print("Argv: {}".format(sys.argv))
    a = raw_input("Webserver? ")
    b = raw_input("External? ")
    if(a=="yes" and b=="yes"):
        vulnerability("extweb")
    elif(a=="yes" and b=="no"):
        vulnerability("intweb")

except:
    print("Input error")
    exit
