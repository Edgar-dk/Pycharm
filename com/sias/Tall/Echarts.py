from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
lin = Line()
lin.add_xaxis(["中国", "美国", "日本"])
lin.add_yaxis("GDP", [30, 20, 25])
# 设置全局配置项set_global_opts来设置,
lin.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    # 设置工具箱，可以用很多的工具去使用
    toolbox_opts=ToolboxOpts(is_show=True),
    # 设置实图展示
    visualmap_opts=VisualMapOpts(is_show=True),
)
lin.render()
