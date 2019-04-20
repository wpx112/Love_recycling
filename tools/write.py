import csv
# import codecs


s = ['大陆国行（有“进网许可”标签）', '金色', '移动版', '6G+128G', '正常进入桌面', '无维修情况', '很少使用，显示完美几乎全新', '很少使用，完美无任何痕迹', '很少使用，完美无任何痕迹', '账号可退出', '充电正常', '振动正常']
file_name = './111111111.csv'

def write_list(file_name,content):
    with open(file_name,'a',newline='') as fp:
        csvwriter = csv.writer(fp,dialect=("excel"))
        csvwriter.writerow(content)