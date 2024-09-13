"""
json是一种轻量级的数据交互格式，采用完全独立于编程语言的文本格式来存储数据（就是字符串）
json无非是字典或者内部元素为字典的列表
"""
import json

# json的格式转化
mem = [{"name":"张三", "age":18}, {"name":"李四", "age":19}, {"name":"王五", "age":20}]
p1 = {"name":"张三", "age":18}
# 把python数据转为json数据
j1 = json.dumps(mem, ensure_ascii=False)# 当有中文时，带上ensure_ascii=False,表示不按照ASCII码表进行翻译
print(f'内容：{j1}\n类型：{type(j1)}')
j2 = json.dumps(p1,ensure_ascii=False)
print(f'内容：{j2}，\n类型：{type(j2)}')
# 把json数据转为python数据
mem2 = json.loads(j1)
print(f'内容：{mem2}，\n类型：{type(mem2)}')
p2 = json.loads(j2)
print(f'内容：{p2}，\n类型：{type(p2)}')
