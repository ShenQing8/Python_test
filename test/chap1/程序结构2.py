#模拟登陆界面
i=0
while i<5:
    name = input('请输入用户名：')
    pswd = input('请输入密码：')
    if name=='name' and pswd=='123456':
        print('登陆成功！')
        break
    else:
        i+=1
        print('用户名或密码错误，您还有',5-i,'次机会')
        continue
else:
    print('已输入错误5次')