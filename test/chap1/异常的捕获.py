try: # 执行此代码，检测异常
    f = open("123.txt","r",encoding="UTF-8")
except FileNotFoundError as e: # 如果有异常，执行此处。except之后可省略，就变成了捕获所有异常
    print("文件不存在，将读取模式转换为写入模式")
    print(f"异常形式为{e}")
    f = open("123.txt","w",encoding="UTF-8")
else: # 未发现异常，执行此处
    print("未出现异常")
finally: # 无论有无异常，都执行
    print("无论有没有异常，我都执行")
    f.close()

