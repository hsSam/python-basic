#!/usr/bin/python
# encoding: utf-8
# douban top 100 movie

import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {'Host': 'movie.douban.com',
               'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

    movie_list = []
    for findex in range(0, 3):
        web_index = 25 * findex
        url = 'https://movie.douban.com/top250?start=' + str(web_index)
        r = requests.get(url, headers=headers)
        print(r.url)
        print(r.status_code)


        soup = BeautifulSoup(r.text, 'lxml')
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)

    return movie_list


movie_list = get_movies()
print(len(movie_list))
print(movie_list)



