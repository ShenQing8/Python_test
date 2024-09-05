#集合是无序的，因此不支持下标索引
#且内容不重复

#定义集合
set1 = {}
set2 = set() #定义空集合
print(f'set1的元素有{set1},类型为{type(set1)}，因此不可用={set1}的方法定义空集合')
print(f'set2的元素有{set2},类型为{type(set2)}')
set3 = {1,2,3,'Python',1,2,3,'Python',1,2,3,'Python'}
print(set3)

#添加元素
set3 = {1,2,3,'Python'}
set3.add('Easy')
print(set3,type(set3))

#移除元素
set3.remove(3)
print(set3)

#随机取出一个元素
ret = set3.pop()
print(ret)

#清空集合
set3.clear()
print(set3)

#取两个集合的差集
set4 = {1,2,3}
set5 = {1,4,5,6}
ret = set4.difference(set5)
print(ret)

#将集合1含有的集合2的元素删掉，集合2不变
set5.difference_update(set4)
print(f'集合1{set5}')
print(f'集合2{set4}')

#得到一个新集合，合并两个集合的元素，原有的两个集合内容不变
set4 = {1,2,3}
set5 = {1,4,5,6}
set6 = set4.union(set5)
print(f'新集合{set6}')
print(f'原集合1{set4}\n'
      f'原集合2{set5}')