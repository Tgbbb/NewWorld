# 无参函数调用
# def speak():
#     print('无参函数调用测试成功')
#
#
# speak()
# __________________________________________________________________________________________

# 有参函数调用
# def speak1(name, sex):
#     print('我的名字是{}，我的性别是{}'.format(name, sex))
#
#
# speak1('唐铬彬', '男人')
# speak1('唐洛琳', '女孩')
# __________________________________________________________________________________________

# # 数字相加的函数,可以返回return多个值，函数遇到return停止
# def Jiafa(a, b):
#     c = a + b
#     b = a * b
#
#     return c, b
#
#
#
# num, num2 = Jiafa(10,10)
# print(num)
# print(num2)
# __________________________________________________________________________________________

# # 递归函数简例
# def recursion(n):
#     print(n)
#     if n == 10:
#         return
#     recursion(n + 1)
#
#
# recursion(1)
# __________________________________________________________________________________________

# 局部变量只能函数内部用，外部不能用，除了return这个值
# def func():
#     x = 20
#     return x
#
#
# num = func()
# print(num)
# __________________________________________________________________________________________

# 全局变量可以在函数内部使用
# x = 20
#
#
# def func1():
#     print("x is :", x)
#
#
