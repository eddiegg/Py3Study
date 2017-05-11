#coding:utf-8
from pyquery import PyQuery as pq

rpt=pq(filename=r'E:\Py3Study\Basics\WebDemo\report\2017-04-25 18.18.26 result.html')
statics=rpt("#heading #attribute").items()
for item in statics:
    print(item.text())
