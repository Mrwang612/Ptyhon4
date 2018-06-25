"""从键盘中输入5个学生的名字，存储到列表中，
然后打印出每个学生名字中的第2个字母"""
# i =1
# list = []
# while i <= 5:
#     name = input("请输入名字:")
#     list.append(name)
#     i += 1
# for b in list:
#     print(b[1])
"""从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生"""
# i =1
# list1 = []
# import random
# while i <= 5:
#     name = input("请输入名字:")
#     list1.append(name)
#     i += 1
# d = random.randint(0,4)
# print("%s同学去打扫" % list1[d])
"""老师分配办公室的应用练习

输入办公室个数
输入老师的个数
然后将了老师分配到办公室，保证每个办公室至少一个，如果"""

# # coding=utf-8
# import random
# # 办公室数量默认是0
# room_nums = 0
# # 教师数量默认是0
# teacher_nums = 0
# while True:
#     # 办公室个数
#     r_nums = input("请输入办公室的个数：")
#     # 老师的个数
#     t_nums = input("请输入老师的个数：")
#
#     # 如果教师数目大于等于办公室数目，才退出循环，并赋值给room_nums、teacher_nums
#     # 否则重新输入
#     if int(r_nums) <= int(t_nums):
#         room_nums = int(r_nums)
#         teacher_nums = int(t_nums)
#         break
#     print("教室数低于办公室数，请重新输入")
#
# # 创建办公室列表，即创建一个嵌套列表
# rooms = []
# while room_nums>=1:
#     rooms.append([])
#     room_nums -= 1
#
# # 创建老师列表，并添加老师
# teachers = []
# while teacher_nums>=1:
#     teacher_nums -= 1
#     teachers.append("teacher%d"%(teacher_nums+1))
# # 开始安排办公室
# # 1.先随机选出三位老师，依次放到办公室中
# for room in rooms:
#     # 随机选出一名老师，注意teachers长度会变
#     index = random.randint(0,len(teachers)-1)
#     # pop方法弹出一个元素，并列表中删除
#     teac = teachers.pop(index)
#     room.append(teac)
#
# # 2.将剩下的老师，再随机分配
# for teacher in teachers:
#     room_index = random.randint(0, len(rooms)-1)
#     rooms[room_index].append(teacher)
# print("分配结束后：", rooms)


"""从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母"""
# list = []
# for i in range(5):
#     i = input("请输入名字:")
#     list.append(i)
# for b in list:
#     print (b[1])


"""从键盘获取5个学生的名字，然后随机抽出一名学生去打扫卫生"""
# import random
# list = []
# for i in range(5):
#     i = input("请输入名字:")
#     list.append(i)
# a = random.randint(0,4)
# print (list[a])

"""完成字符串的逆序以及统计

设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
打印出字符串长度
使用切片逆序打印出字符串"""

# str1 = input("请输入长度低于三十31的字符串")
# if len(str1) < 31:
#     print(str1)
# else:
#     print("请重新输入")
# print(str1[::-1])
"""有10个球分别3红、3蓝、4白，现需要将这10个球放入这3个盒子，
要求每个盒子至少有一个白球，请用程序实现"""
import random
red_ball = ["red", "red" , "red"]  # 红   #
white_ball = ["white" ,"white" ,"white","white" ]  # 白
blue_ball =["blue" ,"blue","blue" ]  # 蓝
list1=[[],[],[]]
for list in list1:
    list.append(white_ball.pop())
balls = red_ball + white_ball + blue_ball
for ball in balls:
    a = random.randint(1,(len(list1) -1))
    list1[a].append(ball)
print(list1)
print(list1)



