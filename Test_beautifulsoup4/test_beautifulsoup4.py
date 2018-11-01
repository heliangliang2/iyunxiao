#coding:utf-8
from bs4 import BeautifulSoup
import requests
import os
# r=requests.get("https://www.qiushibaike.com/")
# #请求首页后获取整个html界面
# blog=r.content
# # print (blog)
# soup=BeautifulSoup(blog,"html.parser")
# #获取所有的class属性为daytime ,返回tag类
# duanzi=soup.find_all(class_="content")
# for i in duanzi:
#     print (i.span.contents[0])#获取a标签的文本



#获取照片
# r=requests.get("http://699pic.com/sousuo-218808-13-1.html")
# s=r.content
# soup=BeautifulSoup(s,"html.parser")
# images=soup.find_all(class_="lazy")
# for i in  images:
#     try:
#         jpg_rl=i["data-original"]
#         title=i["title"]
#         print (title)
#         print (jpg_rl)
#         #保存图片
#         with open (os.getcwd()+"\\jpg\\"+title+'.jpg',"wb") as f:
#             f.write(requests.get(jpg_rl).content)


#contents
# r=requests.get("http://www.cnblogs.com/yoyoketang/")
# #获取整个页面
# blog=r.content

# #用HTML。parser解析
# soup=BeautifulSoup(blog,"html.parser")

# #find找到属性匹配的对象
# tag_soup=soup.find(class_="c_b_p_desc")
#len函数获取子节点的个数
# print (len(tag_soup.contents))

# #打印子节点
# for i in tag_soup.contents:
#     print (i)
# #通过下标取出第一个string 子节点
# print (tag_soup.contents[0])

# #获取下标取出第二个子节点
# print(tag_soup.contents[1])


#len函数获取子节点的个数
# print (len(list(tag_soup.children)))

# #获取子孙节点的个数
# print (len(list(tag_soup.descendants)))

# for i in tag_soup.descendants:
#     print (i) 
#     print ("------------")

r=requests.get("http://www.cnblogs.com/yoyoketang/mvc/blog/sidecolumn.aspx?blogApp=yoyoketang")
s=r.content

#用html.parser解析整个界面
# soup=BeautifulSoup(s,"html.parser")
# tag_soup=soup.find(class_="catListTag")
# ul_soup=tag_soup.find_all("a")
# print (ul_soup)

# for i in ul_soup:
#     print  (i.string)

import xlrd

#打开exlcel表格
data=xlrd.open_workbook("D:\\test1\\Test_beautifulsoup4\\11111.xlsx")
#table=data.sheets()[0]
#table=data.sheet_by_index(0)

table=data.sheet_by_name(u'Sheet1')#通过名称获取
nrows=table.nrows#获取总行数
ncols=table.ncols#获取总列数

print  (table.row_values(0))#获取第一行值
print  (table.col_values(0))#获取第一列值


