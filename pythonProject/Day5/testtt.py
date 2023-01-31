info = {'语文': 100, '数学': 90, '英语': 95}
print(info.values())
info.keys()
for i in info.keys():
    print('小明的{}成绩是{}'.format(i,info[i]))