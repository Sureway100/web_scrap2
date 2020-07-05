import bs4

from urllib.request import urlopen as ureq

from bs4 import BeautifulSoup as soup

my_url = 'https://coreyms.com'


uclient = ureq(my_url )

page_html = uclient.read()
uclient.close()

page_soup = soup (page_html, "html.parser")

containers = page_soup.findAll("article")

container = containers[0]

filename = "webscrap.csv"

f = open(filename, "w")

headers = "headline, summary, link \n"

f.write(headers)

for container in containers:

    head = container.find("h2", {"class" : "entry-title"})
    headline = head.a.text


    xum = container.find("div", {"class" : "entry-content"})
    summary = xum.p.text


    try:
        view = container.find("iframe", {"class":"youtube-player"})
        link = view['src']
    except:
        pass


        
    print( "headline: " +  headline)
    print( "summary: " +  summary)
    print( "link: " +  link)

    f.write(headline + "," + summary + "," + link + "\n")

f.close()

