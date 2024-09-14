from pyecharts.charts import Map
from pyecharts.options import TitleOpts, ToolboxOpts, VisualMapOpts
import json

# 导入数据
f = open("E:/data/beijing.txt", "r", encoding="UTF-8")
data_json = f.read()

# 关闭文件
f.close()

# 转化数据
data = json.loads(data_json)  # 取得北京市的疫情数据
data_source = data["RECORDS"]
data_list = []
for data_list_pre in data_source:
    pName = data_list_pre["provinceName"]
    confirm_count = data_list_pre["confirmedCount"]
    data_list.append((pName, confirm_count))

# print(data_list)

# 创建绘图对象
map = Map()

# # 添加绘图数据
map.add("北京市疫情数据", data_list, "china")

# 全局设置
map.set_global_opts(
    title_opts=TitleOpts(title="北京市疫情变化图", pos_left="center", pos_bottom="99%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True,
                                 is_piecewise=True,
                                 pieces=[
                                    {"min": 0, "max": 49},
                                    {"min": 50, "max": 149},
                                    {"min": 150, "max": 399},
                                    {"min": 400, "max": 649},
                                    {"min": 650, "max": 899},
                                    {"min": 900, "max": 1150}
                                 ])
)
# 绘图
map.render("北京疫情趋势.html")
