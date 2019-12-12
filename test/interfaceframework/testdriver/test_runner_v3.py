#v4.将脚本执行顺序和状态放在一起

import unittest
import csv
import operator

if __name__ == '__main__':
    #打开对应配置文件，进行读取运行顺序
    file=open("D:\learngit\interfaceframework\config\config1.csv","r")
    table=csv.reader(file)
    listd=[]
    n=0
    for row in table:
        n = n + 1
        dic = {}
        if(n>1):
            dic[row[1]]=row[0]
            dic["num"]=int(row[3])
            #将脚本运行状态数据放入字典
            dic["state"]=row[2]
            # print(dic)
            listd.append(dic)
    # print(listd)
    dicn=sorted(listd,key=operator.itemgetter("num"))
    for dic in dicn:
        # print(dic)
        if (dic["state"]=="Yes"):
            i=0
            for content in dic.items():
                print(content)
                if i==0 :
                    print ("要执行的文件：",content[0])
                    fn=content[0]
                    dir=content[1]
                    discover = unittest.defaultTestLoader.discover(dir, pattern=fn)
                    runner=unittest.TextTestRunner()
                    runner.run(discover)
                i=i+1