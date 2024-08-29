#name=input('请输入您的姓名：')

#match相当于switch,但不需要break
"""
grade=input('请输入您的等级：')
match grade:
    case 'A':
        print('优秀')
    case 'B':
        print('良好')
    case 'C':
        print('中等')
    case 'D':
        print('及格')
    case 'E':
        print('不及格')
    case _:
        print('格式不正确')
"""

'''
for i in '10':
    print(i)
'''
#求100到999之间的水仙花数
#153 == 3**3+5**3+1**3
for i in range(100,1000):  #range(m,n)生成m到n的整数，包括m不包括n
    m=i%10
    n=i//10%10
    k=i//100%10
    if i==m**3+n**3+k**3:
        print(i)

#while 同理
s=0
for a in range(1,11):
    s+=a
    if a>10:
        break
else:
    print('程序正常执行',s)




