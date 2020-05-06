## HSBC HK Hibor scraping...

import requests
from bs4 import BeautifulSoup

def countRate(r):
#x is to be set to the variable... should be 1.3
    x = 1.300
    if r+x >= 2.375:
        return 2.375
    return r+x

def primeRate(r):
#x is to be set to the variable... should be -2.750
    x = 2.750
    return r-x


# UA
bh = {"User-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0"}

# URL to table details
urla = "https://rbwm-api.hsbc.com.hk/digital-pws-tools-hibor-eapi-prod-proxy/v1/hibor?year="
qa = [0]
ra = requests.get(urla, headers=bh)
for a in ra.json()["rateTable"][0].values():
    qa.append(a)

dly = countRate(float(qa[2]))

print("-----HIBOR Rate-----")

print("Date: {}\nHibor: {:.3f} + 1.300 = {:.3f}\nRate: {:.3f}%\n".format(qa[1], float(qa[2]), float(qa[2])+1.300,dly))

print("-----Prime Rate-----")

qb = [0]
pb = [0]
urlb = "https://www.hsbc.com.hk/investments/market-information/hk/lending-rate/"
rb = requests.get(urlb, headers = bh)

soup = BeautifulSoup(rb.text, 'lxml')
for th in soup.findAll("th"):
    qb.append(th.get_text())

for ok in soup.findAll("td"):
    pb.append(ok.get_text())

print("Date: {}\nPrime: {:.3f}- 2.750%\nRate: {:.3f}%".format(pb[1], float(pb[2].replace(" ", "").replace("%","")), primeRate(float(pb[2].replace(" ", "").replace("%","")))))