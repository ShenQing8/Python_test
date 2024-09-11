f = open("D:/github Code/乱码.txt","r",encoding="utf-8")
# 读取文件内容
print(f'文件内容是：\n{f.read()}，\n类型：{type(f.read())}')
# 文件读取后光标会停留在读取结束的位置
f.seek(0,0)# 将光标位置设为开头
"""
f.seek(offset, whence),f指的是file(或文件名)

offset: 将光标向前移动n个位置
whence: 参考位置，一般参数为0,1,2
0 ：将开头作为参考位置
1 ：将当前作为参考位置
2 ：将末尾作为参考位置
"""
print(f'{f.read().count('y')}')
print(f'{f.tell()}')# 获取光标当前位置

f.seek(0,0)
print(f'读取一行得到：{f.readline()},类型：{type(f.readline())},可见读取一行时会将‘\\n’也读出来')

f.seek(0,0)
lst = f.readlines()
# print(f'读取全部行：{f.readlines()},\n类型：{type(f.readlines())}')
print(f'读取全部行：{lst},\n类型：{type(lst)}')

f.seek(0,0)
# 遍历
for line in f:
    print(f'一次读取一行数据：{line}，类型是：{type(line)}')

# 关闭文件
f.close()

# 通过with open语法打开文件，可自动关闭
with open("D:/github Code/乱码.txt","r",encoding="utf-8") as f:
    for line in f:
        print(line)
