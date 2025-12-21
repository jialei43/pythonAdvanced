"""
面向对象最基本的概念就是类(Class)和实例(Instance),必须牢记类是抽象的模板，比如student类
，而实例是根据类创建出来的一个个的具体的对象

1、类的定义  Class Student(object) object表示的是Student继承于object
"""
from dataclasses import dataclass, field
from typing import List


# 类的定义
@dataclass
class Student(object):

    def __init__(self, name, age, number, score):
        self.name = name
        self.age = age
        self.number = number
        self.score = score

    @property
    def getname(self):
        return self.name
    @property
    def getage(self):
        return self.age
    @property
    def getnumber(self):
        return self.number
    @property
    def getscore(self):
        return self.score

    def getProperties(self):
        return self.name, self.age, self.number, self.score


s = Student('zhangsan', 26, 10086, 90)
if __name__ == '__main__':

    print(f'{s.getname}')
    print(s.getProperties())

