import requests
from bs4 import BeautifulSoup

res = requests.get("http://itech.net.br/")
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, 'html-parser')
print (soup)