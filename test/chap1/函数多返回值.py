def test1():
    return 1, 2, 3, 'hello', True
# 多返回值被多值接收时，依次为相应的值
a, b, c, d, e = test1()
print(a, b, c, d, e)
# 多返回值被一值接收时，用元组存储
x = test1()
print(x, type(x))
