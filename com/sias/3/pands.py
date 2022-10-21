
import pandas as pa
# 默认情况下，是按照从索引0开始的，同时，也可以自己定义索引

# 0     1
# 1    23
# 2     4
# 3     6
# 4     7
# dtype: int64
# RangeIndex(start=0, stop=5, step=1)
print(pa.Series([1,23,4,6,7]))
print(pa.Series([1,23,4,6,7]).index)
print(pa.Series([1,23,4,6,7]).values)
print(pa.Series([1,23,4,6,7])[2])

dev_mv=pa.read_excel(r'D:\豆瓣电影数据.xlsx')
# print(dev_mv.head())
# print(dev_mv.iloc[0])
print(dev_mv.drop(38737))
print(dev_mv.tail())
print(dev_mv[dev_mv['产地']=='中国大陆'][:5])