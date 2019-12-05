# -*- coding:utf-8 -*-

import requests, bs4

res = requests.get('http://oscar-lab.org/puzzle.html')

soup = bs4.BeautifulSoup(res.text, features='lxml')

# print(soup)
keys = ['0', '1', '2']
news = []
for tr in soup.body.table.find_all('tr'):
    tds = [td for td in tr.find_all('td')]
    if len(tds) != 3:
        continue
    # print(len(tds))
    news_dict = {keys[0]:tds[0].text, keys[1]:tds[1].text, keys[2]:tds[2].find('a')['href']}
    news.append(news_dict)
    
print(news)