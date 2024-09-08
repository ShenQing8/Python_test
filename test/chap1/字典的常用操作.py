my_dict = {'张三': 99, '李四': 88, '王五': 77}
# 新增或更改元素
my_dict['赵六'] = 66
print(f'添加元素后，字典内容为{my_dict}')
my_dict['王五'] = 55
print(f'更改元素后，字典内容为{my_dict}')

# 删除元素
del my_dict['赵六']
print(f'删除元素后，字典内容为{my_dict}')
score = my_dict.pop('王五')
print(f'取出的元素为{score}')

# 清空元素
my_dict.clear()
print(f'清空元素后，字典内容为{my_dict}')

# 获取全部的key
my_dict = {'张三': 99, '李四': 88, '王五': 77}
keys = my_dict.keys()
print(f'字典所有的key为{keys}')

# 遍历
for key in keys:
    print(f'1、字典所有的key对应的value为：{key}：{my_dict[key]}')

for k in my_dict:
    print(f'2、字典所有的key对应的value为：{k}：{my_dict[k]}')

# 统计元素数量
print(f'元素数量为：{len(my_dict)}')