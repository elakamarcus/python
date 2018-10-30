import requests
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode

fsec = open("security", "a")
fsci = open("science", "a")
fodd = open("other", "a")

rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

def grabber(fin, fout):
    for url in open(fin, "r"):
        url = str(url).replace('\n','')
        
        r = requests.get(url, headers = rh)
        soup = BeautifulSoup(r.text, "lxml")
        title = soup.find("meta", property="og:title")
        description = soup.find("meta", property="og:description")
        try:
            fout.write('\n' + "<p>" +
                "<div class=\"title\">" + title["content"].encode('ascii', 'ignore') + "</div>" + '\n' +
                "<div class=\"description\">" + description["content"].encode('ascii', 'ignore') + "</div>" + '\n' +
                "<div class=\"lank\">" + url + "</div>" + "</p>" + '\n')
        except:
            pass

grabber("newsSec", fsec)
fsec.close()

grabber("newsSci", fsci)
fsci.close()

grabber("newsOdd", fodd)
fodd.close()
