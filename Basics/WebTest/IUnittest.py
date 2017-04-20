#coding:utf-8
import unittest
import HTMLTestRunner
import time
import os

def createSuite():
    testunit = unittest.TestSuite()
    test_dir = './'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test*.py',
                                                     top_level_dir=None)
    for test_class in discover:
        for test_case in test_class:
            testunit.addTests(test_case)
    return testunit

if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d %H.%M.%S')
    rptname = './'+now+' result.html'
    with open(rptname,'wb') as rpt:
        runner = HTMLTestRunner.HTMLTestRunner(
                stream=rpt,
                title=u"测试报告",
                description=u"执行结果"
            )
        runner.run(createSuite())