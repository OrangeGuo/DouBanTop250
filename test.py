#encoding=utf8
import requests
from bs4 import BeautifulSoup
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
headers = {
      'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r=requests.get('http://movie.douban.com/subject_search?',params={'search_text':"杀手",'cat':'1002'},headers=headers)
bs = BeautifulSoup(r.text,"lxml")
print(r.url)

content = BeautifulSoup(r.text)
print(content)