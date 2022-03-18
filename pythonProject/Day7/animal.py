class Animal:
    def __init__(self):
        pass

    def eat(self):
        print("作为一只动物，我每天都要吃东西")


class Dog(Animal):  # Dog这个类继承了Animal这个类，继承了父类所有的属性方法
    pass


class Cat(Animal):
    def eat(self):  # 这就是重写多态！
        print('我是一只猫，只喜欢吃猫粮')


dog = Dog()
dog.eat()

cat = Cat()
cat.eat()
