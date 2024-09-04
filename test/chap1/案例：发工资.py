import random
tol = 10000
for i in range(1,21):
    if tol > 0:
        scr = random.randint(1, 10)
        if scr>4:
            tol-=1000
            print(f'向员工{i}发放工资1000元，账户余额{tol}')
        else:
            print(f'员工{i}，绩效分为{scr},低于5，不发工资，下一位')
    else:
        print('工资发完了，下个月再领吧。')
        break