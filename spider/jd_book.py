#!/usr/bin/python
# coding: utf-8

import requests
from bs4 import BeautifulSoup

url = "https://list.jd.com/list.html?cat=1713,3267,3466&page=1&sort=sort_totalsales15_desc&trans=1&JL=4_2_0#J_main"

content = requests.get(url)

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/   bs4 doc
# get all div class=p-name element
soup = BeautifulSoup(content.text, 'lxml')
# value = soup.findAll("div", class_="p-name")
#
# for elm in value:
#     title = elm.a.text.strip()
#     print(title)

# value = soup.findAll("div", id="plist")[0].ul.li.div
# print(value)


# product detail
url = "https://item.jd.com/12238283.html"
content = requests.get(url)
soup = BeautifulSoup(content.text, 'lxml')
print(soup)
