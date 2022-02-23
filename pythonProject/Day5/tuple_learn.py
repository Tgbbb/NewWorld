# 元祖内的元素不能修改,定义元祖用小括号（）
# 只有一个元素的元祖定义方式，后面要加逗号，举例，tuple = （‘唐铬彬’,）  如果不加逗号，定义出来是原始的数据类型
names = ('Tgb', 'Friday', 'Elden Ring')
Things = ('name', 'date', 'game')
# 如何获取元祖中的元素，下标，同数组
# for循环同样可以获取元祖中的值
print(names[0])

# 元祖的操作，内部不能操作，但可以相加,相乘
new_tuple = names + Things
print(new_tuple)

# 元祖只能直接整个删除，将内存里的变量名甚至都删掉了,举例 del new_tuple

# len,元祖*int型，in，not in都可以适用
# 元祖内的内置函数
# max
# min
# list（tuple），可以将元祖转换成数组