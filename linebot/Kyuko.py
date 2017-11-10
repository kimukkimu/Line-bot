import requests
from bs4 import BeautifulSoup


def Kyuko():
    res = requests.get('https://duet.doshisha.ac.jp/kokai/html/fi/fi050/FI05001G.html')
    bsObj = BeautifulSoup(res.text, "html.parser")
    table = bsObj.select("table tr td")
    txt = ""
    for e in table:
        txt += e.text
    return txt

