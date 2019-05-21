import requests
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode

"""
 A simple user-agent, for the request header
 
 TODO: convert to py3
"""
rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

url = "https://aqicn.org/city/hongkong/yuen-long/"
r = requests.get(url, headers = rh)
soup = BeautifulSoup(r.text, "lxml")
x = soup.find("div", {"class":"aqivalue"})

print "[+] " + x.text
print "[!] " + x["title"].encode('ascii', 'ignore')
