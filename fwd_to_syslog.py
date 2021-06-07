#!/bin/python3

"""
    Send syslog data to remote syslog server:
    param1 = serverIP
    param2 = listening port on server (usually 514)
    param3 = data file containing log
        for now the data file is only containing one log
        future iterations maybe utilize readlines instead
        of read
"""
import sys
import logging
import logging.handlers

def sendLogs(ipaddr, port, logfile):
    mylog = logging.getLogger('PapaSmurf')
    mylog.setLevel(logging.INFO)
    handler = logging.handlers.SysLogHandler(address=(ipaddr,int(port)))
    mylog.addHandler(handler)
    with open(logfile, "r") as f:
        data = f.read()
        mylog.info(data)

if __name__ == "__main__":
    sendLogs(sys.argv[1], sys.argv[2], sys.argv[3]) if (len(sys.argv)-1) == 3 else print(f'Need 3 parameters. You gave me {len(sys.argv)}') 
