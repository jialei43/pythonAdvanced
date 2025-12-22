"""
高阶函数：
    变量可以指向函数
以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
"""

from typing import Callable

x = abs(-10)
print(x)

# 函数名可以直接赋值给变量
f = abs
y = f(20)
print(y)


# 由以上得出函数可以赋值给变量，那么我们函数的变量再接收一个函数，理论上也是可以
# f:Callable[[int], int] 标注f的类型是函数
def add(x:int, y:int, f:Callable[[int], int]) ->int:
    return f(x) + f(y)


# 特别要记住此处传入的是函数名 abs而不是abs()函数方法
result = add(10, 20, abs)
print(result)
