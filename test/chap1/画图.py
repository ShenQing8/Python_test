from pyecharts.charts import Line
from pyecharts.options import TitleOpts, ToolboxOpts, LegendOpts,VisualMapOpts

line = Line()# 得到一个空的折线图基底
line.add_xaxis(["中国", "美国", "日本"])# x轴数据
line.add_yaxis("GDP", [30, 20, 10])# y轴数据

# 配置全局设置
line.set_global_opts(
    title_opts=TitleOpts(title="国家GDP",subtitle="仅展示三个国家",pos_left="center",pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True,min_=0,max_=50),
)

line.render()

