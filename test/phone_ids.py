# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

import json
url = 'https://www.aihuishou.com/shouji/b9'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.text,'lxml')
# data
# for s in soup.find_all('a',class_='page'):
#     print(trs.string)
