class Student:
    name = None
    gender = None
    age = None

    # 初始化变量
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("构造方法在创建类对象时就自动执行")

    # __str__
    def __str__(self):
        return f'信息：{self.name}, {self.gender}, {self.age}'

    # __lt__,进行 > 和 < 比较
    def __lt__(self, other):
        return self.age < other.age

    # __le__,进行 >= 和 <= 比较
    def __le__(self, other):
        return self.age <= other.age

    # __ep__,进行 == 比较
    def __eq__(self, other):
        return self.age == other.age

stu1 = Student("坤坤", None, 28)
stu2 = Student("ikun", "未知", 12)
print(f'{stu1}\n{stu2}')              # 利用__str__显示信息
print(stu1 > stu2, stu1 < stu2)       # 利用__lt__进行大于和小于比较
print(stu1 >= stu2, stu1 <= stu2)     # 利用__le__进行大于等于和小于等于比较
print(stu1 == stu2)                   # 利用__eq__进行等于比较
