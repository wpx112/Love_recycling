#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
from lxml import etree
from mysetting import pid,n
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3381.1 Safari/537.36'}


def get_base_infos(url,num):  # 获取所有靓机价的基本信息id组合
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = etree.HTML(r.text)
        base_infos_str = str(html.xpath('//div[@id="group-property"]/@data-sku-property-value-ids')[0])

        if base_infos_str == '[[]]':
            return None
        else:
            base_infos_lst = re.findall('\d+', base_infos_str)
            # n = len(html.xpath('//div[@class="select-property base-property"]/dl'))  #基本信息选项
            n = num

            base_infos = [base_infos_lst[i:i + n] for i in range(0, len(base_infos_lst), n)]

        # print(len(base_infos))
        return base_infos

    else:
        print(r.status_code)
        return None


def get_data_ids(url,num):
    data_ids = []
    tem_ids = []
    base_infos = get_base_infos(url,num)
    r = requests.get(url, headers)

    if r.status_code == 200:
        html = etree.HTML(r.text)

        function_ids = html.xpath('//*[@id="function-property"]/dl/dd/ul/li/@data-id')
        base_property_dls = html.xpath('//*[@id="base-property"]/dl')

        # for dl in base_property_dls:
        #     data_id = dl.xpath('./dd/ul/li/@data-id')
        #     data_ids.append(data_id)

        # 查找data-ids
        for dl in base_property_dls:
            data_id = [re.findall('\d+', i)[0] for i in dl.xpath('./dd/ul/li/@data-ids')]
            data_ids.append(data_id)

        if base_infos != None:
            for data_id in data_ids:
                for id in data_id:
                    if id in base_infos[0]:
                        tem_ids.append(data_id)

        data_ids = [i for i in data_ids if i not in tem_ids]
        data_ids.append(function_ids)
        return data_ids

    else:
        print(r.status_code)
        return None


def generate_id_options(data_ids, qx_id='2124'):  # 生成所有估价的id选项组合(不包含基本信息), qx_id为全新机选项id
    id_options_all = []

    for i in range(len(data_ids)):

        if i == 0:
            id_options = []

            for id in data_ids[i]:
                id_option = [id]
                n = 1
                while n < len(data_ids) - 1:
                    if data_ids[n][0] == qx_id:
                        id_option.append(data_ids[n][1])
                    else:
                        id_option.append(data_ids[n][0])
                    n += 1
                id_options.append(id_option)

            id_options_all += id_options
        # print(len(id_options_all))

        elif i < len(data_ids) - 1:
            id_options = []

            if qx_id in data_ids[i]:
                data_id_tem = data_ids[i][:]
                data_id_tem.remove(data_ids[i][1])
            else:
                data_id_tem = data_ids[i][1:]

            for id in data_id_tem:
                id_option = [id]
                n, m = 1, 1

                while n - 1 < i:
                    if data_ids[n - 1][0] == qx_id:
                        id_option.insert(n - 1, data_ids[n - 1][1])
                    else:
                        id_option.insert(n - 1, data_ids[n - 1][0])
                    n += 1

                while m + i < len(data_ids) - 1:
                    if data_ids[m + i][0] == qx_id:
                        id_option.append(data_ids[m + i][1])
                    else:
                        id_option.append(data_ids[m + i][0])
                    m += 1
                id_options.append(id_option)

            id_options_all += id_options
        # print(len(id_options_all))

        elif i == len(data_ids) - 1:
            id_options = []

            for id in data_ids[i]:
                id_option = [id]
                n = 1
                while n - 1 < i:
                    if data_ids[n - 1][0] == qx_id:
                        id_option.insert(n - 1, data_ids[n - 1][1])
                    else:
                        id_option.insert(n - 1, data_ids[n - 1][0])
                    n += 1
                id_options.append(id_option)

            id_options_all += id_options
        # print(len(id_options_all))

    return id_options_all


def generate_id_units(id_options, base_infos, qx_id='2124'):  # 生成所有包含基本信息id选项组合

    id_units = []

    if base_infos == None:
        for id_option in id_options:
            id_unit = ';'.join(id_option)
            id_units.append(id_unit)

        return id_units

    else:
        if id_options[0][0] == qx_id:  # 如果首项为全新机，则用第二项与基本信息组合生成所有靓机的估价id组合

            for base_info in base_infos:
                base_info_unit = base_info + id_options[1]
                id_units.append(';'.join(base_info_unit))

        else:
            for base_info in base_infos:
                base_info_unit = base_info + id_options[0]
                id_units.append(';'.join(base_info_unit))

        for id_option in id_options:
            id_units.append(';'.join(base_infos[0] + id_option))

        return id_units


'''			

phone_qx_id = '2124'   #手机1 全新机选项id

pad_qx_id = '1983'     #平板全新机选项id
laptop_qx_id = '4475'  #笔记本全新机选项id

df_qx_id = '5676'  	   #单反相机全新机选项id
sm_qx_id = '2398'  	   #数码相机全新机选项id
jt_qx_id = '5677'  	   #镜头全新机选项id
wd_qx_id = '2375'  	   #微单全新机选项id
sx_qx_id = '3809'  	   #摄像机全新机选项id  
sg_qx_id = '4799'  	   #闪光灯全新机选项id
sb_qx_id = '5886'  	   #手表全新机选项id
'''


def entrance_ID(pid,n,phone_path):
    pid = pid

    url = 'https://www.aihuishou.com/product/{pid}.html'
    url = url.format(pid=pid)
    print(url)
    num = n

    base_infos = get_base_infos(url,num)
    data_ids = get_data_ids(url,num)
    id_options_all = generate_id_options(data_ids)
    id_units = generate_id_units(id_options_all, base_infos)

    with open(phone_path, 'a') as f:
        print('id组合数量：', len(id_units))
        for id in id_units:
            f.write(id + '\n')
            f.flush()


