import requests
from bs4 import BeautifulSoup
import wget
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def amir(url):
    link=[]
    r=requests.get(url=url, headers=headers)
    soup=BeautifulSoup(r.content, features="html.parser")
    div_class=soup.find("div",{"class":"GalleryItems-module__searchContent___DbMmK"})
    pic=div_class.find_all("a")
    for i in pic:
        link.append((i.text,i['href']))
    return link

def image_download(imgurl):
    r=requests.get(url=imgurl,headers=headers)
    soup=BeautifulSoup(r.content, features="html.parser")
    image_div=soup.find("img",{"class":"AssetCard-module__image___dams4"})
    x= image_div['src']
    print(x, "\n")
    return x

def main():
    links=amir("https://www.gettyimages.in/photos/aamir-khan-actor")
    head="https://www.gettyimages.in"
    for name, link in links:
        wget.download(image_download(head+link))

if __name__=="__main__":
    main()
