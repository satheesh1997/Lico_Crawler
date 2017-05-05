import requests

from bs4 import BeautifulSoup


def crawler(url):
    src = requests.get(url)
    plain_text = src.text
    soup = BeautifulSoup(plain_text)
    title = soup.find('title')
    title_h = title.string
    fw = open(r"crawled/"+title_h+".txt", "w")
    print("TITLE : " + title_h)
    for meta in soup.findAll('meta'):
        metaname = meta.get('property')
        metacontent = meta.get('content')
        print(metaname, ":", metacontent)
        if str(metaname) != "None":
            fw.write(str(metaname) + " | " + str(metacontent) + "\n")
    fw.close()


crawler('http://yahoo.in')