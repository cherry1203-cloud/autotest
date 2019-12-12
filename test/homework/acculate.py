# -*- coding:utf-8 -*-
# @Time     :2019/11/12 0012 15:03
# @Author   :Lemon_huahua
#@File      :acculate.py

#M与N的数学运算：用户输入两个数 M 和 N，其中 N 是整数，计算M 和 N 的5种数学运算结果，并依次输出，（编程题）
# M=int(input ("M="))
# N=int(input("N="))
# print(M+N)
# print(M-N)
# print(M*N)
# print(M/N)
# print(M**N)


#用户输入矩形的长和宽，计算其面积并输出
# chang=float(input("长:"))
# kuan=float(input("宽："))
# area=chang*kuan
# print("area:",area)

'''
class area:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def cal_area(self):
        s=self.a*self.b
        return s
if __name__=="__main__":
    retangele_area=area(3,4)
    print(retangele_area.cal_area())
'''

#3位水仙花数计算：“3位水仙花数”是指一个三位整数，其各位数字的3次方和等于该数本身。
# 例如：ABC是一个“3位水仙花数”，则：A的3次方＋B的3次方＋C的3次方 = ABC。（编程题）
#
# for num in range(101,999):
#     i=num//100
#     j=num//10%10
#     h=num%10
#     if (i**3+j**3+h**3==num):
#         print (num)

# 打印100以内的斐波那契数列（编程题）
# a=0
# b=1
# s=a+b
# while (s<100):
#     print(s)
#     a=b
#     b=s
#     s=a+b

#打印九九乘法表（编程题）
# for j in range(1,9):
#     for i in range(1,j+1):
#
#         print(i,'*',j,"=",i * j,'',sep='\t',end='')
#     print()


#计算1+2+3...+98+99+100 （编程题）

# s=0
# for i in range(1,101):
#     s=s+i
# print(s)

#求1～100间所有偶数的和（亦可奇数和，使用while循环写）（编程题）
# i=2
# s=0
# while(i<=100):
#     s=i+s
#     i=i+2
# print(s)

#【作文题】 编写一个python程序，输入两个数，比较它们的大小并输出其中较大者。（编程题）
# a=int(input("a="))
# b=int(input("b="))
# if (a>b):
#     print(a)
# else:
#     print(b)

#【作文题】 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？（编程题）

# n = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             s = i * 100 + j * 10 + k
#             if (i!=j)&(i!=k)&(j!=k):
#                 n = n + 1
#                 print("第",n,"个数：",s)
# print("一共有",n,"个数")

#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在 第10次落地时，共经过多少米？第10次反弹多高？
# a=100
# s=0
# for i in range(0,10):
#     s=a+s
#     a=a/2
#     print(a)
# print(s)
