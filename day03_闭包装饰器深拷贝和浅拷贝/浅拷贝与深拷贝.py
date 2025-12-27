'''
演示赋值和浅拷贝的原理
'''
# a 是一个引用，指向了列表内存地址
a = [1,2,3,4,5,6,7,8,9]
# b 是一个引用，指向了列表内存地址
b = [11,22,33,44,55,66,77,88,99]
# data 是一个引用执行[a,b]的内存地址，[0x2fee,0x3b4d]
data = [a,b]
# 将data的指向地址赋值给data2，所以data和data2的指向地址一致
data2 =data
print(id(data))
print(id(data2))

'''
可变类型与 不可变类型
不可变对象：字符串，元组，数值（整形，浮点型）
可变对象：列表，字典，集合
'''
import copy

# 不可变对象 ：内容发生改变，地址发生改变
a = 'python'
print(a)
print(id(a))
a += '123'
print(a)
print(id(a))

# 可变 内容发生改变，地址不变
b = []
print(b)
print(id(b))
b.append(1)
print(b)
print(id(b))

# 普通赋值:date_mycopy与b指向同一空间
date_mycopy = b
print(id(b))
print(id(date_mycopy))
print('*' * 20)
# 浅拷贝：date和date_copy指向不同地址
date_copy = copy.copy(date_mycopy)
print(id(date_mycopy))
print(id(date_copy))

print('*' * 20)
a = 3
b= a
print(id(a))
print(id(b))

# = 赋值永远是将地址赋值给到新的对象，所以id是一致的

"""
以下是 Python 中主要的不可变数据类型：

1. 基础数值类型 (Numbers)
所有的数值类型都是不可变的。

int（整型）

float（浮点型）

complex（复数）

bool（布尔型：True 和 False）

注意： 当你执行 a = 1; a = a + 1 时，并不是把内存里 1 的位置改成了 2，而是新开辟了存放 2 的空间，让 a 指向它。

2. 序列类型 (Sequences)
str（字符串）：字符串中的单个字符是不允许修改的。

tuple（元组）：元组一旦初始化，其成员及其顺序就固定了。

bytes（字节序列）：只读的二进制数据。

3. 集合类型 (Sets)
frozenset（冻结集合）：它是 set 的不可变版本，一旦创建不能增删元素
"""