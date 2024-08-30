for i in range(0,4):
    for j in range(0,4):
        print('* ',end='')
    print()

print('-'*20)

for i in range(0,5):
    for j in range(0,i+1):
        print('* ',end='')
    print()

print('-'*20)

for i in range(0,5):
    for j in range(-5,-i):
        print('* ',end='')
    print()

print('-'*20)

ROW=5
'''
for i in range(0,ROW):
    for j in range(i,ROW-1):
        print('  ',end='')
    for j in range(0,1+2*i):
        print('* ', end='')
    print()
'''#优化如下
for i in range(0,ROW):
    print('  '*(ROW-i-1)+'* '*(1+2*i))

print('-'*20)

row=eval(input('请输入要打印菱形的行数（奇数）：'))
while not row%2:
    row=eval(input('请输入一个奇数：'))
on=(row+1)//2
low=(row-1)//2
'''
for i in range(0,on):
    for j in range(i,on-1):
        print('  ',end='')
    for j in range(0,1+2*i):
        print('* ', end='')
    print()
for i in range(0,low):
    for j in range(0,1+i):
        print('  ',end='')
    for j in range(0,2*low-1-2*i):
        print('* ',end='')
    print()
'''#优化如下
for i in range(0,on):
    print('  '*(on-i-1)+'* '*(1+2*i))
for i in range(0,low):
    print('  '*(1+i)+'* '*(2*low-2*i-1))

print('-'*20)

'''
for i in range(0,on):
    for j in range(i,on-1):
        print('  ',end='')
    for j in range(0,1+2*i):
        if j==0 or j==2*i:
            print('* ', end='')
        else:
            print('  ',end='')
    print()
for i in range(0,low):
    for j in range(0,1+i):
        print('  ',end='')
    for j in range(0,2*low-1-2*i):
        if j==0 or j==2*low-2*i-2:
            print('* ',end='')
        else:
            print('  ',end='')
'''
for i in range(0,on):
    print('  '*(on-i-1)+'* ',end='')
    if i==0:
        print()
    else:
        print('  '*(2*i-1)+'* ')
for i in range(0,low):
    print('  '*(1+i)+'* ',end='')
    if i != low-1:
        print('  '*(2*low-2*i-3)+'* ')
    else:
        pass

