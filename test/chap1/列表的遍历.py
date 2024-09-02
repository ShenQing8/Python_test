lst=[1,'str',3.14,'嗯？']
#直接for循环进行遍历
for item in lst:
    print(item)

#for循环，结合range和len函数进行索引遍历
for i in range(0,len(lst)):
    print(i,'---->',lst[i])

#enumerate：枚举
#使用enumerate函数遍历
for index,item in enumerate(lst,1):#输出编号默认从0开始，也可以手动设置其他数值
    print(index,'---->',item)