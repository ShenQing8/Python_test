# import my_module1
# my_module1.test1(5,6)
# my_module1.test2(2,3)

# 导入相同的函数名时，后导入的会覆盖前导入的
# from my_module1 import test1
# from my_module2 import test1
# test1(3,4)

# from         import 只能导入__all__所规定的列表里东西
# from my_module1 import *
# test1(2,3)
# test2(3,4)

