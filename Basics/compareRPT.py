import pyexcel as pe

#qxx文件，指定日期提取数据
sh = pe.get_sheet(file_name='F:\\sh.xls',start_row=1)
sh_0512 = []
for record in sh:
    if record[2] == '2017-05-12':
        sh_0512.append(record[0])

#qxb数据，处理下载的当日表格
data = pe.get_sheet(file_name='F:\\hz0504.xlsx')
to_be_deleted = []
for i,record in enumerate(data.rows()):
    if (data.row[i][0] == '' or data.row[i][0] == '企业类型' or data.row[i][0] == '企业名称'):
        to_be_deleted.append(i)
data.delete_rows(to_be_deleted)
data.delete_columns([x for x in range(1, data.number_of_columns())])
data.column+=sh_0512
data.save_as(filename='F:\\hz0504n.xlsx')

qxx=[]
qxb=[]

#生成结果
data = pe.get_sheet(file_name='F:\\hz0504n.xlsx')
row = data.number_of_rows()
for records in data:
    qxx.append(records[0])
    qxb.append(records[1])
qxxonly = [item for item in qxx if item not in qxb]
qxbonly = [item for item in qxb if item not in qxx]
both= [item for item in qxx if item in qxb]
data.column += qxxonly
data.column += qxbonly
data.column += both
data.row = data.row +  ['企查查','启信宝','企查查独有','启信宝独有','共有']
data.save_as(filename='F:\\hz0504n.xlsx')

data=pe.get_sheet(file_name='F:\\hz0504n.xlsx')
index=data.number_of_rows()
for i in range(index-1,0,-1):
        data.row[i],data.row[i-1] = data.row[i-1],data.row[i]
data.save_as(filename='')