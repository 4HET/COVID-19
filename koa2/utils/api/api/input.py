import requests
import json

url = 'https://c.m.163.com/ug/api/wuhan/app/index/input-data-list?t=330298515687'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'origin': 'https://wp.m.163.com',
    'referer': 'https://wp.m.163.com/'
}

data = requests.get(url=url, headers=headers).json()
print(data)
print(data['data'])

all = []
for i in data['data']['list']:
    if i['target'] == '上海':
        all.append({"source": i['source'], "data": i['value']});

fp = open('./data/input.json', 'w', encoding='utf-8')
json.dump(all, fp=fp, ensure_ascii=False)