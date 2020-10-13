# coding:utf-8
'''''
@author: jsjxy
'''
from urllib import request
from urllib.request import urlopen, Request
import urllib
import re
from bs4 import BeautifulSoup
from http import cookiejar
import json
import requests
from distutils.filelist import findall


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        """
        只要检查到了是bytes类型的数据就把它转为str类型
        :param obj:
        :return:
        """
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


url =  'https://accounts.douban.com/login'
data={
    'name':'15052525093',
    'password':'970927aaa'
}
header = {
"user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",
"Accept":"application/json",
"Accept-Language":"zh-CN,zh;q=0.9",
"Connection":"keep-alive",
"origin":"https://accounts.douban.com",
"Referer":"https://accounts.douban.com/passport/login",
"Cookie":"_vwo_uuid_v2=D1DCEA72F0F2A9F58DF60FE7DAE701921|67e341e733df5c76d769738ba9dca794; douban-fav-remind=1; gr_user_id=aba737ca-05f5-4fc3-a1f7-04016ea50d10; __gads=ID=6d2bf5559a111c54:T=1557713544:S=ALNI_MZeC-4HGXcfM1idxdooYItf7MSlhg; viewed='1070729_3435711'; bid=JRi9gZNqryE; ll='118168'; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18247; douban-profile-remind=1; ap_v=0,6.0; __utmc=30149280; apiKey=; _pk_ref.100001.2fad=%5B%22%22%2C%22%22%2C1584519951%2C%22https%3A%2F%2Fmovie.douban.com%2Ftop250%3Fformat%3Dtext%22%5D; _pk_ses.100001.2fad=*; last_login_way=account; __utma=30149280.83859530.1580802263.1584517203.1584520839.12; __utmb=30149280.0.10.1584520839; __utmz=30149280.1584520839.12.10.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login; _pk_id.100001.2fad=905e4c80c0e4498e.1583400712.2.1584521174.1583400824.; login_start_time=1584521176789",
"Content-Type":	"application/x-www-form-urlencoded",
"TE":"Trailers","X-Requested-With":"XMLHttpRequest"
}
postdata = urllib.parse.urlencode(data).encode('utf8')

cookie = cookiejar.CookieJar()
#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
cookie_support = request.HTTPCookieProcessor(cookie)
 #通过CookieHandler创建opener
opener = request.build_opener(cookie_support)

req1 = Request(url=url, data=postdata, headers=header)
contents = urlopen(req1)
response1 = opener.open(req1)

ret = Request(url,data=data,headers=header)
#response1 = opener.open(req1)
#page = urllib.request.urlopen('http://movie.douban.com/top250?format=text',headers=header)
#contents = page.read()
response=requests.post(url,data=json.dumps(postdata,cls=MyEncoder), headers=header)

#print(response.text)
soup = BeautifulSoup(contents, "html.parser")
print(type(soup))
print("豆瓣电影TOP250" + "\n" + " 影片名              评分       评价人数     链接 ")
for tag in soup.find_all('div', class_='info'):
    # print tag
    m_name = tag.find('span', class_='title').get_text()
    m_rating_score = float(tag.find('span', class_='rating_num').get_text())
    m_people = tag.find('div', class_="star")
    m_span = m_people.findAll('span')
    m_peoplecount = m_span[3].contents[0]
    m_url = tag.find('a').get('href')
    print(m_name + "        " + str(m_rating_score) + "           " + m_peoplecount + "    " + m_url)