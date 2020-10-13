# coding:utf-8
'''''
@author: jsjxy
'''

from urllib.request import urlopen, Request
import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall


header = {
"user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
}
ret = Request('https://www.caiku.cc/yanshi/23536/')
contents = urlopen(ret)
#page = urllib.request.urlopen('http://movie.douban.com/top250?format=text',headers=header)
#contents = page.read()
# print(contents)
soup = BeautifulSoup(contents, "html.parser")
#print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")

for tag in soup.find_all('div', id='light'):
    # print tag
    color = tag.find('a', class_='super button pink').get_text()

    #print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)
    print(color)