# 类，设计表格
"""
定义类的方法：
class 类的名称:
    类的属性（变量），成员变量

    类的行为（函数），成员方法
    def 方法(self, 参数):
        方法体

    self表示对象本身的意思
    只有通过self，成员方法才能访问成员变量
    self不占用形参位置，传参时无需理会
"""
class Student:
    name = None
    gender = None
    age = None

    def say_hi(self, msg):
        print(f'大家好，我叫{self.name}，{msg}')

# 对象，打印表格
student = Student()
# 给对象赋值，填写表格
student.name = "坤坤"
student.age = 28
student.gender = "男"

student.say_hi("哎呦~你干嘛~~啊~啊~")
