import pyexcel as pe
import multitasking
from testbyexcel.common import Common

case_data = pe.get_book(file_name='./case.xlsx')

@multitasking.task
def run_case():
    run=Common('safari')
    run.open('http://www.baidu.com')
    action = {
        'type':run.type,
        'click':run.click,
        'quit':run.quit,
        'get_text':run.get_text,
        'get_title':run.get_title,
        'verify_attribute': run.verify_attribute
    }
    for step in case_data.sheet_by_index(i).rows():
        if(step[0]=='action'):
            pass
        elif(step[0] in ['text','value']):
            result= action.get('verify_attribute')(step)
            step[8] = result
        elif(action.get(step[0])):
            (action.get(step[0]))(step)
            step[8] = 'pass'

for i in range(1,case_data.number_of_sheets()):
    run_case()

case_data.save_as(filename='./try.xlsx')
