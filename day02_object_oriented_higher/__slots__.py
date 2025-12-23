"""
正常情况下，当我们定义一个class，创建一个class的实例后，我们可以给实例绑定任何属性和方法，这就是动态语言的
灵活性，先定义class

但是，如果我们想要限制实例的属性怎么办？比如只允许对Student实例添加 name 和 age属性
为了达到这种限制的目的，python允许在定义的时候，定义一个特殊的变量 __slots__,来限制class实例能添加的属性

‼️‼️使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
"""
from types import MethodType


class Student(object):
    pass


# 然后尝试给实例绑定一个属性
s = Student()
s.name = 'John'
print(s.name)


# 还可以尝试给是实例绑定一个方法
def set_age(self, age):
    self.age = age


# 将set_age函数绑定给实例s，且命名为set_age
s.set_age = MethodType(set_age, s)
s.set_age(10)
print(s.age)

# 但是，给一个实例绑定的方法，对另外一个实例是不起作用的，因为绑定的对象是实例级别，对其他实例是不可见
s2 = Student()
# s2.set_age(20)
"""
当调用set_age()方法会报如下错误，会告诉你属性不存在
Traceback (most recent call last):
  File "/Users/jialei/PycharmProjects/pythonAdvanced/day02_object_oriented_higher/__slots__.py", line 26, in <module>
    s2.set_age(20)
    ^^^^^^^^^^
AttributeError: 'Student' object has no attribute 'set_age'
"""


# 由于上面单独给实例绑定方法，对其他实例是不可见的，为了给所有实例绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score


"""
通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class
加上功能，这在静态语言中很难实现
"""
Student.set_score = set_score
s.set_score(100)
print(s.score)
s2.set_score(200)
print(s2.score)

print('-' * 34)
"""
使用__slots__
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：


"""


class Teacher(object):
    __slots__ = ['name', 'age']

    def __init__(self):
        pass


# 创建实例
t = Teacher()
t.name = 'John'
t.age = 23
"""
Traceback (most recent call last):
  File "/Users/jialei/PycharmProjects/pythonAdvanced/day02_object_oriented_higher/__slots__.py", line 72, in <module>
    t.score = 100
    ^^^^^^^
AttributeError: 'Teacher' object has no attribute 'score'
"""
# t.score = 100
print(t.name, t.age)

# ‼️‼️使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class MathTeacher(Teacher):
    pass
mt = MathTeacher()
mt.score = 100
print(mt.score)

# 🫵🫵除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class EnglishTeacher(Teacher):
    __slots__ = ['score', 'gender']

et = EnglishTeacher()
et.name = 'zack'
et.age = 25
et.gender = 'man'
et.score = 100
"""
Traceback (most recent call last):
  File "/Users/jialei/PycharmProjects/pythonAdvanced/day02_object_oriented_higher/__slots__.py", line 110, in <module>
    et.address = '昌平区'
    ^^^^^^^^^^
AttributeError: 'EnglishTeacher' object has no attribute 'address'
从错误可以看出类没有这个属性address可以被我们使用
"""
# et.address = '昌平区'