import urllib.request, json
from bs4 import BeautifulSoup

def get_response():
    url = "https://api.covid19api.com/summary"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    for x in  data['Countries'][101]:
        return x

