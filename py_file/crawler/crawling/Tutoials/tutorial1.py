import requests
from bs4 import BeautifulSoup

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'http://gsm.hs.kr' + str(page)# http://creativeworks.tistroy.com/
        souce_code = requests.get(url)
        plain_text = souce_code.text
        soup = BeautifulSoup(plain_text,'lxml')
       
