
# !/usr/bin/env python
# -*- coding: utf-8 -*-


import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host': 'www.aihuishou.com',
    'Referer': 'https://www.aihuishou.com/product/27640.html'
}

# Ppvids = ['2130', '2135', '6873', '2047', '2069', '9507', '5299', '3169', '2809', '6949', '2101', '2105', '2106', '2109','2027', '3304', '6985', '2122', '6948']


def get_priceKey(pid, ppvids):
    """
    返回 获取价格接口需要的参数
    :param pid: 手机的productid
    :param ppvids: 手机属性的组合
    :return: key参数
    """
    url = 'https://www.aihuishou.com/userinquiry/createnew.html'
    imgCaptcha = ''
    pid = str(pid)
    data ={
        'productId': pid,
        'PpvIds[]': ppvids,
        # 'IsEnvironmentalRecycling': 'true',
        'imgCaptcha': imgCaptcha
    }
    print('-------------参数传递------------')
    print(ppvids)
    print(data)
    sess = requests.Session()
    r = sess.post(url=url, headers=headers, data=data)
    res = r.json()

    while res['code'] in [3001, 3002]:
        print(res['data']['captchaUrl'])
        r = sess.get(res['data']['captchaUrl'])

        with open('./code.jpg','wb') as fp:
            fp.write(r.content)
        s = input('请输入验证码')
        print(s)
        imgCaptcha = s
        data = {
            'productId': pid,
            'PpvIds[]': ppvids,
            # 'IsEnvironmentalRecycling': 'true',
            'imgCaptcha': imgCaptcha
        }
        rr = sess.post(url=url, headers=headers, data=data)
        res = rr.json()
        print(res)
        return res['data']['redirectUrl'].split('/')[-1]
    print(res)
    return res['data']['redirectUrl'].split('/')[-1]



def get_price(key):
    """
    根据key获取固定参数手机的价格
    :param key:
    :return:
    """
    url = 'https://www.aihuishou.com/portal-api/inquiry/'+key
    r = requests.get(url,headers=headers)
    print('---------------------正在获取价格----------------')
    print('------------key-'+key+'%----------')
    res_data = r.json()
    res_data = res_data['data']
    price = res_data['amount']
    product_name = res_data['product']
    describe = res_data['inquiryValues']
    # print(describe)
    # print(res_data)
    ds = []
    for d in describe:
        ds.append(d['name'])
    print(ds)
    print('---价格----',str(price))

    return price
Ppvids = [2124,2129,2134,3168,2045,2067,3222,6947,6949,2102,2104,2106,2108,2026,2114,6982,2118]

key = get_priceKey(27640,Ppvids)
price  = get_price(key)
print(price)