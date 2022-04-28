# 类（class）和对象(object)是两种以计算机为载体的计算机语言的合称。对象是对客观事物的抽象，类是对对象的抽象。类是一种抽象的数据类型。它们的关系是，对象是类的实例，类是对象的模板。
class Person:
    age = 28  # 类的属性
    __name = '唐铬彬'  # 双下划綫是类的私有变量，只能在类的内部中去使用

    def print_name(self):  # self就是对象本身的意思，self.后面可以调用所有对象内容的数据以及方法
        print(self.__name)
        self.tgb = 'bb'

    def test__self(self):
        self.__name = 'Tgb'
        print(self.__name)

    @classmethod
    def classmethod_learn(cls):  # !类方法，不用实例化对象直接调用,类同其他类中的方法，cls就是类的本身。
        print(cls.age)

    @staticmethod
    def staticmethod_learn():  # !静态方法，不需要参数，如果需要调用类属性，就直接 类名.属性（参数）
        print("现在的名字叫：TGB")
        print(Person.__name)


if __name__ == '__main__':  # 作为该文件使用，其他文件调用该模块时不生效，没有这个，其他文件调用该模块就会都执行
    # 实例化过程:一个实例化的对象赋给一个变量
    person = Person()

    # 实例化后的应用
    print(person.age)
    # print(person.__name)  # 双下划线为类中的,可以类里面声明方法去引用
    person.print_name()  # 调用类中的方法
    person.test__self()  # 调用类中的方法
    # !!!实例化对象可以使用类中所有的属性和方法
    Person.classmethod_learn()  # 类方法的实际应用例子，直接用类名Person调用类方法，不用实例化对象
    Person.staticmethod_learn()  # 静态方法的实际应用例子，直接用类名Person调用静态方法

# 封装：构造方法将内容封装到对象中，然后通过对象直接或者self间接获取被封装的内容,具体例子参考init_learn的注释
# 继承：子类继承父类所有的属性和方法,参考文件animal.py
# 多态：重写父类的方法,参考文件animal.py
