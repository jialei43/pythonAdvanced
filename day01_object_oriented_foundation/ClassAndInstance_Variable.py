"""
一般来说，实例变量用于存储每个实例特有的数据，而类变量用于存储类的所有实例共享的属性和方法
"""


class Dog:
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance


dog1 = Dog('土豆')
dog2 = Dog('毛豆')
# 实例的变量的name 不同，是每个变量特有的数据
print(f'dog1的名字：{dog1.name}')
print(f'dog2的名字：{dog1.name}')

# 类的属性 是所有实例共享的 ,俩个实例的king是一样的，如果一个修改了kind，另外一个kind也会改变，因为类的属性是所有实例共享的

print(f'dog1的king:{dog1.kind}')
print(f'dog2的king:{dog2.kind}')
Dog.kind = 'hjksdhfjk'
print(f'dog1的king:{dog1.kind}')
print(f'dog2的king:{dog2.kind}')
