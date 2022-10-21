# 1.判断语法
age = input("请输入一个数据：")
if int(age) >= 30:
    print("你已经进入了中年")
else:
    print("你还是青年")
#  2.多个嵌套
height = input("请你输入你的身高：")
if int(height) > 190:
    print(f"你有资格打篮球，身高是{height}")
    print(f"类型是{type(height)}")
    if int(input("请输入你的年龄")) > 34:
        print("继续执行")
    else:
        print("跳出这次选择")
else:
    print("你的身高不够要求")
