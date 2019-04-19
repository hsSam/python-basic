#!/usr/bin/python
# coding: UTF-8

import requests
from bs4 import BeautifulSoup

link = "http://www.santostang.com/"

headers = {'User-Agent': ''}

r = requests.get(link, headers = headers)
soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h1", class_="post-title").a.text.strip()
print(title)

with open('title.xtx', "a+") as f:
    f.write(title)
    f.close
