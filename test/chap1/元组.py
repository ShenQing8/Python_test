#元组不可被修改

#定义方法
t1 = (8,'hello',True,'hello',"hello",(1,2,3),[1,2,3])
t2 = ()     #定义空元组
t3 = tuple()#定义空元组
print(f't1,类型{type(t1)},元素{t1}')
print(f't2,类型{type(t2)},元素{t2}')
print(f't3,类型{type(t3)},元素{t3}')

#定义只含有一个元素的元组
t4 = ('hello',) #要带一个逗号

#index,count,len
print(f'True在元组中下标为{t1.index(True)}')
print(f'\'hello\'在元组中共有{t1.count('hello')}个')
print(f'元组t1共有{len(t1)}个元素')

#元组不可修改，但元组内部的列表可以修改
print(f't1的内容是{t1}')
t1[6][0] = 4
t1[6][1] = 5
t1[6][2] = 6
print(f't1的内容是{t1}')
#同理，列表里的元组内容不可修改