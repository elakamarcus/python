import requests
from bs4 import BeautifulSoup
import lxml
import sys
from unidecode import unidecode
import datetime

f = open("bajsfil", "a")

rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

for url in open("newsURLs", "r"):
    url = str(url).replace('\n','') # for some odd reason, some URLs add a newline?!
    r = requests.get(url, headers = rh)
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    try:
        f.write('\n' + "<p>" +
            "<div class=\"title\">" + title["content"].encode('ascii', 'ignore') + "</div>" + '\n' +
            "<div class=\"description\">" + description["content"].encode('ascii', 'ignore') + "</div>" + '\n' +
            "<div class=\"lank\">" + url + "</div>" + "</p>" + '\n')
    except:
        pass

f.close()