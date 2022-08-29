import requests
import json
import re

news = []

for page in range(1,5):
    url = 'https://interface.sina.cn/wap_api/wap_std_subject_components_list.d.json?url=https://news.sina.cn/zt_d/feiyan1231&page={}&callback=__jp0'.format(str(page))

    data_json = requests.get(url=url).text
    data = re.findall('__jp0\((.*?)\)', data_json)[0]

    # print(json.loads(data)['result']['data']['components'])

    dit = json.loads(data)['result']['data']['components']
    if dit == []:
        break

    # fp = open('inform.json', 'w', encoding='utf-8')
    # json.dump(dit, fp=fp, ensure_ascii=False)

    for i in dit:
        if i['type'] == 'wap_zt_std_theme_feed':
            # print(i['data'])
            # fp = open('news.json', 'w', encoding='utf-8')
            # json.dump(i['data'], fp=fp, ensure_ascii=False)
            for j in i['data']:
                try:
                    # print(j['url'], j['title'])
                    news.append({'news':  j['title'], 'url':j['url']})
                except:
                    pass

# print(news)
fp = open('./data/news.json', 'w', encoding='utf-8')
json.dump(news, fp=fp, ensure_ascii=False)
fp.close()