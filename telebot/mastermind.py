import requests
from bs4 import BeautifulSoup

def get_response(msg):
    url = "https://www.worldometers.info/coronavirus/#count"
    resp=requests.get(url)
    print(resp.status_code)
    soup=BeautifulSoup(resp.text, 'html.parser')
    l=soup.find("div", {"class":"maincounter-number"})
    y=l.span.text
    return y