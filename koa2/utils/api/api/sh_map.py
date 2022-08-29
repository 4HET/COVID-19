import requests
import json
url = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'
}

params = {
    'modules': 'statisGradeCityDetail,diseaseh5Shelf'
}
response_data = requests.post(url,headers=headers, params=params).json()

areaTree_data = response_data['data']['diseaseh5Shelf']

# print(areaTree_data)
# fp = open('inform.json', 'w', encoding='utf-8')
# json.dump(areaTree_data, fp=fp, ensure_ascii=False)

# print(areaTree_data.keys())
# print(areaTree_data['areaTree'][0]['children'])
all = []
dl = ['境外输入','外地来沪','境外来沪','地区待确认']
for i in areaTree_data['areaTree'][0]['children']:
    # print(i['name'])
    if i['name'] == '上海':
        # print(i)
        for j in i['children']:
            if j['name'] in dl:
                continue
            # print(j['name'], j['today']['confirm'])
            if j['name'] == '浦东':
                name = j['name'] + '新区'
            else:
                name = j['name'] + '区'
            all.append({'name': name, 'value': j['today']['confirm']})
        break
    # print(i['today']['confirm'])

#
fp = open('./data/sh_map.json', 'w', encoding='utf-8')
json.dump(all, fp=fp, ensure_ascii=False)
