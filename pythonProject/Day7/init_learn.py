# init，类对象内置方法，生成对象时调用，可以用来进行一些初始化操作，不需要显示去调用，系统会默认去执行，如果用户自己没有定义，就执行默认的构造方法。类想要类中的变量是灵活的，就使用定义构造方法中的参数
# 就是构造方法！
class Hero:
    def __init__(self, name, blood, price):  # 定义构造方法时，定义了要传的参数，这就是封装
        self.name = name
        self.blood = blood
        self.price = price

    def print_hero(self):
        print("英雄的名字是", self.name)
        print("英雄的血量是", self.blood)
        print("英雄的初始金币是", self.price)


hero = Hero("Link", 1500, 300)
hero.print_hero()
