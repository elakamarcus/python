## HSBC HK Hibor rate
import requests
from bs4 import BeautifulSoup

def countRate(r):
#x is to be set to the variable...
    x = 1.300
    if r+x >= 2.375:
        return 2.375
    return r+x

# UA
bh = {"User-agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0"}

# URL to table details
url = "https://rbwm-api.hsbc.com.hk/digital-pws-tools-hibor-eapi-prod-proxy/v1/hibor?year="
q = [0]
r = requests.get(url, headers = bh)
for a in r.json()["rateTable"][0].values():
    q.append(a)

dly = countRate(float(q[2]))

print("Date: {}\nHibor: {:.3f} + 1.300 = {}\nRate: {}%".format(q[1], float(q[2]), float(dly)+1.300,dly))

## TODO:
## get the prime rate as well, P+y
