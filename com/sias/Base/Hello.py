# 1.类型判断
print("你好")
name = "张三"
print(type(name))
# 2.类型转换
a = 12
print(type(str(a)))
b = "34"
c = str(b)
print(type(c))
d = "233"
e = int(d)
print(type(e))

# 3.占位符的拼接
name1 = "胡育林"
age = 22
score = 34.43
print("我的名字叫做：%s，年龄：%d，取得的分数是：%f" % (name1, age, score))
print(f"我的名字叫做：{name1} 年龄：{age} 取得的分数是：{score}")
print("数据的乘积：%s" % (age * 2))
print("这个类型是 %s" % (type("zhangsan")))
# 4.数字的宽度问题
age1 = 34.3253
print("宽度变成5，%5d" % age1)
print("宽度变成5，%5.2f" % age1)
# 5.数据的输入,在输入的数据里面获的都是字符串类型
input1 = input("请你输入一个整数：")
print(f"整数的内容是{input1},类型是{type(int(input1))}")

import random

num=random.randint(1, 10)
print(num)
