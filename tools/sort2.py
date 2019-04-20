import copy

# base_property = {'1291': [7401, 7402], '315': [2023, 3987, 7396], '314': [2014, 2015, 2019, 2794, 2984, 3950], '456': [2452, 2902, 2903], '333': [2072, 2075], '343': [2100, 2101], '352': [2124, 2125, 2126, 2128, 6873], '351': [2118, 2120, 3098, 2122], '350': [2114, 2115, 8565, 2475, 3304], '332': [2067, 2965, 2070, 2069], '580': [3168, 3169], '353': [2129, 2130], '355': [2134, 2135], '1279': [6982, 6985], '325': [2045, 2047], '1135': [5300, 5299], '345': [2104, 2105], '347': [2108, 2109], '1268': [6947, 6948], '529': [2808, 2809]}

# cc = [{'id': 2014, 'name': '大陆国行（有“进网许可”标签）'}, {'id': 2902, 'name': '灰色'}, {'id': 3084, 'name': '全网通'}, {'id': 4066, 'name': '4G+64G'}, {'id': 2026, 'name': '正常进入桌面'}, {'id': 2067, 'name': '无维修情况'}, {'id': 2114, 'name': '很少使用，显示完美几乎全新'}, {'id': 2118, 'name': '很少使用，完美无任何痕迹'}, {'id': 2125, 'name': '很少使用，完美无任何痕迹'}, {'id': 3222, 'name': '账号可退出'}, {'id': 2106, 'name': '充电正常'}, {'id': 6949, 'name': '振动正常'}]

# print('------ccc---------',len(cc))
# # print(cc)

def sort3(base_property,cc): # 手机
    kk = base_property.keys()
    if '492' in kk: # 全网通
        base_property['1'] = base_property.pop('492')
    if '456' in kk: # 金色
        base_property['2'] = base_property.pop('456')
    if '806' in kk: # 内存
        base_property['3'] = base_property.pop('806')
    if '314' in kk:  # 购买渠道
        base_property['4'] = base_property.pop('314')
    if '1228' in kk:  # 苹果型号
        base_property['5'] = base_property.pop('1228')
#------------------------------------------------------
    if '580' in kk: # 触摸功能
        base_property['10000'] = base_property.pop('580')
    if '353' in kk: # 受潮状况
        base_property['10001'] = base_property.pop('353')
    if '1279' in kk: # 零件维修和更换情况
        base_property['10002'] = base_property.pop('1279')
    if '325' in kk: # 通话功能
        base_property['10003'] = base_property.pop('325')
    if '344' in kk: # 指纹功能
        base_property['10004'] = base_property.pop('344')
    if '345' in kk: # 拍摄功能
        base_property['10005'] = base_property.pop('345')
    if '347' in kk: # 无线功能
        base_property['10006'] = base_property.pop('347')
    if '1268' in kk: # 屏幕传感器功能
        base_property['100007'] = base_property.pop('1268')
    if '529' in kk: # 指南功能不正常
        base_property['100008'] = base_property.pop('529')
    if '5300' in kk:  # 面容识别功能
        base_property['100009'] = base_property.pop('5300')
    if '355' in kk:  # 机身是否弯曲"
        base_property['100010'] = base_property.pop('355')
    if '1135' in kk:  # 面容识别功能"
        base_property['100011'] = base_property.pop('1135')
    if '1269' in kk:  # 震动功能"
        base_property['100012'] = base_property.pop('1269')
    for c in cc:
        c['k_sort'] = 9999
        for k,v in base_property.items():
            if c['id'] in v:
                c['k_sort'] = int(k)
    print(cc)

    def function(date):
        return date['k_sort']

    cc.sort(key=function)
    return (cc)


def sort2(base_property,des):
    res = []
    cc1 = copy.deepcopy(des)
    print('before cc1=============')
    print(cc1)
    for d in des:
        for bp in base_property.keys():
            # print(rr[r])
            if d['id'] in base_property[bp]:
                print('-----c---------')
                print(d)
                res.append(d)
                cc1.remove(d)
                break
    res = res+cc1
    return res



def sort_pc(base_property,cc):
    """
    :param base_property:  获取的基本属性
    :param cc: 每个组合返回的组合属性
    :return: 排序后的属性
    """
    kk = base_property.keys()
    if '1197' in kk: # 固态硬盘
        base_property['1'] = base_property.pop('1197')
    if '724' in kk: # 处理器
        base_property['2'] = base_property.pop('724')
    if '1227' in kk: # 内存
        base_property['3'] = base_property.pop('1227')
        #---------------------更新线---------
    if '314' in kk:  # 购买渠道
        base_property['4'] = base_property.pop('314')
    if '1228' in kk:  # 苹果型号
        base_property['5'] = base_property.pop('1228')
#------------------------------------------------------
    if '1261' in kk: # 进水情况
        base_property['10000'] = base_property.pop('1261')
    if '1262' in kk: # 内部维修
        base_property['10001'] = base_property.pop('1262')
    if '507' in kk: # 硬盘使用情况
        base_property['10002'] = base_property.pop('507')
    if '327' in kk: # 键盘使用情况
        base_property['10003'] = base_property.pop('327')
    if '321' in kk: # 电池情况
        base_property['10004'] = base_property.pop('321')
    if '454' in kk: # 触摸板
        base_property['10005'] = base_property.pop('454')
    if '1256' in kk: # 接口功能
        base_property['10006'] = base_property.pop('1256')
    # if '1268' in kk: # 屏幕传感器功能
    #     base_property['100007'] = base_property.pop('1268')
    # if '529' in kk: # 指南功能不正常
    #     base_property['100008'] = base_property.pop('529')
    # if '5300' in kk:  # 面容识别功能
    #     base_property['100009'] = base_property.pop('5300')
    # if '355' in kk:  # 机身是否弯曲"
    #     base_property['100010'] = base_property.pop('355')
    # if '1135' in kk:  # 面容识别功能"
    #     base_property['100011'] = base_property.pop('1135')
    # if '1269' in kk:  # 震动功能"
    #     base_property['100012'] = base_property.pop('1269')
    for c in cc:
        c['k_sort'] = 9999
        for k,v in base_property.items():
            if c['id'] in v:
                c['k_sort'] = int(k)
    print(cc)

    def function(date):
        return date['k_sort']
    cc.sort(key=function)
    return (cc)
# res = sort(base_property,cc)
# print('------res----------',len(res))
# print(res)