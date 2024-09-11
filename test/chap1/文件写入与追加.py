import time

f = open("wight.txt","w",encoding="utf-8")

f.write("123456")

# time.sleep(5)# 程序休眠5秒
# f.flush()# 刷新，是内存中的数据存到硬盘中

f.close()

# 追加
f = open("wight.txt","a",encoding="utf-8")
f.write("\n456789")
f.close()