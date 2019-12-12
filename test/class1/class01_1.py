# -*- coding:utf-8 -*-
# @Time     :2019/11/6 0006 15:54
# @Author   :Lemon_huahua
#@File      :c01_1.py
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"*",i,"=",i*j,'','\t ',end='')
    print("")
