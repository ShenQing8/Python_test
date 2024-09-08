"""
位置传参
关键字传参
缺省参数
不定长参数
"""
def prt(name, sex, age):
    print(f'姓名：{name}，性别：{sex}，年龄：{age}')
# 位置传参
prt('小美', '女', 18)
# 关键字传参
prt(sex='男', name='小李', age=19)

# 缺省参数
# def prt2(name, sex='女', age):,缺省的部分要在后面
def prt2(name, age, sex='女'):
    print(f'姓名：{name}，性别：{sex}，年龄：{age}')
prt2('小王', 19)
prt2('小张', 19, '男')

# 不定长传参
def prt3(*args):# 位置传参
    print(f'内容是：{args}，类型是：{type(args)}')
prt3(1, 2, 3, 'hello', True)
def prt4(**kwargs):
    print(f'内容是：{kwargs}，类型是：{type(kwargs)}')
prt4(name='小穗', sex='女', age=18)
