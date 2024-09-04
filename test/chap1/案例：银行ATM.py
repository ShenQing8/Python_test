name = 'lxr'
money = 1000000000
def menu():
    print('-'*10,'主菜单','-'*10)
    print(f'{name}您好，欢迎来到星穹银行！\n'
          f'查询余额\t请按1\n'
          f'存款\t\t请按2\n'
          f'取款\t\t请按3\n'
          f'退出\t\t请按0')
    print('-'*28)
    return eval(input())

if input('请输入您的姓名：')==name:
    while 1:
        ret = menu()
        match ret:
            case 0:
                break
            case 1:
                print(f'当前账户余额{money}元')
            case 2:
                add = eval(input('请输入要存款金额：'))
                money += add
                print(f'存款成功！'
                      f'当前账户余额{money}元')
            case 3:
                move = eval(input('请输入取款金额：'))
                if money >= move:
                    money -= move
                    print(f'取款成功！'
                          f'当前账户余额{money}元')
                else:
                    print(f'余额不足！'
                          f'当前余额{money}元')
else:
    print('姓名错误，请重新输入！')