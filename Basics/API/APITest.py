import requests
import unittest
import json
import HTMLTestRunner
import time

class GetChainRelation(unittest.TestCase):
    '''接口测试，包含ByID和ByName'''


    def setUp(self):
        self.base_url = r'http://uatapi..com/APIService/'
        self.appkey = ''

    def tearDown(self):
        pass

    def testGetChainRelationById(self):
        '''正常返回'''
        self.data={"appkey":self.appkey,
             "id":'94878eba-ddf0-41a9-9097-e6380badea8b'}
        response = requests.post(self.base_url+'relation/getChainRelationById',self.data)
        result = json.loads(response.text)
        self.assertEqual(result['status'],'200')
        self.assertEqual(result['message'],'操作成功')

    def testGetChainRelationByIdWrongAppkey(self):
        """Appkey错误"""
        self.data={"appkey":self.appkey+'a',
             "id":'94878eba-ddf0-41a9-9097-e6380badea8b'}
        response = requests.post(self.base_url+'relation/getChainRelationById',self.data)
        result = json.loads(response.text)
        self.assertEqual(result['status'], '101')
        self.assertEqual(result['message'],'appkey无效')

def createSuite():
        testunit = unittest.TestSuite()
        test_dir = './'
        discover=unittest.defaultTestLoader.discover(test_dir,pattern='*.py',
                                                         top_level_dir=None)
        for test_class in discover:
            for test_case in test_class:
                testunit.addTests(test_case)
        return testunit

if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d %H.%M.%S')
    rptname = './report/'+now+' result.html'
    with open(rptname,'wb') as rpt:
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=rpt,
                title=u"测试报告",
                description=u"执行结果"
            )
        runner.run(createSuite())