#coding:utf-8
import unittest
import HTMLTestRunner
import time
import multiprocessing
import threading

def createSuite():
    testunit = unittest.TestSuite()
    test_dir = r'E:\Py3Study\Basics\WebTest'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test*.py',
                                                     top_level_dir=None)
    for test_class in discover:
        for test_case in test_class:
            testunit.addTests(test_case)
    print(testunit)
    return testunit

# def multi_createSuite():


if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d %H.%M.%S')
    rptname = 'E:\\Py3Study\\Basics\\WebTest\\'+now+' result.html'
    # with open(rptname,'wb') as rpt:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #             stream=rpt,
    #             title=u"测试报告",
    #             description=u"执行结果"
    #         )
    #     runner.run(createSuite())
    pool = multiprocessing.Pool(processes=4)
    suite = createSuite()
    rpt=open(rptname,'wb')
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=rpt,
            title=u"测试报告",
            description=u"执行结果"
        )
        pool.apply_async(runner.run(i))
    pool.close()
    pool.join()
    rpt.close()
