def func1():
    print("func1开始")
    num = 1/0
    print("func1结束")

def func2():
    print("func2开始")
    func1()
    print("func2结束")

def main():
    print("main开始")
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常情况是：{e}")

main()
