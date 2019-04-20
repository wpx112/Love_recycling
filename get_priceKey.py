# !/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from mysetting import phone_name,res_path
# from tools.sort2 import sort3
from tools.sort2 import sort_pc
# from test.sort3 import sort3
from tools.write import write_list
from feifei.fateadm_api import TestFunc



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Host': 'www.aihuishou.com',
    'Referer': 'https://www.aihuishou.com/product/27640.html'
}



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
    if r.status_code ==200:
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
                'IsEnvironmentalRecycling': '',
                'imgCaptcha': imgCaptcha
            }
            rr = sess.post(url=url, headers=headers, data=data)
            res = rr.json()
            print(res)
            return res['data']['redirectUrl'].split('/')[-1]
        print(res)
        return res['data']['redirectUrl'].split('/')[-1]


def get_priceKey_old(pid, ppvids):
    """
    返回 获取价格接口需要的参数
    :param pid: 手机的productid
    :param ppvids: 手机属性的组合
    :return: key参数
    """
    url = 'https://www.aihuishou.com/userinquiry/create'
    imgCaptcha = ''
    pid = str(pid)
    mid=''
    price_unit = ';'.join(ppvids)
    print(price_unit)
    data = {
        'AuctionProductId': pid,
        'ProductModelId': mid,
        'PriceUnits': price_unit,
    }
    print('-------------参数传递------------')
    print(data)
    sess = requests.Session()
    r = sess.post(url=url, headers=headers, data=data)
    res = r.json()
    while res['code'] in [3001, 3002]:
        print(res['data']['captchaUrl'])
        r = sess.get(res['data']['captchaUrl'])
        path = r'./tools/yzcode/yzcode.jpg'
        with open(path,'wb') as fp:
            fp.write(r.content)

        s = TestFunc()
        # s = input('请输入验证码')
        print(s)
        imgCaptcha = s
        data = {
            'AuctionProductId': pid,
            'ProductModelId': mid,
            'PriceUnits': price_unit,
            'imgCaptcha': imgCaptcha
        }
        rr = sess.post(url=url, headers=headers, data=data)
        res = rr.json()
        if res['code'] not in [3001, 3002]:
            with open(path,'rb') as fp:
                content = fp.read()
                s_path = r'D:\wpx\workspace\Love_recycling\tools\save_jpg\{s}.jpg'
                save_path = s_path.format(s=s)
                with open(save_path, 'wb') as ffp:
                    ffp.write(content)

    print(res)
    redirectUrl = res['data']['redirectUrl']
    if 'Noprice' in redirectUrl:
        return 400
    return redirectUrl.split('/')[-1]


def get_price(key,base_property):
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
        print('------------key-'+key+'%----------')
        res_data = r.json()
        res_data = res_data['data']
        price = res_data['amount']
        product_name = res_data['product']
        describe = res_data['inquiryValues']

        describe = sort_pc(base_property=base_property,cc=describe)

        print('-------------------describe---------------')
        print(describe)
        ds = []

        for d in describe:
            ds.append(d['name'])
        ds = [str(price),phone_name]+ds
        print('-------------------------------------ds------------------------------')
        print(ds) # 在此处开始写入csv
        write_list(file_name=res_path,content=ds)
        print('---价格----',str(price))



