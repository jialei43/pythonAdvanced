"""
多态：同一个函数在不同的情形下，触发不一样的状态
"""


class Animals(object):
    def spark(self):
        pass


class Dog(Animals):
    def spark(self):
        print("汪汪汪")


class Cat(Animals):
    def spark(self):
        print("喵喵喵")


class Pig(Animals):
    def spark(self):
        print("哼哼哼")

class Audio(object):
    def spark(self):
        print('我喜欢唱歌')
def animal_spark(animal: Animals):
    animal.spark()


dog = Dog()
cat = Cat()
pig = Pig()
audio = Audio()

animal_spark(dog)
animal_spark(cat)
animal_spark(pig)
animal_spark(audio)
