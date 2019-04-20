import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}



def get_property(product_id):
    """
    :param product_id: 手机id
    :return: ppvids 手机中各个属性
    """
    phone_url = 'https://www.aihuishou.com/portal-api/product/quick-inquiry?productId={product_id}'
    phone_url = phone_url.format(product_id=product_id)
    r = requests.get(url=phone_url, headers=headers)
    res = r.json()

    ppvid_items = {}
    items = res['data']['items']
    print(items)
    ppvid_items['normal'] =items[0]['ppvs']
    ppvid_items['new'] = items[1]['ppvs']
    ppvid_items['bad'] = items[2]['ppvs']
    print(ppvid_items)

def get_property2(product_id):
    phone_url = 'https://www.aihuishou.com/product/{product_id}.html'
    phone_url = phone_url.format(product_id=product_id)
    # print(phone_url)
    r = requests.get(url=phone_url, headers=headers)
    res = r.text
    return res






res = get_property2(24347)
print(res)
