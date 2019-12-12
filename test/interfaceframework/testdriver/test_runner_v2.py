#v4.0从配置文件中读取测试脚本，执行状态和执行顺序

#实验：对数据字典内容进行排序
# import operator
# dic2=[{"test3":"d://rr//tt","num":1},{"test2":"d://rr//tt","num":3},{"test1":"d://rr//tt","num":2}]
# dicn=sorted(dic.items(),key=operator.itemgetter(1))
# print(dicn)
# for key,value in dicn:
#     print (key)
#     print (value)
# for fn in dicn:
#     print(fn[0])
# list2=sorted(dic2,key=operator.itemgetter("num"))
# # print(dicn)
# for dicn in list2:
#     # print(dicn)
#     n=0
#     for key,value in dicn.items():
#         if n==0:
#             print(key)
#             print(value)
#             n=n+1

#把配置文件中的内容放进字典中
# import csv
# file=open("D:\learngit\interfaceframework\config\config1.csv","r")
# table=csv.reader(file)
# listd=[]
# n=0
# for row in table:
#     n = n + 1
#     dic = {}
#     if(n>1):
#         dic[row[1]]=row[0]
#         dic["num"]=int(row[3])
#         # print(dic)
#         listd.append(dic)
# # print(listd)
# dicn=sorted(listd,key=operator.itemgetter("num"))
# for dic in dicn:
#     # print(dic)
#     i=0
#     for content in dic.items():
#         if i==0:
#             print ("fn:",content[0],"dir:",content[1])
#             fn=content[0]
#             dir=content[1]
#             i=i+1
#*************************v3.0驱动脚本程序***************************
import unittest
import csv
import operator

if __name__ == '__main__':
    #打开对应配置文件，进行读取运行顺序（构造字典列表）
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
            # print(dic)
            listd.append(dic)
    # print(listd)
    dicn=sorted(listd,key=operator.itemgetter("num"))
    for dic in dicn:
        # print(dic)
        i=0
        for content in dic.items():
            if i==0:
                print ("fn:",content[0],"dir:",content[1])
                fn=content[0]
                dir=content[1]
                discover = unittest.defaultTestLoader.discover(dir, pattern=fn)
                runner=unittest.TextTestRunner()
                runner.run(discover)
            i=i+1


