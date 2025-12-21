"""
多继承演示：
    格式：
        class 类名(类名1,类名2...)
"""


# 师傅类
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')


class School(object):
    def __init__(self):
        self.kongfu = '黑马煎饼果子配方'

    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼')


# 先继承谁，就使用谁
class Prentice(School, Master):
    pass


class Prentice2(School, Master):
    def __init__(self):
        self.kongfu = '独创煎饼果子技术'

    def make_cake(self):
        # 调用父类的方法
        # School.make_cake(self)
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼')

    #  学校类的方法调用
    def school_make_cake(self):
        # 将self对象修改为School
        School.__init__(self)
        School.make_cake(self)

    # 师傅类方法调用
    def master_make_cake(self):
        # 将self对象修改为Master
        Master.__init__(self)
        Master.make_cake(self)


prentice = Prentice();
prentice.make_cake()
print(prentice.kongfu)
# 打印子类继承父类，调用的顺序
print(Prentice.__mro__)
print(Prentice.mro())

# 如果子类有与父类重名的方法，会使用子类的重写方法
prentice2 = Prentice2();
prentice2.make_cake()
print(prentice2.kongfu)

prentice2.master_make_cake()
prentice2.school_make_cake()
prentice2.make_cake()
print('-' * 34)


class Prentice3(School):
    def __init__(self):
        self.kongfu = '独创煎饼果子技术'

    def make_cake(self):
        # 调用父类的方法
        # School.make_cake(self)
        self.__init__()
        print(f'使用{self.kongfu}制作煎饼')

    #  学校类的方法调用
    def school_make_cake(self):
        # super只适用于单继承
        super().__init__()
        super().make_cake()


prentice3 = Prentice3()
prentice3.make_cake()
prentice3.school_make_cake()
