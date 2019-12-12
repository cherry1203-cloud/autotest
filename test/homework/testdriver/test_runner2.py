import unittest
import os,csv
if __name__ == '__main__':
    #获取配置文件路径
    path=os.getcwd()
    file_path=os.path.abspath(os.path.dirname(path)+os.path.sep+".")+"\config\config2.csv"
    file=open(file_path,"r")
    table=csv.reader(file)
    num=0
    for row in table:
        if num>0 and int(row[2])==1:
            test_dir=row[0]
            filename=row[1]
            print(filename)
            discover=unittest.defaultTestLoader.discover(test_dir,filename)
            runner=unittest.TextTestRunner()
            runner.run(discover)
            
        num=num+1
