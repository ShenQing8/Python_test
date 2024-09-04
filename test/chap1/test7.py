#python支持系列解包赋值
a,b=10,20
print(a,b)
a,b=b,a
print(a,b)
print('-------------')
m,n,q=1,2,3
print(m,n,q)
m,n,q=n,q,m
print(m,n,q)
print('-'*20)
i=5
for i in range(5):
    print(i)
print(i)