import random

# 题目计算1——100数字相加

# times = 1
# limitimes = 100
# num = 1
# while times < limitimes:
#     times += 1
#     num = num + times
# print(num)

# ------------------------------------------分割符-----------------------------------------------------分割符
# break 终止循环，continue 跳出循环(执行continue，后面的代码都不会执行)

# a = 0
# while True:
#     a+=1
#     print('a 的值是 {}'.format(a))
#     if a > 5:
#         break

# ------------------------------------------分割符-----------------------------------------------------分割符
# 题目：打印1——100能被2整除的数字

# num2 = 0
# num = 0
# while num2 <= 100:
#     num2 += 1
#     if num % 2 == 0:
#         print(num)
#     num += 1

# num1 = 1
# while num1 <=100:
#     if num1 % 2 == 0:
#         print('{}能被2整除'.format(num1))
#     num1 += 1

# num1 = 1
# while num1 <=100:
#     if num1 % 2 == 0:
#         print('{}能被2整除'.format(num1))
#     num1 += 1
#     if num1 % 2 != 0:
#         continue
#     print('这个数被2整除时才执行，这个数是{}'.format(num1))

# ------------------------------------------分割符-----------------------------------------------------分割符
# 题目：随机数1-10，你拥有5次机会猜这个数，猜对了打印：你猜对了，5次都猜错了打印：你的机会用完了。

rNum = random.randint(1, 10)
times = 5
# print('随机数是{}'.format(rNum))
while times > 0:
    # try为抛出异常的语句，出现异常时执行except的代码，此处抛出异常后依然在循环里，except后面跟的异常类型，无异常时执行else的代码
    try:
        gNum = int(input('请猜猜这个数是多少，输入1-10之间的整数,您还有{}次机会:'.format(times)))
    except ValueError:
        print('喂！叫你输入1-10之间的整数')
    else:
        if gNum == rNum:
            print('呵呵，运气真好，猜对了╮(╯▽╰)╭')
            break
        elif gNum > 10:
            print('喂！叫你输入1-10之间的整数')
            continue
        elif gNum < 1:
            print('喂！叫你输入1-10之间的整数')
            continue
        elif gNum == rNum:
            print('呵呵，运气真好，猜对了╮(╯▽╰)╭')
            break
        times -= 1
        if times == 0:
            print('你的机会用完了哟！(*^▽^*)')
