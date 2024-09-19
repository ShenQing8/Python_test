"""
私有成员定义：
    在前面加上__，则表示私有
    即外部不能直接使用
"""
class Phone:
    # 5g开关
    is_5g_on = None

    def __is_5g_enable(self):
        return bool(self.is_5g_on)

    # 判断5g是否开启
    def __check_by_5g(self):
        if self.__is_5g_enable():
            print("5g已开启")
        else:
            print("5g已关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_by_5g()
        print("正在通话中")

phone = Phone()
phone.is_5g_on = True
phone.call_by_5g()
