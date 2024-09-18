from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [60, 50, 40], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [70, 55, 46], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [90, 65, 60], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

bar4 = Bar()
bar4.add_xaxis(["中国", "美国", "英国"])
bar4.add_yaxis("GDP", [100, 70, 70], label_opts=LabelOpts(position="right"))
bar4.reversal_axis()

# 时间线
timeline = Timeline({"theme": ThemeType.DARK})

# 将4幅图添加进timeline中
timeline.add(bar1, "一")
timeline.add(bar2, "二")
timeline.add(bar3, "三")
timeline.add(bar4, "四")

# 自动播放
timeline.add_schema(
    play_interval=1000,     # 自动播放间隔，单位毫秒
    is_timeline_show=True,  # 显示时间轴
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环播放
)

# 画图
timeline.render("基础柱状图.html")
