import requests
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode

rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

yuenlong = "https://aqicn.org/city/hongkong/yuen-long/"

urllist = ["https://aqicn.org/city/hongkong/yuen-long/","https://aqicn.org/city/sweden/stockholm-sodermalm/", "https://aqicn.org/city/beijing/","http://aqicn.org/city/jiangsu/jintan/shijiancezhan/","http://aqicn.org/city/jiangsu/changzhou/"]
city = ["Yuen Long", "Stockholm", "Beijing  ", "Jintan   ", "Changzhou"]
print(" City\t\tAQI\tText")
print ("---------------------------------------")
for a in range(0,len(urllist)):
        url = urllist[a]
        r = requests.get(url, headers = rh)
        if r.status_code == 200:
                soup = BeautifulSoup(r.text, "lxml")
                x = soup.find("div", {"class":"aqivalue"})
                print("{}\t{}\t{}".format(city[a], x.text, x["title"]))
print("---------------------------------------")
print("              -- EOF --                ")