#!/bin/python3

"""
TODO: 
1. Make a function for each feed
    a. Physics - done
    b. apnews or rtnews
        1. rtnews - done
        2. rtxxyy
        3. rtyyxx
        4. ap
    c. local news
2. Save to text or save to DB?
3. Create html template for the news
4. PHP script to push

"""

from bs4 import BeautifulSoup
import requests
import lxml

def writeToFile(filename, title, description, links):
    print("in writeToFile")
    if(filename and title and description and links):
        try:
            fout = open(filename, "w")
            fout.write(title + '\n' + description + '\n' + links + '\n')
            fout.close()
        except:
            print("Unable to open target file.")
    else:
        print("Parameters empty.")


def fetchnews(section, url):
    rh = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    # fetch the site
    r = requests.get(url, headers = rh)
    # let bs4 use xml to parse. lxml don't handle self-closing tags well
    soup = BeautifulSoup(r.text, "xml")
    # verify http code
    if r.status_code == 200:
        # loop through articles, the tag is called item
        for article in soup.findAll("item"):
            title = article.find("title").text # title of the news
            description = article.find("description").text # brief information
            links = article.find("link").text # link to full article
            #print("Title: {}\nBrief: {}\nURL: {}\n".format(title, description, links))
            # write to file  
            writeToFile(section, title, description, links)       
    else:
        print("Unable to connect. Error code: {}".format(r.status_code))    


def rtnewsFeed():
    print("in rtNews")
    url = "https://www.rt.com/rss/news/"
    fetchnews("rtnews", url)


def physOrgFeed():
    print("In Physics org feed")
    url = "https://phys.org/rss-feed/"
    fetchnews("physics", url)
