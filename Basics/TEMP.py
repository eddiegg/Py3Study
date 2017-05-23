# import os, pickle, json, shutil, glob, re
# import pyexcel as pe
import heapq
from collections import defaultdict


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


# records = pyexcel.get_sheet(file_name='./test.xlsx')
# new_column = ["结果"]
# for record in records:
#     if(record[0]=='企业C'):
#         new_column.append('通过')
# records.column+=new_column
# records.save_as('./test.xlsx')

# data = pe.iget_records(file_name='./comp.xlsx')
# for record in data:
#     # print(record,type(record))
#     print(record['企业名'])

# data = pe.get_sheet(file_name='./comp.xlsx',start_row=1,row_limit=3)
# print(len(list(data.rows())))
# for record in data:
#     print(record)

# data = pe.get_sheet(file_name='./comp.xlsx')
# del data.row[4:]
# data.save_as(filename='./comp.xlsx')

# data = pe.get_sheet(file_name='./comp.xlsx')
# print(data)


# '''根据处理结果更新列'''
# data = pe.get_sheet(file_name='./test.xlsx')
# print(type(data))
# for record in data:
#     try:
#         if(int((record[1])[:-1])>8000):
#             record[2]='不错'
#         else:
#             record[2]='继续努力'
#     except ValueError:
#         print('这条数据有问题：'+str(record))
#         pass
# data.save_as(filename='./comp_result.xlsx')

# '''处理有多行合并的excel数据，去除空行和不需要的行，去除不需要的列并加上需要的新列'''
# data = pe.get_sheet(file_name='F:\\fj2.xlsx')
# num_rows = data.number_of_rows()
# num_cloumns = data.number_of_columns()
# to_be_deleted = []
# for i in range(0, num_rows):
#     if (data.row[i][0] == '' or data.row[i][0] == '企业类型' or data.row[i][0] == '企业名称'):
#         to_be_deleted.append(i)
# data.delete_rows(to_be_deleted)
# data.delete_columns([x for x in range(1, num_cloumns)])
# # 新增一列
# data.column += ["结果", ]
# data.save_as(filename='F:\\fj2.xlsx')

# '''list of list数据保存为excel'''
# data=pe.get_sheet(file_name='F:\\fj2.xlsx')
# result=[]
# for line in data:
#     result.append(list(line))
# pe.save_as(array=result,dest_file_name='F:\\arraytoexcel.xlsx')
#
# '''处理有多行合并的excel数据，去除空行和不需要的行，去除不需要的列并加上需要的新行'''
# data = pe.get_sheet(file_name='F:\\hz0505.xlsx')
# to_be_deleted = []
# print(type(data.row))
# for i,record in enumerate(data.rows()):
#     if (data.row[i][0] == '' or data.row[i][0] == '企业类型' or data.row[i][0] == '企业名称'):
#         to_be_deleted.append(i)
# data.delete_rows(to_be_deleted)
# data.delete_columns([x for x in range(1, data.number_of_columns())])
# # 新增一行，只能加在末尾
# data.save_as(filename='F:\\hz0505.xlsx')

d= defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print(d)