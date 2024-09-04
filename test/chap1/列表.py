#列表是可变数据类型

#创建方式：
#1、使用[]直接创建
#2、使用函数list(object)创建,list是将object转换成列表类型
lst1=[1,'str',3.14,'嗯？']
lst=[[1,2,3],[4,5,6]]
print('',lst[0],'\n',lst[1])
str='123456'
lst2=list(str)
lst3=['bsdihv']
print(lst1)
print(lst2)
print(lst3)

#适用于序列的函数也适用于列表
print(len(lst1))
print(len(lst2))
print(len(lst3))

#删除列表
del lst1
#print(lst1)   #name 'lst1' is not defined