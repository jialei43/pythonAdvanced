"""
私有属性和私有方法：
    私有属性和方法不能被子类继承，不能被外部使用，只能在类内部访问
    格式：
        私有属性：__属性名称
        私有方法：__方法名称
    如果外部想使用私有属性和方法，只能通过公有方法进行返回私有的属性和方法
"""


class Person:
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        # self.__money = 50000
        self.__money = money

    def get_money(self) -> int:
        return self.__money

    def reduce_money(self, money: int) -> int:
        self.__money -= money
        return self.__money
    def __get_age(self) -> int:
        return self.age
    def inheritance_class_get_age(self) -> int:
        return self.__get_age()

class Student(Person):
    pass


class Teacher(Person):
    pass


s = Student('小明', 23, 50000)
# print(s.money)
print(s.get_money())
print(s.reduce_money(200))
# s.get_age()
print(s.inheritance_class_get_age())