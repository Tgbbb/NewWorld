# # 数组定义用中括号 []
# names = ['唐铬彬', '雨宫莲', '小豆子']
# # 常用取数组中的数据的方法：1、下标 2、for循环
# print(names[0])
# for name in names:
#     print(name)
# # 获取数组的长度
# print(len(names))
#
# # 数组修改数据
# names[1] = '测试题换'
#
# # 数组删除数据，del[‘下标’]
# del names[1]
#
# # 数组直接+，-，*，÷，相加有前后顺序问题
# # 判断数据是否在数组中 举例: a = ‘唐铬彬'，a in [names] 返回一个布尔值
# print('唐铬彬' in names)


# append和extend，append仅在数组最后增加一个对象；extend直接延展数组，将一个数组的内容直接加在数组中
TestList1 = ['黑暗之魂1', '黑暗之魂2', '黑暗之魂3']
TestList2 = ['艾尔登法环', '血源诅咒', '恶魔之魂']

TestList1.append(TestList2)
print('这是append的效果：', TestList1)
TestList1.extend(TestList2)
print('这是extend的效果：', TestList1)

