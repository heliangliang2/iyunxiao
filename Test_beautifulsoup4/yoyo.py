#coding:utf-8
from  bs4 import BeautifulSoup
yoyo=open("D:\\test1\\Test_beautifulsoup4\\result.html")
print(type(yoyo))
soup=BeautifulSoup(yoyo,"html.parser")
print(soup.prettify())