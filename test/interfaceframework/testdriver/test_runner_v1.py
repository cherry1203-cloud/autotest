#测试 框架驱动程序v1.0
#从配置文件占领读取一个脚本文件进行调用
import csv
import unittest
if __name__ == '__main__':
    #从csv文件中读取相关路径和文件名
    file=open("D:\learngit\interfaceframework\config\config1.csv","r")
    table=csv.reader(file)
    num=0
    for row in table:
        num=num+1
        #v2.0增加脚本执行状态
        if num>1 and row[2]=="Yes" :
            testdir=row[0]
            pattern=row[1]
            discover=unittest.defaultTestLoader.discover(testdir,pattern=pattern)
            runner=unittest.TextTestRunner()
            runner.run(discover)

