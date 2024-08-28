#eval函数使用示例
a='1.11+5'
print(eval(a))
print('------------------')
age=eval(input('请输入您的年龄：'))
print(age,type(age))
height=eval(input('请输入您的身高：'))
print(height, type(height))
print('--------------------')
hello='北京欢迎你'
print(hello,type(hello))
print(eval('hello'),type(eval('hello')))
