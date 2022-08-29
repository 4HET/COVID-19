# -*- coding:utf-8 -*-
import jieba

import json

import requests
import re

url = 'https://top.baidu.com/board?tab=realtime'


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
}

data = requests.get(url=url, headers=headers).text
with open('index.html','w', encoding='utf-8') as f:
    f.write(data)
data_list = re.findall('</div> <div class="hot-index_1Bl1a"> (.*?) </div> <div class="text_1lUwZ"> 热搜指数 </div> </div> <img class="line_3-bzA" src=".*?"> <div class="content_1YWBm"> <a href=.*?> <div class="c-single-text-ellipsis">  (.*?) </div>', data, re.DOTALL)

# ed = []
# for i in data_list:
#     ed.append({'name': i[1], 'value': i[0]})
# print(data_list)
data_dir = {}
for i in data_list:
    name,value = i[1],int(i[0])
    t = jieba.lcut(name)
    for j in t:
        if len(j)>1:
            if(j in data_dir.keys()):
                data_dir[j]+=value
            else:
                data_dir[j] = value
# print(data_dir)
data_dir = sorted(data_dir.items(),key=lambda x:x[1],reverse=True)
print(data_dir)
data_final = []
# for key,val in data_dir.items():
n = 80
cnt = 0
for i in data_dir:
    if cnt>=n:
        break
    # print(i)
    key = i[0]
    val = i[1]
    data_final.append({'name':key,'value':val})
    cnt+=1
# print(data_final)
fp = open('./data/wordCloud.json', 'w', encoding='utf-8')
json.dump(data_final,fp=fp,ensure_ascii=False)


