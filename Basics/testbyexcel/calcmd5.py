import hashlib
import pyexcel as pe

# data = pe.get_sheet(file_name='/Users/eddie/PycharmProjects/Py3Study/Basics/testbyexcel/comp.xlsx')
# tokenlst=["token"]
# for i in range(1,data.number_of_rows()):
#     tempdict = dict(zip(data.row[0],data.row[i]))
#     sorted_tempdict = sorted(tempdict.items())
#     tempstr = ''
#     SALT='eddie'
#     for (k,v) in sorted_tempdict:
#         if k not in ['key','token','result']:
#             tempstr += str(v)
#     tempstr+=SALT
#     m5 = hashlib.md5()
#     m5.update(tempstr.encode(encoding='utf-8'))
#     tokenlst.append(m5.hexdigest())
# data.column[8]=tokenlst
# data.save_as(filename='./md5.xlsx')

parmfile = pe.get_sheet(file_name="./md5.xlsx")
for i in range(1,parmfile.number_of_rows()):
    tempdict = dict(zip(parmfile.row[0],parmfile.row[i]))
    parm={}
    for (k,v) in tempdict.items():
        if v != '':
            parm[k]=v
    print(parm)

parm_dict={"start":2,"eid":"123456","hit":5}


def get_md5(parms,salt):
    sorted_parm = sorted(parms.items())
    temp=''
    for (k,v) in sorted_parm:
        temp+=str(v)
    temp+=salt
    print(temp)
    m5 = hashlib.md5()
    m5.update(temp.encode(encoding='utf-8'))
    return m5.hexdigest()

# print(get_md5(parm_dict,SALT))