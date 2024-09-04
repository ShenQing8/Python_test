lst=[1,'str',3.14,'嗯？']

#在列表的最后增加 一个 元素
print(lst,id(lst))
lst.append(666)
print(lst,id(lst))
#在列表最后追加一堆元素
lst.extend([1,2,3])
print(lst)

#在指定下标处插入一个元素
lst.insert(2,666)
print(lst,id(lst))

#统计列表中元素的数量
count = lst.count(666)
print(count)

#取出并删除指定下标的元素
s=lst.pop(1)
print(lst,id(lst))
print(s)

#删除第一个出现的指定元素,删除成功则返回None,未找到则报错
'''
k=lst.remove(666)
print(lst,id(lst))
print(k)
'''
#可使用循环删除全部的指定元素
while 666 in lst:
    lst.remove(666)
print(lst)

#逆序
print(lst.reverse())
print(lst,id(lst))

#拷贝
new_lst=lst.copy()
print(new_lst)
#也可用list进行拷贝
new_lst2=list(lst)
print(new_lst2)

#清空列表,但是不删除列表
lst.clear()
print(lst)
#直接删除列表
del lst
# print(lst)