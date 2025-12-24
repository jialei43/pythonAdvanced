"""
定义一个闭包，用于求解方程的y与x值的变化，例如 y = ax + b
"""

from functools import wraps
from time import time


def solution(a=5, b=6):
    def solution2(x):
        return a * x + b

    return solution2


f = solution()
y = f(10)
print(y)


def func_count(x):
    @wraps(x)
    def func_count2():
        print("hello world")
        nonlocal x
        x += 1
        print(f'执行了{x}次')
        return x

    return func_count2


total = 0
f = func_count(total)
total = f()
total = f()
total = f()

"""
请使用装饰器方式来统计输出100000句"黑马程序员YYDS"的执行时间。
"""


def time1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        print(f'执行时间：{end - start}')

    return wrapper


@time1
def a():
    for i in range(100000):
        print("黑马程序员YYDS")


a()

"""
定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt。
"""
def suffix(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        txt_suffix =result + '.txt'
        print(f'字符串后缀:{txt_suffix}')
        return result
    return wrapper

@suffix
def string():
     return "project"

string()