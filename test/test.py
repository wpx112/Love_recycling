# !/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
headers = {
    'Origin': 'https://www.aihuishou.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    # 'Host': 'www.aihuishou.com',

}
url1 = 'https://www.aihuishou.com/userinquiry/create'
captcha = ''
data1 = {
    'AuctionProductId':'27604',
    'ProductModelId':'',
    'PriceUnits':'2014;2023;2075;2902;7401;2026;2100;2125;2118;2114;2067',
     'imgCaptcha':captcha
}
print(data1)
sess = requests.Session()
r = sess.post(url=url1, headers=headers, data=data1)
res = r.json()
print(res)
while res['code'] in [3001,3002]:
    # yz_url = res['data']['captchaUrl']
    # imge = requests.get(yz_url)
    # with open('./2.jpg','wb') as fp:
    #     fp.write(imge.content)
    #
    print(data1)
    s = input('请输入验证码:')
    print(s)

    captcha = s
    data1 = {
        'AuctionProductId':27604,
        'ProductModelId':'',
        'PriceUnits':'2014;2023;2075;2902;7401;2026;2100;2125;2118;2114;2067',
        'imgCaptcha':captcha
    }
    print(type(data1))
    rr = sess.post(url=url1, headers=headers, data=data1)
    res=rr.json()
    print(res)
    img_url = 'https://www.aihuishou.com/captcha/getimgcaptcha'
    img_data = {
        'type': 'Inquiry'
    }
    img_r = sess.post(url=img_url, headers=headers, data=img_data)
    print(img_r.json())


