import os, pickle, json , shutil, glob
from tablib import Dataset
import pyexcel as pe
import pyexcel_xls

# d = "F:\\"
# print([x for x in os.listdir(d) if os.path.isfile(d+x)])

# my_dict = {"title":"pyton","price":20.00}

# '''dumps返回str，dump写入文件'''
# print(pickle.dumps(my_dict))
# pp = pickle.dumps(my_dict)
# '''loads字符串反序列化，load从文件读取字符串并反序列化'''
# print(pickle.loads(pp))
# with open(r'F:\temp.txt','wb') as f:
#     pickle.dump(my_dict,f)
# with open(r'F:\temp.txt','rb') as f:
#     print(pickle.load(f))

# my_dict_str = json.dumps(my_dict)
# print(my_dict_str)
# print(json.loads(my_dict_str))
#
# with open('./ff','w') as f:
#     json.dump(my_dict,f)
# with open('./ff','r') as f:
#     print(json.load(f)["title"])
#
# '''利用obj的__dict__方法序列化对象'''
# class BookShelf:
#     def __init__(self, no, capacity):
#         self.number = no
#         self.capacity = capacity
#
# book_shelf = BookShelf(1,100)
#
# print(json.dumps(book_shelf,default=lambda obj:obj.__dict__))
#
# '''反序列化JSON为对象,利用object_hook函数'''
# def dict_to_BookShelf(js_str):
#     return BookShelf(js_str['number'],js_str['capacity'])
#
# book_shelf_str = '{"capacity": 100, "number": 1}'
# print(json.loads(book_shelf_str, object_hook=dict_to_BookShelf))
# with open('./fn','wb') as wf:
#     with open('./ff' ,'rb') as inf:
#         shutil.copyfileobj(inf, wf, 1024*24)

# num = 3.03
# if(str(num) == str(num)[::-1]):
#     print("true")
# else:
#     print("false")

# test_result = Dataset()
# test_result.headers = ('公司','是否查找到（Y/N）')
# with open('./fn','r',encoding='utf-8',newline='') as f:
#     for line in f:
#         line = line.strip('\n').split(',')
#         test_result.append(line)
# time_stamp = ['05/10','05/09',' ',' ']
# test_result.append_col(time_stamp,'时间')
# with open('./tt.xls','wb') as d:
#     d.write(test_result.xls)

# records = pyexcel.get_sheet(file_name='./test.xlsx')
# new_column = ["结果"]
# for record in records:
#     if(record[0]=='企业C'):
#         new_column.append('通过')
# records.column+=new_column
# records.save_as('./test.xlsx')

records = pe.get_sheet(file_name='F:\\fj.xlsx')
comp_list = []
for record in records:
    if(record[0] != '' and record[0] != '企业名称'):
        comp_list.append(record[0])
print(comp_list)
print(len(comp_list))