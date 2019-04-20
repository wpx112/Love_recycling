from get_Ppvids import get_property
from get_priceKey import get_priceKey,get_price,get_priceKey_old
from mysetting import phone_path,pid,tag_path,phone_name
import os

# 判断tag_path文件是否存在，没有则创建
tag = os.path.exists(tag_path)
if not tag:
    open(tag_path, 'a').close()


path = phone_path
base_property = get_property(pid)


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
        key = get_priceKey_old(pid, ppvid1)
        get_price(key, base_property)
        print('-----------------------------------------第%d条数据写入完成-----------------------------------'%i)
        with open(tag_path,'a') as fp:
            fp.write(ppvid+'\n')
    i+=1







