# -*- encoding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib
import re

loginUrl = 'http://accounts.douban.com/login'
formData = {
    "redir": "http://movie.douban.com/mine?status=collect",
    'name': '15052525093',
    'password': '970927aaa',
    'remember': 'false',
    'ticket': ''
}
headers = {"user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",}
r = requests.post(loginUrl, data=formData, headers=headers)
page = r.text
# print r.url

'''获取验证码图片'''
# 利用bs4获取captcha地址
soup = BeautifulSoup(page, "html.parser")
#captchaAddr = soup.find('img', id='captcha_image')['src']
# 利用正则表达式获取captcha的ID
#reCaptchaID = r'<input type="hidden" name="captcha-id" value="(.*?)"/'
#captchaID = re.findall(reCaptchaID, page)
# print captchaID
# 保存到本地
#urllib.urlretrieve(captchaAddr, "captcha.jpg")
#captcha = raw_input('please input the captcha:')

#formData['captcha-solution'] = captcha
#formData['captcha-id'] = captchaID

r = requests.post(loginUrl, data=formData, headers=headers)
#page = r.text
print(r.url)
if r.url == 'http://movie.douban.com/mine?status=collect':
    print('Login successfully!!!')
    print('我看过的电影', '-' * 60)
    # 获取看过的电影
    soup = BeautifulSoup(page, "html.parser")
    result = soup.findAll('li', attrs={"class": "title"})
    # print result
    for item in result:
        print(item.find('a').get_text())
else:
    print("failed!")
