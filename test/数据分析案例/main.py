"""
传入文件地址，获取获取数据
数据分析与计算
绘图
"""
from file_reader import FileReader, TextFileReader, JsonFileReader
from data_type import Source
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 获取1、2月数据
jan = TextFileReader("D:/Python_Data/sale/2011年1月销售数据.txt")
feb = JsonFileReader("D:/Python_Data/sale/2011年2月销售数据JSON.txt")
jan_source: list[Source] = jan.file_reader()  # 得到1、2月数据，类型：list[Source]
feb_source: list[Source] = feb.file_reader()
total_source: list[Source] = jan_source + feb_source

# 将1、2月每天的销售额汇总
money_dict = {}
for source in total_source:
    if source.date in money_dict.keys():
        money_dict[source.date] += source.money
    else:
        money_dict[source.date] = source.money

# 绘制1、2月销售额的柱状图
bar = Bar(init_opts=InitOpts(theme=ThemeType.VINTAGE))

"""添加x、y轴数据，x轴为日期，y轴为销售额"""
bar.add_xaxis(list(money_dict.keys()))
bar.add_yaxis("销售额(单位：亿)", list(money_dict.values()), label_opts=LabelOpts(is_show=False))

bar.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        min_=30000,
        max_=120000
    )
)

bar.render("1、2月份销售额.html")
