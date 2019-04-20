# !/usr/bin/env python
# -*- coding: utf-8 -*-



import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

def get_property(product_id):
    phone_url = 'https://www.aihuishou.com/portal-api/product/inquiry-detail-new/{product_id}?quickInquiryValue=0'
    phone_url = phone_url.format(product_id=product_id)
    r = requests.get(url=phone_url, headers=headers)
    res = r.json()
    data = res['data']
    print("-------------res-------------")
    product = data['product']
    product_id = product['id']
    print(product_id)
    ppvids = []
    print(len(data['propertyNames']))
    for data_p in data['propertyNames']:
        print(data_p)
        ids = []
        for dp in data_p['values']:
            ids.append(dp['ppvIds'][0])

        ppvids.append(ids)

    print('------------------获取到手机的基本属性-------------------')
    print(ppvids)
    # print('-'.join(ppvids))
    return ppvids

res = get_property(24347)


print(res)