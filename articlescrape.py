import requests
from bs4 import BeautifulSoup
import lxml
import sys
from unidecode import unidecode
import datetime

f = open("bajsfil", "a")

rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

for url in open("newsURLs", "r"):
    r = requests.get(url, headers = rh)
    soup = BeautifulSoup(r.text, "lxml")
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")

    if not title["content"]:
        title["content"] = "N/A"
    if not description["content"]:
        description["content"] = "N/A"
    print "<div class=\"title\">" + title["content"].encode('ascii', 'ignore') + "</div>" + '\n'
    print "<div class=\"description\">" + description["content"].encode('ascii', 'ignore') + "</div>" + '\n'
    print "<div class=\"lank\">" + url + "</div>" + "</p>" + '\n'

## manually, the above and below works very well. But when running the script, something gives out a NoneType error....


#   troubleshooting block
#
#    try:
#        title = unidecode(title["content"])
#    except:
#        title = unidecode(title)
#    try:
#        description = unidecode(description["content"])
#    except:
#        description = unidecode(description)
#

#
#     f.write('\n' + "<p>" +
#        "<div class=\"title\">" + title + "</div>" + '\n' +
#        "<div class=\"description\">" + description + "</div>" + '\n' +
#        "<div class=\"lank\">" + url + "</div>" + "</p>" + '\n')
#

f.close()