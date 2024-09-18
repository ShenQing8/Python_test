from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()

# 添加数据
bar.add_xaxis(["中国", "美国", "英国"])
# 将数据显示在右边
bar.add_yaxis("GDP", [60, 50, 40], label_opts=LabelOpts(position="right"))

# x,y轴翻转
bar.reversal_axis()

# 画图
bar.render("基础柱状图.html")
