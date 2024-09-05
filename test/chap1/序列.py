#序列指的是有序排列的数据容器，包括列表，元组，字符串
#三者都能进行切片操作
s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print()
for i in range(-len(s),0):
    print(i,s[i],end='\t')
print()
#切片操作,切片不会改变原先序列的值
s1=s[0:len(s):2] #切片[起始位置 : 结束位置(不包含) : 切片长度]
print(s1)
print(s[::-1])#利用切片操作逆序字符串
print(s[-1:-len(s)-1:-1])

print(max(s))
print(min(s))
print('h' in s)

print(s.index('h'))#第一次在序列中出现的位置
#print(s.index('v'))#ValueError: substring not found 不存在则会报错
print(s.find('orld'))#find函数可以用来找字符串，找到则返回所找字符串的第一个下标
print(s.find('v'))#找不到则返回-1

print(s.count('o'))#在序列中出现的总次数