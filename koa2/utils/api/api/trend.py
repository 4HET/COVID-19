import requests
import json
import time

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=jQuery341026745307075030955_1584946267054&_=1584946267055'
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}
res = requests.get(url,headers=headers)
# print(res.text)
response_data = json.loads(res.text.replace('jQuery341026745307075030955_1584946267054(','')[:-1])
# print(response_data)
chinaDayList = eval(response_data['data'])['chinaDayList']#历史记录
chinaDayAddList = eval(response_data['data'])['chinaDayAddList']#历史新增记录
# print(chinaDayList)
# print(chinaDayAddList)
history = {}
for i in chinaDayList:
    ds = '2022.' + i['date']#时间
    tup = time.strptime(ds,'%Y.%m.%d')
    ds = time.strftime('%Y-%m-%d',tup)#改变时间格式，插入数据库
    confirm = i['confirm']
    suspect = i['suspect']
    heal = i['heal']
    dead = i['dead']
    history[ds] = {'confirm':confirm,'suspect':suspect,'heal':heal,'dead':dead}
for i in chinaDayAddList:
    try:
        ds = '2022.' + i['date']#时间
        tup = time.strptime(ds,'%Y.%m.%d')
        ds = time.strftime('%Y-%m-%d',tup)#改变时间格式，插入数据库
        confirm_add = i['confirm']
        suspect_add = i['suspect']
        heal_add = i['heal']
        dead_add = i['dead']
        history[ds].update({'confirm_add':confirm_add,'suspect_add':suspect_add,'heal_add':heal_add,'dead_add':dead_add})
    except:
        pass
# print(history)
fp = open('./data/trend.json', 'w', encoding='utf-8')
json.dump(history, fp=fp, ensure_ascii=False)