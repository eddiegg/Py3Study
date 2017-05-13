import pyexcel as pe

from testbyexcel.common import Common

case_data = pe.get_book(file_name='./case.xlsx')
run=Common('ie')
run.open('http://www.baidu.com')
action = {
    'type':run.type,
    'click':run.click,
    'quit':run.quit,
    'get_text':run.get_text,
    'get_title':run.get_title
}
for step in case_data.sheet_by_index(1).rows():
    if(step[0]=='action'):
        pass
    elif(action.get(step[0])):
        (action.get(step[0]))(step)

