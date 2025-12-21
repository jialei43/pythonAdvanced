"""
魔法函数
__init__() 在实例化对象时，传入的参数会绑定到类的属性上面
__str__() 返回一个字符串，当打印实例对象时，会执行打印返回的字符串
__del__() 在程序结束时自动调用
"""


class MagicFunction(object):
    # 创建对象时，自动调用
    def __init__(self, name, age, genere, address):
        self.name = name
        self.age = age
        self.genere = genere
        self.address = address

    # 打印对象时，自动被调用
    def __str__(self):
        return (f'{self.name}, {self.age}, {self.genere}, {self.address}')

    def __del__(self):
        print(f'实例对象{self}---已销毁')


# 全局对象变量程序结束后才会被销毁
magic = MagicFunction("花花", 23, "男", "北京市昌平区")
print(magic)


# 局部变量的对象，方法结束生命周期结束，会被回收
def createMaficFunction():
    magic2 = MagicFunction("刘鹏", 28, "男", "北京市昌平区")
    print(magic2)


createMaficFunction()
# del magic 不手动调用，系统也会自动调用
# 当实例对象被销毁后不能再使用
# print(magic.name)
