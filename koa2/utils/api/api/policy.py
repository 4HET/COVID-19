import requests
import re
import json
url = 'https://wsjkw.sh.gov.cn/xwfbh/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'Referer': 'https://wsjkw.sh.gov.cn/yqfk2020/index.html'
}
data = requests.get(url=url, headers=headers).text

print(data)

data_begin = re.findall('<ul class="uli16 nowrapli list-date ">(.*?)</ul>', data, re.DOTALL)
print(data_begin)
url_b = 'https://wsjkw.sh.gov.cn/xwfbh/'
data_list = re.findall('<li><a href="/xwfbh/(.*?)" title=".*?" target="_blank">(.*?)</a><span class="time">.*?</span></li>', data_begin[0], re.DOTALL)

print(data)
print(data_list)

all = []
for i in data_list:
    all.append({"name": i[1], "utl": url_b + i[0]})

fp = open('./data/policy.json', 'w', encoding='utf-8')
json.dump(all, fp=fp, ensure_ascii=False)