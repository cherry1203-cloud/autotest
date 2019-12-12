#冒泡排序
#将一组无需的数列变成一组有序的数列
#完成多趟比较
list_a=[7,3,6,9,5,2]
list_len=len(list_a)
for i in range(0,list_len-1):
    for i in range(0,list_len-1):
        if list_a[i]>list_a[i+1]:
            temp=list_a[i]
            list_a[i]=list_a[i+1]
            list_a[i+1]=temp
    # j=j+1
print (list_a)

#完成一趟比较
# list_a=[7,3,6,9,5,2]
# list_len=len(list_a)
# print(list_len)
# for i in range(0,list_len-1):
#     if list_a[i]>list_a[i+1]:
#         temp=list_a[i]
#         list_a[i]=list_a[i+1]
#         list_a[i+1]=temp
# print (list_a)

# #v1.0 比较两个数字，并将最大数排在后面
# a=input("第一个数：")
# b=input("第二个数：")
# if(a>b):
#     t=a
#     a=b
#     b=t
# print(a,b)

