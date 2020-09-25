#-*- coding=utf-8 -*-
#豆瓣动画片 简介

import requests
import re
import wget
import time
import os

print('可下载国家/地区')
country_list=['全部地区','中国大陆','欧美美国','中国香港','中国台湾','日本','韩国','英国','法国','德国','意大利','西班牙','印度','泰国','俄罗斯','伊朗','加拿大','澳大利亚','爱尔兰','瑞典','巴西','丹麦']
for i in range(len(country_list)):
    str_i=str(i+1)
    print(str_i+'.'+country_list[i])
print('--------分割线--------')
I=input('请输入想下载动漫的国家名：') #大写的I

i=int(I)-1
os.mkdir(country_list[i])

for page in ['0','20']:
    url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=动漫&start='+page+'&genres=动画&countries='+country_list[i]
    head={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    response=requests.get(url,headers=head)
    text=response.text
    # print(text)

    r1='"title":"(.*?)".*?"cover":"(.*?)"'
    result=re.findall(r1,text,re.S)
    # print(result)


    for a in range(len(result)):
        time.sleep(0.5)
        b=list(result[a])
        name=b[0]+'.jpg'            #wget 重命名文件名
        b[1]=b[1].replace('\\','')
        name2=country_list[i]+'\\'+name
        wget.download(b[1],out=name2)
        print('正在下载封面图片：',name)
        # img=Image(name)           #Excel 原来不能插入图片....


input("please input any key to exit!")