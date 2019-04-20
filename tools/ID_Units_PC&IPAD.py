#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
from mysetting import phone_path,n,pid
import re


def get_data_ids(url):
    info = get_base_infos(url, num)
    info_list = []
    # print(info)
    if info != None:
        for q in info:
            for k in q:
                if k not in info_list:
                    info_list.append(k)

    # print('info_list:%s'%info_list)

    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    data_id_all = html.xpath(r'//div[contains(@class, "select-property")]/dl')
    data_ids = []  # 所有id

    for data_id in data_id_all:
        data_ids_all = data_id.xpath(r'./dd/ul/li/@data-id')
        for n in range(len(data_ids_all)):
            if '%s' % data_ids_all[n] not in info_list:
                if data_ids_all not in data_ids:
                    data_ids.append(data_ids_all)

    for i in data_ids:
        if i == []:
            data_ids.remove(i)
    # print(data_ids)
    return data_ids


def get_base_infos(url, num):  # 基本信息组合列表
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        html = etree.HTML(r.text)

        base_infos_str = str(html.xpath('//*[@id="group-property"]/@data-sku-property-value-ids')[0])
        if base_infos_str == '[[]]':
            return None
        else:
            base_infos_lst = re.findall('\d+', base_infos_str)

            # n = len(html.xpath('//div[@class="select-property base-property"]/dl'))
            n = num

            base_infos = [base_infos_lst[i: i + n] for i in range(0, len(base_infos_lst), n)]

            # print(len(base_infos))
            return base_infos

    else:
        print(r.status_code)
        return None


def generate_id_groups(data_ids, dd):
    id_groups = []

    for i in range(len(data_ids)):

        if i == 0:
            n = 1
            lst = [data_ids[i]]
            while n < len(data_ids):
                if n != len(data_ids) - 1:
                    if data_ids[n][0] == '%s' % dd:
                        lst.append([data_ids[n][1]])
                    else:
                        lst.append([data_ids[n][0]])
                else:
                    break
                n += 1

            id_groups.append(lst)

        elif i < len(data_ids) - 1:
            n = 1
            m = 1
            lst = []

            if data_ids[i][0] == '%s' % dd:
                lst += [data_ids[i][0:]]
            else:
                lst += [data_ids[i][1:]]

            while n - 1 < i:
                if data_ids[n - 1][0] == '%s' % dd:
                    lst.insert(n - 1, [data_ids[n - 1][1]])
                else:
                    lst.insert(n - 1, [data_ids[n - 1][0]])
                n += 1

            while m + i < len(data_ids):
                if m + i != len(data_ids) - 1:
                    lst.append([data_ids[m + i][0]])
                else:
                    break
                m += 1

            id_groups.append(lst)

        elif i == len(data_ids) - 1:
            n = 1
            lst = [data_ids[i]]

            while n - 1 < i:
                if data_ids[n - 1][0] == '%s' % dd:
                    lst.insert(n - 1, [data_ids[n - 1][1]])
                else:
                    lst.insert(n - 1, [data_ids[n - 1][0]])
                n += 1

            id_groups.append(lst)

    return id_groups


# id_groups = generate_id_groups(data_ids)
# for i in id_groups:
#	print(i)


def CrawlId(price_txt, base_infos, id_group, th):  # 解析pid,mid,PriceUnits  th记录循环次数

    data_ids = id_group

    if base_infos == None:

        res = [[]]

        for i in data_ids:
            res = [x + [y] for x in res for y in i]
        price_units = [';'.join(i) for i in res]

        for i in price_units:
            print(i)
            price_txt.write(i + '\n')
            price_txt.flush()
            print('PriceUnits组合数量：%s' % len(price_units))

    else:
        res = [[]]
        aaa = []  # 靓机选项

        for i in data_ids:
            res = [x + [y] for x in res for y in i]

        if th == 0:  # 各种组合的靓机价
            aaa += res[0]
            base_infos_tem = [i + aaa for i in base_infos]
            base_infos_units = [';'.join(i) for i in base_infos_tem]
            for i in base_infos_units:
                print(i)
                price_txt.write(i + '\n')
                price_txt.flush()
            print('PriceUnits组合数量：%s' % len(base_infos_units))

        res = [base_infos[0] + i for i in res]
        price_units = [';'.join(i) for i in res]

        for i in price_units:
            print(i)
            price_txt.write(i + '\n')
            price_txt.flush()
        print('PriceUnits组合数量：%s' % len(price_units))


pid = pid

url = 'https://www.aihuishou.com/product/{pid}.html'
url = url.format(pid=pid)
num = n

dd = 4475

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36'}

if __name__ == '__main__':

    r = requests.get(url, headers=headers)
    html = etree.HTML(r.text)
    info_amount = len(html.xpath('//div[@class="select-property base-property"]/dl'))  # 基本信息选项数量
    data_ids = get_data_ids(url)

    # print('data_ids:%s'%data_ids)
    base_infos = get_base_infos(url, num)

    for th in range(len(generate_id_groups(data_ids, dd))):
        path = phone_path
        price_txt = open(phone_path, 'a',
                         encoding='utf-8')

        CrawlId(price_txt, base_infos, generate_id_groups(data_ids, dd)[th], th)

