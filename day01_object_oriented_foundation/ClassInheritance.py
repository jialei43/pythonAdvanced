"""
本节学习类的继承
创建类的格式：
    class 类名：
    class 类名():
    class 类名(Object):
类的继承：
    格式：class 类名(被继承类名)
"""


# 定义父类
class Father(object):
    def __init__(self, sex):
        self.sex = sex

    def walk(self):
        print('爱散步')


# 子类继承父类，会继承父类所有成员属性和方法
class Child(Father):
    pass


child = Child('女')
child.walk()
print(f'child的性别:{child.sex}')
