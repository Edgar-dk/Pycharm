from typing import TextIO


def add(x, y):
    result = x + y
    print(f"{x}+{y}={result}")


a = add(1, 34)

print(type(a))

list_context = [1, "dshj", 90, 2, 1, 2, 2]

print(list_context.count(1))
list_context.extend([5, 5])
list_context.append(["ds", "io"])
list_context.insert(1, ["00000"])
print(list_context)
print(list_context[1])
print(list_context[-1])
print(list_context.index(90))

list_context1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_even = []
list_add = []

for i in list_context1:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_add.append(i)
print(list_even)

tuple_number = (1, [1, 3, "for"], 1, 5)
tuple_number[1][0] = "g"
index = 0
while index < len(tuple_number):
    print(tuple_number[index])
    index += 1
print(tuple_number.count(1))
print(tuple_number.index(5))
print("====================")
split = [1, 5, 6, 7, 8, 2, 4]
print(split[1:5])
split1 = (1, 4, 7, 3, 6, 9, 3)
print(split1[1:4])
print("============================")
my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
# 创建一个集合
my_set = set()
for i in my_list:
    my_set.add(i)
print(my_set)

info_dict = {
    "王力鸿": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "周杰轮": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "林俊节": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "张学油": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "刘德滑": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

for i in info_dict:
    if info_dict[i]["级别"] == 1:
        employee_info_dict = info_dict[i]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        info_dict[i] = employee_info_dict
print(info_dict)

with open("D:/1.txt", 'r', encoding='UTF-8') as f:
    # 在这个去读取数据的时候，是从上一个read的后面那个指针的位置开始读取的，没有数据的就，就代表着这个数据已经被读取完毕了
    print(f.readlines())
f1 = open("D:/1.txt", 'a', encoding='UTF-8')
f1.write("这个是文件的一部分")
f1.flush()


f2 = open("D:/2.txt", 'r', encoding='UTF-8')
f3 = open("D:/4.txt", 'a', encoding='UTF-8')
print("+++++++++++++++++++++++")
for i in f2:
    print(i)
    # i是一行数据，把数据读取出来之后，让进写的文件中
    f3.write(i)

f2.close()
f3.close()
