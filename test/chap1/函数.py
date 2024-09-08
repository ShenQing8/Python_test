def add(x, y):
    """
    这是一个计算两数相加的函数
    :param x: 加数之一
    :param y: 加数
    :return: 返回相加后的结果
    """
    return x+y

print(f'1+1的结果是{add(1, 1)}')

# 变量的作用域，全局变量和局部变量
a = 10

def test1():
    print(a)

def test2():
    global a # global声明的变量将与全局变量相关联
    a = 20
    print(a)

test1()
test2()
print(a)
