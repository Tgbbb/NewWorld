# num1 = 10
# num2 = 5
# if num1 > num2:
#     print('num1就是比num2大')
#     num1 += 1
#     print('num1的值是：', num1)
# else:
#     print('num1还真不比num2大')

# ------------------------------------------分割符-----------------------------------------------------分割符

# age = int(input('朋友，请输入你的年龄:'))
# if 60 >= age >= 18:
#     print('尊贵的客人您好，请进入我们的专属服务通道')
# elif age >= 61:
#     print('大爷，咱这么大岁数了，就别整这么刺激的了吧！Σ(⊙▽⊙"a')
# elif 10 <= age <= 15:
#     print('小伙子，好好学习，天天向上！别TM天天看些花里胡哨的东西！[○･｀Д´･ ○]')
# elif age == 8:
#     print('这TM是八岁？！Σ(⊙▽⊙"a')
# else:
#     print('小朋友[○･｀Д´･ ○]，请立即退出！非礼勿视哦！')

# ------------------------------------------分割符-----------------------------------------------------分割符

UserName = 'admin'
PassWord = 'admin123'
InputUserName = input('请输入您的用户名：')
InputPassWord = input('请输入您的密码：')
if InputUserName == UserName and InputPassWord == PassWord:
    print('校验正确')
else:
    print('O(∩_∩)O，密码或用户名错误哟，铁汁~')
