import pyexcel as pe

#企查查文件
qxxfile = 'F:\\sh0519.xls'
#定义企查查文件抽取记录日期
qxx_date = '2017-05-10'
#启信宝文件
qxbfile = 'F:\\sh0510.xlsx'

#提取qxx指定日期的数据
sh = pe.get_sheet(file_name=qxxfile,start_row=1)
temp = []
for record in sh:
    if record[2] == qxx_date:
        temp.append(record[0])

#处理qxb数据
data = pe.get_sheet(file_name=qxbfile)
to_be_deleted = []
for i,record in enumerate(data.rows()):
    if (data.row[i][0] == '' or data.row[i][0] == '企业类型' or data.row[i][0] == '企业名称'):
        to_be_deleted.append(i)
data.delete_rows(to_be_deleted)
data.delete_columns([x for x in range(1, data.number_of_columns())])
data.column+=temp
data.save_as(filename=qxbfile)

qxb=[]
qxx=[]

#生成结果
data = pe.get_sheet(file_name=qxbfile)
row = data.number_of_rows()
for records in data:
    qxb.append(records[0])
    qxx.append(records[1])
qxxonly = [item for item in qxx if item not in qxb]
qxbonly = [item for item in qxb if item not in qxx]
both= [item for item in qxx if item in qxb]
data.column += qxbonly
data.column += qxxonly
data.column += both
data.row = data.row +  ['启信宝','企查查','启信宝独有','企查查独有','共有']
data.save_as(filename=qxbfile)

#表头顺序调整
data=pe.get_sheet(file_name=qxbfile)
index=data.number_of_rows()
for i in range(index-1,0,-1):
        data.row[i],data.row[i-1] = data.row[i-1],data.row[i]
data.save_as(filename=qxbfile)