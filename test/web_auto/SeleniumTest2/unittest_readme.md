
批量执行测试用例
if __name__ == '__main__':
    suite=unittest2.defaultTestLoader.discover("./TestCase","*Test.py")
    # unittest2.TextTestRunner().run(suite)
    path="report/Testreport.html"
    file=open(path,'wb')
    HTMLTestRunner(stream=file,verbosity=1,title="自动化测试报告",description="测试环境：Chorme",tester="changcheng").run(suite)
二进制文件，测试报告详细程度，报告的标题，报告的正文，测试人员
5

#技术实验
1.导包 unittest2 单元测试框架
2.测试用例类必须继承unittest2.TestCase类
3.每个测试用例的方法名必须以test开头才能执行，普通的只能被调用才会执行
测试用例的执行顺序与名字有关
4.重写父类的两个方法setUp()和tearDown()
setUp()    在每个测试用例前，要做的预置条件
tearDown() 在每个测试用例后，要做的场景还原
5.if __name__ == '__main__':
      unittest2.main()
在当前文件中右键运行，才会执行下面的语句，在其他文件中运行，不会执行。
光标必须在main函数中

6.重写父类中的setUPClass()和tearDownClass()
setUPClass()    在类中所有方法前，要做的预置条件
tearDownClass() 在类中所有方法前，要做的场景还原
7.BaseTestCase
创建一个父类，包含setUPClass()和tearDownClass()
8.数据驱动 批量注册10个用户
8.1.准备一个excel表格，保存10个用户信息
8.2编写代码读取excel中的内容
导入库      import csv
制定路径    path=r"D:\learngit\web_auto\SeleniumTest2\test_data\register_testcases.csv"
(当路径中存在反斜线时，在字符串前面加一个r，用来表示不再把反斜线看成转义字符)
打开csv文件  with open(path) as file:
读取内容     data=csv.reader(file)
打印内容
        list=[]
        i=0  
        for row in data:
            if i==0:                  去除表头
                pass
            else:
                list.append(row)
            i=i+1
        return list
8.3把读取到的内容分别传入测试用例中，执行10次
for row in data:
    self.driver.find_element_by_name("username").send_keys(row[0])    
9.循环读取数据时如果中间报错怎么办？ 数据驱动测试ddt
import ddt                       导入ddt包
@ddt.ddt                         类前加装饰器，表明时数据驱动类
class registerTest3(BaseTestCase):
    table = reader("register_testcases.csv")
    @ddt.data(*table)            方法前加装饰器，将数据源转为为多个参数
    def test_register(self,row): 
        self.driver.find_element_by_name("username").send_keys(row[0])
       


10.文件路径  
base_path=os.path.dirname("__file__)            
path=base_path.replace("func","test_data/"+filename)


