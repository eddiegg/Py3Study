import pyexcel as pe

from testbyexcel.common import Common

case_data = pe.get_book(file_name='./case.xlsx')
run=Common('ff')
run.open('http://www.baidu.com')

for step in case_data.sheet_by_index(1).rows():
    if(step[0]=='action'):
        pass
    case:

        run.step[0](step)


