# lambda 定义的函数成为匿名函数
# 不能重复使用
# 无函数名，且函数体只能写一行
def test_func(compute):
    ret = compute(1, 1)
    print(ret)
test_func(lambda x, y: x+y)
