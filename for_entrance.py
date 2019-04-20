# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from get_priceKey import get_priceKey,get_price,get_priceKey_old
import os
# from tools.sort2 import sort_pc
from tools.sort2 import sort3
from tools.write import write_list
from tools.entrance_ID_Units_PC import entrance_ID

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# product_id = '27756'

def start_id(product_id):
    print(product_id)
    def get_price(key,base_property,res_path,product_name):
        """
        根据key获取固定参数手机的价格
        :param key:
        :return:
        """
        if key!=400:
            print('------------key----------')
            print(key)
            url = 'https://www.aihuishou.com/portal-api/inquiry/'+key
            r = requests.get(url,headers=headers)
            # print('------------key-'+key+'%----------')
            res_data = r.json()
            res_data = res_data['data']
            price = res_data['amount']
            describe = res_data['inquiryValues']

            describe = sort3(base_property=base_property,cc=describe)

            # print('-------------------describe---------------')
            # print(describe)
            ds = []
            for d in describe:
                ds.append(d['name'])
            ds = [str(price),product_name]+ds
            print('-------------------------------------ds------------------------------')
            print(ds) # 在此处开始写入csv
            write_list(file_name=res_path,content=ds)

            print('---价格----',str(price))

    phone_url = 'https://www.aihuishou.com/portal-api/product/inquiry-detail-new/{product_id}?quickInquiryValue=0'
    phone_url = phone_url.format(product_id=product_id)
    r = requests.get(url=phone_url, headers=headers)
    res = r.json()
    data = res['data']
    skus = len(data['skus'][0])
    if not skus:
        skus =1


    print('-----------------skus-----------------')
    print(skus)
    print("-------------product_name-------------")
    # phone_name='这个没有标题'
    phone_name = data['product']['name']
    # phone_name = 'OPPO R17 Pro_Untis'
    print(phone_name)
    phone_path = r'D:\wpx\workspace\Love_recycling\property_comb\phone\20190420\ids\{pn}.txt'.format(pn=phone_name)
    # phone_path = r'D:\wpx\workspace\Love_recycling\property_comb\phone\20190420\ids\OPPO R17 Pro_Untis.txt'
    res_path = r'./property_comb/phone/20190420/results/{pn}.csv'.format(pn=phone_name)
    tag_path = r'./property_comb/phone/20190420/tag/{pn}.txt'.format(pn=phone_name)
    ppvids = {}
    for data_p in data['propertyNames']:
        datap_id = data_p['id']
        datap_name = data_p['name']
        print(datap_id)
        print(datap_name)
        datap_name = data_p['name']
        ids = []
        for dp in data_p['values']:
            ids.append(dp['ppvIds'][0])
        datap_id = str(datap_id)
        ppvids[datap_id] = ids
    print('------------------获取到手机的基本属性-------------------')
    #-----------------------------------------------entrance_ID_Units_PC-------------------------------------

    # from tools import entrance_ID_Units_PC
    tag = os.path.exists(tag_path)
    print('----------创建前')
    print(not tag)
    # 判断tag_path文件是否存在，没有则创建
    if not tag:
        print('-------------开始创建ID组合--------------')
        entrance_ID(pid=product_id, n=skus, phone_path=phone_path)
        print('-------------创建ID结束------------------')
        open(tag_path, 'a').close()


    # ---------------------------------------------read_text------------------------------------------------
    path = phone_path
    def get_combine(path):
        p_res = []
        with open(path,'r') as fp:
            while True:
                text_line = fp.readline()
                if text_line:
                    text_line = text_line.strip('\n')
                    p_res.append(text_line)
                else:
                    break
        return p_res


    # 读取已经下载好的id组合
    combine = get_combine(path)
    # 读取已经写入的id组合
    tag_combine = get_combine(tag_path)

    i = 1
    for ppvid in combine:
        if ppvid not in tag_combine:
            ppvid1 = ppvid.split(';')
            print('------ppvids1---------')
            print(ppvid1)
            key = get_priceKey_old(product_id, ppvid1)
            get_price(key, ppvids,res_path=res_path,product_name=phone_name)
            print('-------------------------------------第%d条数据写入完成-----------------------------------'%i)
            with open(tag_path,'a') as fp:
                fp.write(ppvid+'\n')
        i += 1


if __name__ == '__main__':
    pids = ['29023']

    for id in pids:
        start_id(id)








