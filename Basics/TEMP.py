#coding:utf-8
# import os, pickle, json, shutil, glob, re
# import pyexcel as pe
import requests,json


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

jsonVal=[{"conditions":[{"filed":"test1","operation":"lt","value":"111"},  \
                        {"filed":"test2","operation":"rt","value":"333"},   \
                        {"filed":"test3","operation":"eq","value":"222"}]},"2nd"]
jstring='{"end_date":"-","changerecords":[],"address":"重庆市渝中区瑞天路182号6单元1-2#","reg_no":"500103008812619","oper_name":"官珉","branches":[],"credit_no":"91500103MA5U6FHX56","term_start":"2016-06-16","province":"CQ","partners":[{"stock_type":"自然人","identify_no":"（非公示项）","real_capi_items":[],"name":"官珉","identify_type":"（非公示项）","should_capi_items":[{"should_capi_date":"-","invest_type":"","shoud_capi":"100 万人民币"}]},{"stock_type":"自然人","identify_no":"（非公示项）","real_capi_items":[],"name":"邓小柱","identify_type":"（非公示项）","should_capi_items":[{"should_capi_date":"-","invest_type":"","shoud_capi":"100 万人民币"}]}],"check_date":"2016-06-16","scope":"预包装食品经营（依法须经批准的项目，经相关部门批准后方可开展经营活动）；销售初级农产品、日用百货、办公用品、工艺美术品（不含文物）；货物进出口（法律、行政法规禁止的项目除外，法律、行政法规限制的项目取得许可后经营）。『以上范围法律、法规、国务院决定禁止经营的不得经营；法律、法规、国务院决定规定应经审批而未获审批前不得经营』★★","name":"重庆千香汇商贸有限公司","belong_org":"重庆市工商行政管理局渝中区分局","term_end":"永久","id":"6681b7e7-216b-4bc9-b322-54c5e18f3abd","org_no":"MA5U6FHX5","abnormal_items":[],"employees":[{"name":"官珉","job_title":"执行董事、经理"},{"name":"邓小柱","job_title":"监事"}],"regist_capi":"200 万人民币","econ_kind":"有限责任公司(自然人投资或控股)","start_date":"2016-06-16","status":"存续"}'

pp=json.loads(jstring)
keys=[]
keys2=pp.keys()
def get_keys(dic):
    for (key,value) in dic.items():
        if(isinstance(value,dict)):
            get_keys(value)
        elif(isinstance(value,list)):
            if(len(value)>0):
                temp=dict(value[0])
                keys.append(key)
                for (k,v) in temp.items():
                    keys.append(k)
            else:
                keys.append(key)
        else:
            keys.append(key)

get_keys(pp)
print(keys)
print(keys2)
