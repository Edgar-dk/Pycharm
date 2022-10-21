"""
演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()
# 准备数据
data = [
    # 指定这个城市的数字，只要是这个数字的话，就按照颜色显示在地图上
    ("北京", 99),
    ("上海", 199),
    ("湖南", 299),
    ("台湾", 399),
    ("广东", 499)
]
# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        # 开始设置地图的颜色
        is_show=True,
        # 手动修改地图的颜色
        is_piecewise=True,
        # 指定颜色，在这个范围内，颜色是这中
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]
    )
)

# 绘图
map.render()