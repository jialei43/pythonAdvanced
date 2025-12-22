"""
Python内建的filter()函数用于过滤序列。

和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，
filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""

# 例如，在一个list中，删掉偶数，只保留奇数，可以这么写
my_list = [1, 2, 4, 5, 6, 9, 10, 15]
conversion_list = list(filter(lambda x: x % 2 == 0, my_list))
print(conversion_list)

# 把一个序列中的空字符串删掉，可以这么写：
list2 = ['A', '', 'B', None, 'C', '  ']
print(list(filter(lambda x: x and x.strip(), list2)))