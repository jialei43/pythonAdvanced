"""
sorted(迭代器,key->函数(定义排序规则),reverse=True/False)
"""

my_list = [36, 5, -12, 9, -21]
sort_lsit = sorted(my_list, key=abs, reverse=False)
print(sort_lsit)

my_list2 = ['Credit', 'Zoo', 'about', 'bob']
# 将字符转换为小写后，进行比较
sort_lsit = sorted(my_list2, key=str.lower, reverse=False)
print(sort_lsit)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


L2 = sorted(L, key=by_name)
print(L2)
L3 = sorted(L, key=lambda x:x[0])
print(L3)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)
print(L2)
L3 = sorted(L, key=lambda x:x[1])
print(L3)
