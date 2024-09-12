__all__ = ['test1']

def test1(a, b):
    print(a + b)

def test2(a, b):
    print(a - b)

# test1(2,3)
# 以下只会在当前文件运行中才会运行，外部导入不运行
if __name__ == '__main__':
    test1(2,3)
