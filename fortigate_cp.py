import requests as req
from urllib.parse import urlparse
import re
from bs4 import BeautifulSoup

username=''
password=''

f = req.request('GET','http://example.com').content.decode()
# print(f)
token_url= re.findall("\"(https:.*?)\"",f)[0]
# print(token_url)


f = req.request('GET', token_url).content.decode()
# print(f)

b=BeautifulSoup(f,'html.parser')
payload= ""

for i in b.find_all('input'):
    if i.get('name') not in ['','username','password']:
        payload += str(i.get('name')) + '=' + str(i.get('value')) + '&' 
payload += 'username' + '=' + username + '&'
payload += 'password' + '=' + password
# print(payload)

headers = {}
headers['Referer'] = token_url


url=urlparse(token_url)
try:
    finish = req.request('POST', url.scheme+"://"+url.netloc, data=payload.encode(), headers=headers).content.decode()
except BaseException:
    print("this is beta")
# print(finish)
    
