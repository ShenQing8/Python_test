fr = open("zhangdan.txt","r",encoding="utf-8")
fa = open("bill.txt.bak","a",encoding="utf-8")

# 存在小bug，如果名字中有“测试”也会被过滤掉
# for line in fr:
#     if "测试" not in line:
#         fa.write(line)

for line in fr:
    line = line.strip()# 将字符串前后的空格及\n都删去
    if line.split(',')[4] == "正式":  # 以逗号将各个元素分隔开，并将类型转换为列表
        fa.write(f"{line}\n")

fr.close()
fa.close()
