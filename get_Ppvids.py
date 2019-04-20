# !/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


def get_property(product_id):
    """
    :param product_id: 手机id
    :return: ppvids 手机中各个属性
    """
    phone_url = 'https://www.aihuishou.com/portal-api/product/inquiry-detail-new/{product_id}?quickInquiryValue=0'
    phone_url = phone_url.format(product_id=product_id)
    r = requests.get(url=phone_url, headers=headers)
    res = r.json()
    data = res['data']
    skus = len(data['skus'][0])
    print('------------skus--------------')
    print(skus)
    print("-------------res-------------")
    # print(res)
    product = data['product']
    product_id = product['id']
    print(product_id)
    ppvids = {}
    print('-------propertyNames-------')
    print(data['propertyNames'])
    for data_p in data['propertyNames']:
        datap_id = data_p['id']
        datap_name = data_p['name']
        print(datap_id)
        print(datap_name)
        datap_name = data_p['name']
        ids = []
        for dp in data_p['values']:
            ids.append(dp['ppvIds'][0])

        datap_id =str(datap_id)
        ppvids[datap_id]=ids
    print('------------------获取到手机的基本属性-------------------')
    print(ppvids)
    return ppvids

# res = get_property(170)
# print(res)