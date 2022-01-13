class Things:
    def __init__(self,num,name,price,quan):
        self.num=num
        self.name=name
        self.price=price
        self.quan=quan
    def Price(self):
        return self.price
    def prnid(self):
        print('商品编号:',self.num,'品名:',self.name,'价格:',self.price,'数量:',self.quan)
thing1 = Things('01','西游记',22,'10')
thing2 = Things('02','红楼梦',40,'10')
thing3 = Things('03','水浒传',15,'10')

thing1.prnid()
thing2.prnid()
thing3.prnid()

ZONG=(thing1.Price()+thing2.Price()+thing3.Price())
print('三种商品的总金额为：',ZONG)
