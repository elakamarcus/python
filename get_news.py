#!/bin/python3

"""
TODO: 
1. Make a function for each feed
    a. Physics
    b. apnews or rtnews
    c. local news
2. Save to text or save to DB?
3. Create html template for the news
4. PHP script to push

"""

from bs4 import BeautifulSoup
import requests
import lxml

# Very unnice global vars. Consider make a class or function for fetching...
rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}


def physOrgFeed():
    url = "https://phys.org/rss-feed/"
    # fetch the site
    r = requests.get(url, headers = rh)
    # let bs4 use xml to parse. lxml don't handle self-closing tags well
    soup = BeautifulSoup(r.text, "xml")
    try:
        fout = open("articles.lst", "w")
        # verify http code
        if r.status_code == 200:
            # loop through articles, the tag is called item
            for article in soup.findAll("item"):
                title = article.find("title").text # title of the news
                description = article.find("description").text # brief information
                links = article.find("link").text # link to full article
                #  print it all..
                # print("Title: {}\nBrief: {}\nURL: {}\n".format(title, description, links))
                # write to file
                fout.write(title + '\n' + description + '\n' + links + '\n')
        else:
            print("Unable to connect. Error code: {}".format(r.status_code))
    except:
        print("Unable to open target file.")

def rtnewsFeed():
    url = "https://www.rt.com/rss/news/"
    # fetch the site
    r = requests.get(url, headers = rh)
    # let bs4 use xml to parse. lxml don't handle self-closing tags well
    soup = BeautifulSoup(r.text, "xml")
    try:
        fout = open("articles.lst", "w")
        # verify http code
        if r.status_code == 200:
            # loop through articles, the tag is called item
            for article in soup.findAll("item"):
                title = article.find("title").text # title of the news
                # Description here contains some HTML...
                description = article.find("description").text # brief information
                links = article.find("link").text # link to full article