# coding:utf-8
import csv, requests, json, time, xlwt
qxb=[]
qxx=[]

with open(r'F:\compare\qxb_hangzhou_0505.csv', 'r', encoding='gbk') as source:
    readdata = csv.reader(source)
    for row in readdata:
        qxb.append(row)

with open(r'F:\compare\qxx_hangzhou_0505.csv', 'r', encoding='gbk') as source:
    readdata = csv.reader(source)
    for row in readdata:
        qxx.append(row)

print(len(qxx), len(qxb))
qxxonly = [item for item in qxx if item not in qxb]
qxbonly = [item for item in qxb if item not in qxx]
both = [item for item in qxb if item in qxx]
print(qxxonly)
print(qxbonly)
print(len(qxxonly),len(qxbonly),len(both))

