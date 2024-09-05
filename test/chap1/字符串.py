# name = '张三'
# age = 18
# print(f'{name}今年\n{age}岁')
my_str = 'Python easy'
# my_str[7] = 'E'，不可直接修改字符串里的值，只能重新赋一个字符串
print(f'{my_str.index('t')}')

new_str = my_str.replace('e','E')
print(new_str)

#str.split(分割规则)，按照分割规则分割字符串，若空着，则按空格分割
#lt = my_str.split()
lt = my_str.split('t')
print(f'my_str经过split分割后含有元素{lt},类型是{type(lt)}')

#str.strip，会返回去除后的字符串，不会改变原字符串
my_str2 = '    1122Python12 easy122  '
my_str3 = my_str2.strip()
print(f'my_str2经过strip后去除首尾空格，得到{my_str3}')
my_str4 = my_str3.strip('12')
print(f'my_str3经过strip后去除首尾\'1\'和\'2\'，得到{my_str4}')
