
import unittest2

from web_auto.SeleniumTest2.lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    suite=unittest2.defaultTestLoader.discover("./TestCase","*Test.py")
    # unittest2.TextTestRunner().run(suite)
    path="report/Testreport.html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file,verbosity=1,title="自动化测试报告",description="测试环境：Chorme",tester="changcheng").run(suite)

