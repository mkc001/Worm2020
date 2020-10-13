import requests
from bs4 import BeautifulSoup
from urllib import request
from urllib.request import urlopen, Request
import urllib
import re
import bs4
from bs4 import BeautifulSoup
from http import cookiejar
import json
import requests


def main():
    url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
    url = 'https://movie.douban.com/mine?status=collect'
    ua_headers = { "User-Agent":'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    data = {
        'ck': '',
        'name': '15052525093',
        'password': '970927aaa',
        'remember': 'false',
        'ticket': ''
    }

    s = requests.session()
    s.post(url=url_basic, headers=ua_headers, data=data)
    response = s.get(url=url, headers=ua_headers)

    #req1 = Request(url=url, headers=ua_headers)
    #contents = urlopen(req1).read()
    #soup = BeautifulSoup(contents, "html.parser")
    soup = BeautifulSoup(response.text,'html.parser')
    #print(response.text)
    #print(soup)
    #with open('douban.html' , 'wb') as f:
        #f.write(response.content)

    for tag in soup.find_all('div', class_='info'):
        #m_name = tag.find('li', class_='title').get_text()
        m_name = tag.find('em')
        #m_name = str(m_name).replace("em","")
        #print(type(m_name))
        #m_rating_score = float(tag.find('span', class_='rating_num').get_text())
        #m_people = tag.find('div', class_="star")
        #m_span = m_people.findAll('span')
        #m_peoplecount = m_span[3].contents[0]
        m_url = tag.find('a').get('href')
        m_comment = tag.find('span', class_="comment")
        print("片名：" + str(m_name) + "评论" + str(m_comment) + "连接" + str(m_url))

if __name__ == '__main__':
    main()