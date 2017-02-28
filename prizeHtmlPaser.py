from prizeModel import *
import requests
from bs4 import BeautifulSoup


def parse2Pirze(plist):
    prizeList=list()
    for d in plist:
        prizeList.append(dict2Prize(d))
    return prizeList

import urllib.request
prizeList=list()
response = requests.get("http://caipiao.163.com/award/ssq/")
soup = BeautifulSoup(response.text)
for x in soup.findAll("a"):
    if x.get('time','Not') != 'Not':
       x['id']=x.text
       prizeList.append(x)

prizes=parse2Pirze(prizeList)
print('prize len:',len(prizes))
print(prizes)
