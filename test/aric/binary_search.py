#折半查找
#查找有序数列中是否存在数字29
# 注意：移动指针是移动到mid+1或mid-1,不是移动到mid.

#4.0写成一个函数
def binary_search(a,b):
    b_len=len(b)
    left=0
    right=b_len-1
    mid=(left+right)//2
    while(left<=right):
        if(b[mid]>a):
            right=mid-1
        elif(b[mid]<a):
            left=mid+1
        else:
            print("找到该数字")
            break
        mid=(left+right)//2
    if(left>right):
        print("找不到该数字")
b=[10,14,18,20,21,23,26,29,32]
a=30
binary_search(a,b)

#3.0如果中间数小于29，向后查找，如果中间数大于29，向前查找
# b=[10,14,18,20,21,23,26,30,32]
# b_len=len(b)
# left=0
# right=b_len-1
# mid=(left+right)//2
# print(mid)
# while(left<=right):
#     if(b[mid]>29):
#         right=mid-1
#     elif(b[mid]<29):
#         left=mid+1
#     else:
#         print("找到该数字")
#         break
#     mid=(left+right)//2
# if(left>right):
#     print("找不到该数字")
# 注意：移动指针是移动到mid+1或mid-1,不是移动到mid.

#v2.0找到数列中间数
# b=[10,14,18,20,21,23,26,29,32]
# b_len=len(b)
# left=0
# right=b_len-1
# mid=(left+right)//2
# print(b[mid])

# #v1.0 比较两个数字是否相等
# b=int(input("b="))
# a=29
# if(a==b):
#     print("两个数字相等")
# else:
#     print("两个数字不相等")






