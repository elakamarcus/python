
"""
Physics news feed

Intention is to feed into self-scrolling window for awesome effects.

TODO:
    1. Review XML to identify which tags are interesting
    2. Fetch site and grab out the 
        1. Title
        2. Description, e.g. brief summary of the news
        3. URL
    3. Formatting to match the self-scrolling w/e for awesome effects.

    1-2 = completed.

"""

from bs4 import BeautifulSoup
import requests
import lxml

# set the url to fetch xml feed
url = "https://phys.org/rss-feed/" 

# set UA
rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}

# fetch the site
r = requests.get(url, headers = rh)

# let bs4 use xml to parse. lxml don't handle self-closing tags well
soup = BeautifulSoup(r.text, "xml")

if r.status_code == 200: # just verify successful only connections..
    # loop through articles, the tag is called item
    for article in soup.findAll("item"):
        title = article.find("title").text # title of the news
        description = article.find("description").text # brief information
        links = article.find("link").text # link to full article
        # print it all..
        print("Title: {}\nBrief: {}\nURL: {}\n".format(title, description, links))
else:
    print("Unable to make the connection. Quit.")

