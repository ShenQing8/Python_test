# lst=[1,'str',3.14,'嗯？']
# #可用while循环
#
# #直接for循环进行遍历
# for item in lst:
#     print(item)
#
# #for循环，结合range和len函数进行索引遍历
# for i in range(0,len(lst)):
#     print(i,'---->',lst[i])
#
# #enumerate：枚举
# #使用enumerate函数遍历
# for index,item in enumerate(lst,1):#输出编号默认从0开始，也可以手动设置其他数值
#     print(index,'---->',item)

lst = [1,2,3,4,5,6,7,8,9,10]
#定义函数，取出列表中的偶数
def while_get():
    i = 0
    ret = []
    while i < len(lst):
        if not lst[i] % 2:
            ret.append(lst[i])
        i += 1
    print(f'通过while循环，取出偶数{ret}')

def for_get():
    ret = []
    for i in range(0,len(lst)):
        if not lst[i] % 2:
            ret.append(lst[i])
    print(f'通过for循环，取出偶数{ret}')

while_get()
for_get()