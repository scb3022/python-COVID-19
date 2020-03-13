from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import os
import sys

while True:
    response = urlopen('https://coronamap.site/')
    soup = BeautifulSoup(response, 'html.parser')
    for Confirmed in soup.select('body > div:nth-child(8) > div.content > div'):
        print('확진자 :',Confirmed.get_text())
    
    for Recovered in soup.select('body > div:nth-child(8) > div.content1.clear > div:nth-child(1) > div:nth-child(2)'):
        print('완치 :',Recovered.get_text())
    
    for Deaths in soup.select('body > div:nth-child(8) > div.content1.clear > div:nth-child(3) > div:nth-child(2)'):
        print('사망자 :',Deaths.get_text())
        
    time.sleep(43200)

    
