"""
在绑定属性时，如果我们直接把属性暴漏出去，虽然写起来很简单，但是没办法检验参数，导致可以把成绩随便改
"""
class Student(object):
    pass
s = Student()
s.score = 9999
print(s.score)
"""
这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()
来获取成绩，这样，在set_score()方法里，就可以检查参数：


"""
class Teacher(object):
    def get_salary(self):
        return self.__salary
    def set_salary(self, salary):
        if not isinstance(salary,int):
            raise ValueError('salary must be an integer')
        if salary < 0 :
            raise ValueError('salary must be greater than 0')
        self.__salary = salary

t = Teacher()
t.set_salary(10000)
print(t.get_salary())
# 会报错  salary must be greater than 0
# t.set_salary(-10000)
# print(t.get_salary())

"""
还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的：

@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
于是，我们就拥有一个可控的属性操作：
"""
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student1()
s.score = 60
print(s.score)