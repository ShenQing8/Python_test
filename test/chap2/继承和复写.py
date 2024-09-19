"""
class 类名（父类1，父类2，…………）:
    新内容（或直接pass)

    # 复写
    需要复写的变量或方法再重新写一遍
"""


class Phone2022:
    producer = "SM"


class Phone2023:
    producer = "S"
    is_5g_enable = True
    is_idcard = True

    def cam_indeed(self):
        print("行")


class Phone2024(Phone2022, Phone2023):
    producer = "M"
    is_flying = True

    def NFCwrite(self, msg: str):         # 变量注解
        print(f"NFC写入, 内容：{msg}")

    def NFCread(self, msg: str):          # 变量注解
        print(f"NFC读取, 内容：{msg}")

    def add(self,x: int, y: int) -> int:  # 函数返回值注解
        return x + y

myphone = Phone2024()
myphone.NFCwrite("门禁")
myphone.NFCread("开锁")
print(myphone.add(2, 3))
print(myphone.producer)

