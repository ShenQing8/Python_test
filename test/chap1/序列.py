s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print()
for i in range(-len(s),0):
    print(i,s[i],end='\t')
print()
#切片操作
s1=s[0:len(s):2] #切片[起始位置 : 结束位置(不包含) : 切片长度]
print(s1)
print(s[::-1])#利用切片操作逆序字符串
print(s[-1:-len(s)-1:-1])
print(max(s))
print(min(s))
print('h' in s)
print(s.index('w'))#第一次在序列中出现的位置
print(s.count('o'))#在序列中出现的总次数