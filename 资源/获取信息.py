#!/usr/bin/env python
# -*- coding: utf-8 -*-
#引入开发包
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
#使用geopy查询
def geocodeN(address):
    gps=Nominatim()
    location=gps.geocode(address)
    return location.longitude,location.latitude
resp=urlopen("http://www.tcmap.com.cn/hainan/").read()
#使用BeautifulSoup进行解析
soup=BeautifulSoup(resp,"html.parser")
listUrls=soup.findAll("a",href=re.compile(".+zhen\.html"))
file=open("海南省所有镇的经纬度.txt","w")
for url in listUrls:
    #string只能获取一个 get_text()获取标签下所有的文字
    try:
        longitude,latitude=geocodeN("海南省"+url.get_text())
        print("海南省"+url.get_text()+','+str(longitude)+','+str(latitude))
        file.write("海南省"+url.get_text()+','+str(longitude)+','+str(latitude)+'\n')
    except:
        pass
file.close()
#文件最后的空行一定要删除！！！