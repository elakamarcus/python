#!/bin/python

import sys
import requests
import json
import whois
import datetime

#apikey = '9fc37298ba646b201891c8d6687e5bad2cd93498c06313f8bcdf643f27705902'
apikey = '' # update with apikey, probably parameter
resource = 'b4429d77586798064b56b0099f0ccd49' # update with sys.argv

class target_properties:
    def __init__(self, id, currdate, registrar, country, total, positives, malware, malicious )
        self.id = id
        self.currdate = datetime.date.today()
        self.registrar = registrar
        self.country = country
        self.total = total
        self.hits = positives
        self.malware = malware
        self.malicious = malicious # true/false

def lookupwhis(ref):
    result = whois.query(ref)
    pass

def isMalicious(tot, positives):
    if (positives > 5):
        return True
    return False

def whatMalware(ref):
    pass

def dovirtotal(ref):
    """
    TODO: some code to do a virustotal query, get:
        - total / positive
        - search result, count words and include most common as result 
            - consider merge Win32/W32 
        - ref should be json...
    """
    pass


sampleresult = '{"scans": {"Bkav": {"detected": true, "version": "1.3.0.9899", "result": "W32.StuxnetQKN.Worm", "update": "20200518"}, "MicroWorld-eScan": {"detected": true, "version": "14.0.409.0", "result": "Gen:Variant.NSAnti.1", "update": "20200518"}, "CMC": {"detected": true, "version": "1.1.0.977", "result": "Worm.Win32.Stuxnet!O", "update": "20190321"}, "CAT-QuickHeal": {"detected": true, "version": "14.00", "result": "TrojanDropper.Stuxnet.A", "update": "20200518"}, "Qihoo-360": {"detected": true, "version": "1.0.0.1120", "result": "Malware.Radar01.Gen", "update": "20200518"}, "McAfee": {"detected": true, "version": "6.0.6.653", "result": "Artemis!B4429D775867", "update": "20200518"}, "Cylance": {"detected": true, "version": "2.3.1.101", "result": "Unsafe", "update": "20200518"}, "VIPRE": {"detected": true, "version": "83814", "result": "Trojan-Dropper.Win32.Stuxnet.A (v)", "update": "20200518"}, "AegisLab": {"detected": false, "version": "4.2", "result": null, "update": "20200518"}, "Sangfor": {"detected": true, "version": "1.0", "result": "Malware", "update": "20200423"}, "K7AntiVirus": {"detected": true, "version": "11.110.34124", "result": "Trojan ( 004bb9201 )", "update": "20200518"}, "Alibaba": {"detected": true, "version": "0.3.0.5", "result": "Worm:Win32/Stuxnet.81164c96", "update": "20190527"}, "K7GW": {"detected": true, "version": "11.110.34125", "result": "Trojan ( 004bb9201 )", "update": "20200518"}, "Cybereason": {"detected": true, "version": "1.2.449", "result": "malicious.758679", "update": "20190616"}, "Arcabit": {"detected": true, "version": "1.0.0.875", "result": "Trojan.NSAnti.1", "update": "20200518"}, "Invincea": {"detected": true, "version": "6.3.6.26157", "result": "heuristic", "update": "20200502"}, "Baidu": {"detected": false, "version": "1.0.0.2", "result": null, "update": "20190318"}, "F-Prot": {"detected": true, "version": "4.7.1.166", "result": "W32/Backdoor2.HTYL", "update": "20200518"}, "Symantec": {"detected": true, "version": "1.11.0.0", "result": "Trojan.Gen.MBT", "update": "20200518"}, "ESET-NOD32": {"detected": true, "version": "21346", "result": "Win32/Stuxnet.A", "update": "20200518"}, "APEX": {"detected": true, "version": "6.22", "result": "Malicious", "update": "20200516"}, "Paloalto": {"detected": false, "version": "1.0", "result": null, "update": "20200518"}, "ClamAV": {"detected": true, "version": "0.102.3.0", "result": "Win.Worm.Stuxnet-8", "update": "20200518"}, "Kaspersky": {"detected": true, "version": "15.0.1.13", "result": "Worm.Win32.Stuxnet.z", "update": "20200518"}, "BitDefender": {"detected": true, "version": "7.2", "result": "Gen:Variant.NSAnti.1", "update": "20200518"}, "NANO-Antivirus": {"detected": true, "version": "1.0.134.25112", "result": "Trojan.Win32.Stuxnet.biygo", "update": "20200518"}, "SUPERAntiSpyware": {"detected": false, "version": "5.6.0.1032", "result": null, "update": "20200513"}, "Avast": {"detected": true, "version": "18.4.3895.0", "result": "FileRepMalware", "update": "20200518"}, "Rising": {"detected": true, "version": "25.0.0.25", "result": "Worm.Win32.Stuxnet.r (CLASSIC)", "update": "20200518"}, "Ad-Aware": {"detected": true, "version": "3.0.5.370", "result": "Gen:Variant.NSAnti.1", "update": "20200518"}, "Sophos": {"detected": true, "version": "4.98.0", "result": "Troj/Stuxnet-A", "update": "20200518"}, "Comodo": {"detected": true, "version": "32453", "result": "Worm.Win32.Stuxnet.B@2cd2cp", "update": "20200518"}, "F-Secure": {"detected": true, "version": "12.0.86.52", "result": "Trojan.TR/Dropper.Gen", "update": "20200518"}, "DrWeb": {"detected": true, "version": "7.0.46.3050", "result": "Trojan.Stuxnet.2", "update": "20200518"}, "Zillya": {"detected": true, "version": "2.0.0.4092", "result": "Worm.Stuxnet.Win32.14", "update": "20200518"}, "TrendMicro": {"detected": true, "version": "11.0.0.1006", "result": "TROJ_STUXNET.AF", "update": "20200518"}, "McAfee-GW-Edition": {"detected": true, "version": "v2017.3010", "result": "BehavesLike.Win32.Downloader.hc", "update": "20200518"}, "Trapmine": {"detected": false, "version": "3.2.25.947", "result": null, "update": "20200505"}, "FireEye": {"detected": true, "version": "32.31.0.0", "result": "Generic.mg.b4429d7758679806", "update": "20200508"}, "Emsisoft": {"detected": true, "version": "2018.12.0.1641", "result": "Gen:Variant.NSAnti.1 (B)", "update": "20200518"}, "SentinelOne": {"detected": true, "version": "4.3.0.0", "result": "DFI - Suspicious PE", "update": "20200513"}, "Cyren": {"detected": true, "version": "6.3.0.2", "result": "W32/Backdoor.CCJX-3242", "update": "20200518"}, "Jiangmin": {"detected": true, "version": "16.0.100", "result": "Trojan/Generic.afza", "update": "20200518"}, "Webroot": {"detected": true, "version": "1.0.0.403", "result": "W32.Stuxnet", "update": "20200518"}, "Avira": {"detected": true, "version": "8.3.3.8", "result": "TR/Dropper.Gen", "update": "20200518"}, "Antiy-AVL": {"detected": true, "version": "3.0.0.1", "result": "Worm/Win32.Stuxnet", "update": "20200518"}, "Kingsoft": {"detected": false, "version": "2013.8.14.323", "result": null, "update": "20200518"}, "Microsoft": {"detected": true, "version": "1.1.17000.7", "result": "Trojan:Win32/Stuxnet.E", "update": "20200518"}, "Endgame": {"detected": true, "version": "4.0.2", "result": "malicious (high confidence)", "update": "20200512"}, "ViRobot": {"detected": true, "version": "2014.3.20.0", "result": "Dropper.Stuxnet.611840", "update": "20200518"}, "ZoneAlarm": {"detected": true, "version": "1.0", "result": "Worm.Win32.Stuxnet.z", "update": "20200518"}, "Avast-Mobile": {"detected": false, "version": "200518-00", "result": null, "update": "20200518"}, "GData": {"detected": true, "version": "A:25.25662B:26.18776", "result": "Gen:Variant.NSAnti.1", "update": "20200518"}, "TACHYON": {"detected": true, "version": "2020-05-18.01", "result": "Trojan/W32.Agent.611840.AC", "update": "20200518"}, "AhnLab-V3": {"detected": true, "version": "3.17.6.27456", "result": "Win-Trojan/Stuxnet.615936", "update": "20200518"}, "Acronis": {"detected": true, "version": "1.1.1.76", "result": "suspicious", "update": "20200515"}, "VBA32": {"detected": true, "version": "4.4.0", "result": "Malware-Cryptor.Inject.gen.2", "update": "20200518"}, "ALYac": {"detected": false, "version": "1.1.1.5", "result": null, "update": "20200518"}, "MAX": {"detected": true, "version": "2019.9.16.1", "result": "malware (ai score=100)", "update": "20200518"}, "Malwarebytes": {"detected": false, "version": "3.6.4.335", "result": null, "update": "20200518"}, "Zoner": {"detected": false, "version": "0.0.0.0", "result": null, "update": "20200517"}, "TrendMicro-HouseCall": {"detected": true, "version": "10.0.0.1040", "result": "TROJ_STUXNET.AF", "update": "20200518"}, "Tencent": {"detected": true, "version": "1.0.0.1", "result": "Win32.Worm.Stuxnet.Pdlq", "update": "20200518"}, "Yandex": {"detected": true, "version": "5.5.2.24", "result": "Trojan.DR.Stuxnet!xE7D7l8HRzY", "update": "20200518"}, "Ikarus": {"detected": true, "version": "0.1.5.2", "result": "Trojan.Win32.Stuxnet", "update": "20200518"}, "eGambit": {"detected": true, "version": null, "result": "Trojan.Generic", "update": "20200518"}, "Fortinet": {"detected": true, "version": "6.2.142.0", "result": "W32/Stuxnet.A!worm", "update": "20200518"}, "BitDefenderTheta": {"detected": true, "version": "7.2.37796.0", "result": "Gen:NN.ZexaF.34110.LuW@auwjPjf", "update": "20200514"}, "AVG": {"detected": true, "version": "18.4.3895.0", "result": "FileRepMalware", "update": "20200518"}, "Panda": {"detected": true, "version": "4.6.4.2", "result": "Trj/CI.A", "update": "20200518"}, "CrowdStrike": {"detected": true, "version": "1.0", "result": "win/malicious_confidence_100% (W)", "update": "20190702"}, "MaxSecure": {"detected": true, "version": "1.0.0.1", "result": "Trojan.Malware.1490988.susgen", "update": "20200518"}}, "scan_id": "56f6b74cd7c19b5f4a9b9acf7d203e252f9e3afb43294d9784deacce31d69534-1589815712", "sha1": "f6cd3094f1eefba2fe2d66bdbc13d551380c6f93", "resource": "b4429d77586798064b56b0099f0ccd49", "response_code": 1, "scan_date": "2020-05-18 15:28:32", "permalink": "https://www.virustotal.com/gui/file/56f6b74cd7c19b5f4a9b9acf7d203e252f9e3afb43294d9784deacce31d69534/detection/f-56f6b74cd7c19b5f4a9b9acf7d203e252f9e3afb43294d9784deacce31d69534-1589815712", "verbose_msg": "Scan finished, information embedded", "total": 72, "positives": 62, "sha256": "56f6b74cd7c19b5f4a9b9acf7d203e252f9e3afb43294d9784deacce31d69534", "md5": "b4429d77586798064b56b0099f0ccd49"}'
b = json.loads(sampleresult)
p1 = target_properties(1)
p1.total = b["total"]
p1.hits = b["positives"]
p1.malware = isMalicious(p1.total, p1.hits)

""
for (k, v) in b["scans"].items():
    try:
        print(v["result"])
    except:
        pass
