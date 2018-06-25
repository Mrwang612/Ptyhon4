"""
"""
# dict1 = {"name":"zhangsan","age":18,"boy":True}
# print (type (dict1))
# name = dict1["name"]
# print (name)
# dict1["name"] = "wangmazi"
# dict1["name1"] = "就是这么溜"
# print(dict1)
dict1 = {"name":"zhangsan","age":18,"boy":True}
"""增加键值对"""
# dict1["name"] = "haha"
# dict1["name1"] = "hello"   # 如果键值对存在就会修改键值对的值 , 如果不存在 就会添加一个键值对
# print(dict1)
"""删除键值对"""
# # del dict1["name"]   # 删除指定key对应值元素
# a = dict1.pop("name")  # 删除指定key的值 并返还
# print(a)
# dict1.clear()    # 清空字典
# print(dict1)
"""修改键值对"""
# dict1["he"] = 19   # 如果键存在 会修改键的值  键不存在 就会添加一个
#  dict1["name"] = 19
# print(dict1)
"""查询键值对"""
# a = dict1["age"]   # 根据键取值 键值对不存在的会报错
# for b in dict1.items():   # 可进行遍历,获取所有的(键,值)
#     print(b)


