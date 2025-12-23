"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，
创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
称为生成器：generator。
"""
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把雷彪生成的[]改成(),就创建了一个generator
# L是一个list
L = [x * x for x in range(10)]
# G是一个generator
G = (x * x for x in range(10))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# Traceback (most recent call last):
#   File "/Users/jialei/PycharmProjects/pythonAdvanced/函数式编程/yield.py", line 25, in <module>
#     print(next(G))
#           ^^^^^^^
# StopIteration
# print(next(G))
print("-" * 34)
# 当然上面不断地调用next(G)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
# ‼️‼️generator如果已经迭代过后，就不能再迭代了，因为指针已经到最后了，没有元素可以展示了
for i in G:
    print(i)
print("-" * 34)
"""
generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现
比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1
    return 'done'


fib(20)
print("-" * 34)
"""
仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，
推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator函数，
只需要把print(b)改为yield b就可以了：
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'


# 此时f就是generator的可迭代对象，可以通过for循环进行迭代
f = fib(20)

for e in f:
    print(e)

print('-' * 34)


def triangles():
    b = [1]
    while True:
        yield b
        b = [i + j for i, j in zip(b + [0], [0] + b)]


n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
