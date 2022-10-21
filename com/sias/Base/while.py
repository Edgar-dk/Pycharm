# a = 1
# sum = 0
# while a <= 100:
#     sum += a
#     a += 1
#
# print(sum)
import random

num = random.randint(1, 100)

count = 0
flag = True
while flag:
    num_input = int(input("请你输入一个数"))
    if num_input == num:
        print("恭喜你猜中了")
        flag = False
    else:
        if num_input>num:
            print("")
