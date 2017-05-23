import pyexcel as pe

from testbyexcel.common import Common
case_data = pe.get_book(file_name='./case.xlsx')
run=Common('chrome')
run.open('http://www.qixin.com')
cookie={}
cookie = {'name':'sid',
              'value': 's%3AHT9QqsgJt7peDpuKm5v1xHIWMH86y-hc.Pkp5AmvF6mFp3zsNoPDECrYT1vyLWeJqTlg73dm8oX4'}
run.driver.add_cookie(cookie)
action = {
    'type':run.type,
    'click':run.click,
    'quit':run.quit,
    'get_text':run.get_text,
    'get_title':run.get_title,
    'open':run.open
}
for step in case_data.sheet_by_index(1).rows():
    if(step[0]=='action'):
        pass
    # elif(step[0]=='open'):
    #     action.get(step[0])(step[1])
    #     cookie = {'name': 'sid',
    #               'value': 's%3AHT9QqsgJt7peDpuKm5v1xHIWMH86y-hc.Pkp5AmvF6mFp3zsNoPDECrYT1vyLWeJqTlg73dm8oX4'}
    #     run.driver.add_cookie(cookie)
    elif(action.get(step[0])):
        (action.get(step[0]))(step)