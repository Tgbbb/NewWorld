# 数组和字典的表现形式的区别
# 一位学生的成绩，语文100，数学90，英语95
# 我如果用数组表现，就是如下例
# subjects = ['语文', '数学', '英语']
# score = [100, 90, 95]
# for sum in range(len(subjects)):
#     print('{}科目的分数是{}'.format(subjects[sum], score[sum]))
# # 该方式极其麻烦
# # 所以用字典
# info = {'语文': 100, '数学': 90, '英语': 95}
# 用type查看类型，为dict
# key和value支持的数据类型
# key用字符串和数字，value支持python任何的数据类型

# 一个字典里面，key不能重复
# 如何获取字典里的值 变量名[key]
# 添加、修改字典里的值，变量名[key] = value，存在修改，不存在添加
# 删除字典里的值，del 变量名[key]
# 清空字典，变量名.clear
# items遍历字典，一个变量去遍历时获取的是元组类型
# for i in info.items():
#     print(i)
# # 当两个变量去获取遍历时，就是两个值，如下例：
# for i,l in info.items():
#     print(i, '---', l)
# # keys():遍历字典里的key，还可以用list（）将keys转换成数组
# # values():遍历字典里的values,还可以用list（）将keys转换成数组
# # pop(key),删除一个键值对，返回这个key的value值
# list(info.keys())


# 数组里有字典的操作，如下例：
# Dict_in_List = [{'DarkSouls1': 90, 'Darksouls2': 85, 'DarkSouls3': 100}, {'BloodBorne': 110, 'Persona5': 150}, {'FinalFantasy': 100, '2077': 0}]
# print(Dict_in_List[0]['DarkSouls3'])

# --------------------------------------------------------------------------------------------------------------

# 题目：购物车，程序运行后，让购物车输入水果的编号，然后增加水果的数量
# ShopingCar = {0: '梨子', 1: '苹果', 2: '西瓜', 3: '桃子'}
# FruiltNum = int(input('请输入水果的编号（0,1,2,3）：'))
# FruiltKucun = {0: 0, 1: 0, 2: 0, 3: 0}
#
#
# if FruiltNum in list(FruiltKucun.keys()):
#     FruiltKucun[FruiltNum] += 1
#
#
# print('添加商品成功，{}的库存现在为{}'.format(ShopingCar[FruiltNum], FruiltKucun[FruiltNum]))
# print(FruiltKucun)

# --------------------------------------------------------------------------------------------------------------
# 购物车实现，完整版！
Disc = {0: '艾尔登法环', 1: '血源诅咒', 2: '地平线II：西之绝境', 3: '女神异闻录5', 4: '塞尔达传说：荒野之息', 5: '黑暗之魂III', 6: '魔物猎人：The World', 7: '马力欧奥德赛'}
ShopCar = {'艾尔登法环': 0, '血源诅咒': 0, '地平线II：西之绝境': 0, '女神异闻录5': 0, '塞尔达传说：荒野之息': 0, '黑暗之魂III': 0, '魔物猎人：The World': 0, '马力欧奥德赛': 0}
Disc_num = list(Disc.keys())
while True:
    print('当前购物车内：', str(ShopCar))
    Start = int(input('请问您想干什么：进行购物>1，退出程序>2:'))
    if Start == 1:
        while True:
            print('商品对应的编号是:', str(Disc))
            Disc_inputnum = int(input('请输入您想添加商品的对应编号,不想继续购物输入99:'))
            if Disc_inputnum == 99:
                break
            elif Disc_inputnum not in Disc_num:
                print('没有找到对应商品，请重新输入')
                continue
            else:
                ShopCar[Disc[Disc_inputnum]] += 1
                print('添加成功，购物车展示如下:', str(ShopCar))
                End = int(input('继续购物>1,退出购物>2:'))
                if End == 1:
                    continue
                elif End == 2:
                    break
    elif Start == 2:
        break


