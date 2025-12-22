"""
函数（方法）的类型注解 - 形参注解
def 函数方法名(形参名:类型,形参名:类型,......) ->类型：
"""


# x-int,y-int 返回数据类型int
def add(x: int, y: int) -> int:
    return x + y


print(add(2, 3))


def fun(data: list):
    print(data)


fun([1, 2, 3, 4])
