"""
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
"""
from functools import reduce


# 案例一：对列表的每个元素进行平方，形成新的列表

def squared(x):
    return x ** 2


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# map 方法返回来的是可迭代器，如果需要指定烈性的容器，需要进行指定转化
mapped = list(map(squared, my_list))
print(mapped)
mapped2 = list(map(lambda x: x ** 2,my_list))
print(mapped2)

# 案例二：将list中的数据转换为str类型

def conversion_str(x:int)->str:
    return str(x)

mapped = list(map(conversion_str, my_list))
print(mapped)
mapped2 = list(map(lambda x: str(x),my_list))
print(mapped2)

"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是
    格式：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

"""

# 比方说对一个序列求和，就可以用reduce实现：
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum =reduce(lambda x, y: x + y, list1)
print(sum)

# 案例二：將列表元素組合成一個字符串
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
product = reduce(lambda x, y: f'{x}{y}', list2)
print(type(product))
print(product)

# 案例三：將字符串轉換為數字
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(lambda x: DIGITS[x], s))

result = str2int(product)
print(type(result))

print(result)