"""一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序: 
1> 完成随机的分配 
2> 获取办公室信息 (每个办公室中的人数，及分别是谁)
"""
import random
ofice = [[],[],[]]
teachter = ["a","b","c","d","e","f,","g","h"]
for a in teachter:  # 遍历所有的老师
    name = random.randint(0,2)  # 随机抽取一个办公室
    ofice[name].append(a)   #  将老师放到办公室中
# print(ofice)
i = 1
for b in ofice:  #遍历所有的办公室
    print("%d个办公室有%d个老师"% (i,len(b)))  #  输出遍历后的办公室
    for a in b:    # 将分好办公室的老师一个一个遍历出来
        print(a)
    i += 1
print(ofice)



