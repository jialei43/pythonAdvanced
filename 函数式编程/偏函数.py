"""
所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
这样的函数我们称之为偏函数


"""
import functools

int2 = functools.partial(int,base=16)
for i in range(10000,10100):
    print(int2(str(i)))

sorted = functools.partial(sorted, reverse=True)
print(sorted(list(range(10000))))
