import requests
from lxml import etree
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# name = '华硕 VivoBook S400CA'


def get_pid(name):
    url = 'https://www.aihuishou.com/product/search?keyword='
    url = url+name
    r = requests.get(url,headers=headers)
    html = etree.HTML(r.text)
    pid = '6666666666666'
    s = name
    try:
        s = html.xpath('//*[@id="body"]/div[4]/ul/li[1]/a/@title')[0]
        a_href = html.xpath('//*[@id="body"]/div[4]/ul/li[1]/a/@href')[0]
        pid = re.findall('\d+',a_href)[0]
    except Exception as e:
        print('解析错误',e)
    if name in s:

        return pid
    else:
        return '6666666666666'

path = r'D:\wpx\workspace\Love_recycling\tools\spider_item'
pid_path=r'D:\wpx\workspace\Love_recycling\tools\spider_item_pid.txt'
p_names = []
with open(path,'r',encoding='utf-8') as fp:
    while True:
        text_line = fp.readline()
        if text_line:
            text_line = text_line.strip('\n')
            p_names.append(text_line)
        else:
            break
res_id = []
for nam in p_names:
    with open(pid_path, 'a', encoding='utf-8') as f:
        pid = get_pid(nam)
        res_id.append(pid)
        print(pid)
        items = pid+"---------------"+nam
        print(items)
        f.write(items+'\n')
print(res_id)

