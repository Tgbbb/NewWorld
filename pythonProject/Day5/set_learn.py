# 集合的定义方法,集合特点，集合中元素不重复，无序
# a = set{} 空集合的定义方式
# a = {‘aa’,‘bb’} 有数据的集合的定义方式
# 集合会自动去掉重复值

# 一些集合的简单运算,in和not in
# 将字符串转为集合
# a = 'abc'
# set(a)
# 将数组转为集合，用set{list}去重
# 比如
tgb = [1, 2, 1, 3, 2, 4]
bgt = set(tgb)
print(bgt)
# 一些集合运算符
# a-b,集合a中包含，而集合b不包含的元素
# a | b 取并集
# a & b 取交集
# a ^ b 不同时包含a与b的元素

# 一些集合的方法
# add（）添加，a.add（）
# update() 添加，有就不添加，没有就添加，a.update（）
# remove() 移除，a.remove（‘b’）
# clear（），清空集合中的元素,a.clear()
# len(a),计算集合的长度
# intersection(),取交集的方法,a.inersection(b)
# union()取并集