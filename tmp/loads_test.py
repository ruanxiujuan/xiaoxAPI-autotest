import json


f_posdict = open('test.txt', encoding='gbk')   # 打开‘demo.json’的json文件
posdict = f_posdict.read().split('\n')
posdict = [x.encode('utf-8').decode("utf-8-sig") for x in posdict]
res=json.load(f_posdict)                        # 把json串变成python的数据类型：字典
gpd_list = json.load(f_posdict)                 # 遍历列表的每个元素
for name in gpd_list:
    print(res)
print(type(res))
f_posdict.close()