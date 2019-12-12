#测试框架驱动程序获取脚本执行顺序
#构造一个字典列表进行排序
# import operator
# dict1=[{"test1":"dir1","num":3},{"test2":"dir1","num":1},{"test3":"dir1","num":2}]
# print(sorted(dict1,key=operator.itemgetter("num")))

import unittest
import os, csv
import operator
if __name__ == '__main__':
    # 获取配置文件路径
    path = os.getcwd()
    file_path = os.path.abspath(os.path.dirname(path) + os.path.sep + ".") + "\config\config3.csv"
    file = open(file_path, "r")
    table = csv.reader(file)
    num = 0
    userinfo={}
    listinfo = []
    for row in table:

        if num > 0 and int(row[2]) == 1:
            userinfo[row[0]]=row[1]
            userinfo["order"]=int(row[3])

        if userinfo!={}:

            listinfo.append(userinfo)
        userinfo={}
        num = num + 1

    listinfo1=sorted(listinfo,key=operator.itemgetter("order"))
    print(listinfo1)
    for i in range(0,len(listinfo1)):
        print(listinfo1[i])
        n=0   #只读取字典一个键值对
        for test_dir,filename in listinfo1[i].items():
            if n==0:
                discover = unittest.defaultTestLoader.discover(test_dir, filename)
                runner = unittest.TextTestRunner()
                runner.run(discover)
                # print(key)
                # print(value)
            n=n+1

















