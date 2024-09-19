"""
多态是指同一行为，使不同对象获得不同状态
定义父类中含有哪些方法，子类对这些方法进行实现，但实现方式不同

抽象类（接口）：
    包含抽象方法的类。
    抽象方法是：没有具体的实现方法（pass）

抽象类的作用：
    多用于顶层设计（设计标准），以便子类具体实现。
    也是对子类的一种软性约束，要求子类必须复写父类的一些方法
    并配合多态使用，获得不同的工作状态
"""


# 父类，即接口
class AC:
    def make_cold(self):
        pass

    def make_hot(self):
        pass

    def weave_lr(self):
        pass

    # 接口有，但可以不用
    def weave_ud(self):
        pass

    def weave_around(self):
        pass


# 定义不用的子类
class MEAD(AC):
    def make_cold(self):
        print("美的制冷")

    def make_hot(self):
        print("美的制热")

    def weave_lr(self):
        print("美的左右摆风")

    def weave_ud(self):
        print("美的上下摆风")


class GREE(AC):
    def make_cold(self):
        print("格力制冷")

    def make_hot(self):
        print("格力制热")

    def weave_lr(self):
        print("格力左右摆风")

    def weave_around(self):
        print("格力环绕摆风")


def prt(ac: AC):
    ac.weave_ud()
    ac.weave_around()

# 创建对象
my_mead = MEAD()
my_gree = GREE()

prt(my_mead)
prt(my_gree)
