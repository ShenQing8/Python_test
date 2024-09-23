# 水一下，懒了

from pymysql import Connection

# 构建到MySQL数据库的链接
conn = Connection(
    host="lcoalhost",       # 主机名（IP）
    port=3306,              # 端口
    user="root",            # 账户
    password=""             # 密码
)

print(conn.get_server_info())


# 关闭链接
conn.close()
