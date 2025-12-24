"""
在函数嵌套的前提下，内部函数使用外部函数的变量，且外部函数返回了内部函数
这种：使用外部函数变量的内部函数称为闭包
格式：
    def 外部函数名(外部参数)：
        def 内部函数名(内部参数)：

            nonlocal 外部参数 # 只有使用nonlocal修饰的变量才可以修改外部函数的值，如果只是使用，不对外部函数的参数进行操作不需要加nonlocal

            外部参数 = “”
        return 内部函数名
"""
import gc


# 方式一：
def seekpeace(num1: int):
    number = 10
    def num():

        return number + num1

    return num


numbers = seekpeace(1)
numbers = seekpeace(2)
# numbers = seekpeace(3)
# numbers = seekpeace(4)
print(numbers())
print('-' * 34)
# 方式二:
def seekpeace(num1: int):
    def num(number: int):

        return number + num1

    return num


"""
实现：
10 +1
10+1+2
10+1+2+3
....
10+1+2+3+4+...+9
"""
total_num = 10
for i in range(10):
    s= seekpeace(total_num)
    total_num = s(i)
    print(total_num)
"""
下面的方法俩个list使用了相同的堆内存空间是因为，内部函数没有使用外部函数的list_nim1,是新建的
一个list_num1,当外部函数结束时，外部函数的变量list_num1变量被回收了，但是此时内存堆空间未被
回收，此时内部函数被调用创建list_num1变量时，python的优化器就将list_num1执向了未回收的堆内存
进行复用，所以他俩打印的内存地址一致
"""
def out_func():
    list_num1 = []
    print("in outer_func id(list_num1):", id(list_num1))
    def inner_func():
        list_num1 =[]
        print("in inner_func id(list_num1):", id(list_num1))

    # inner_func()
    return inner_func

new_func = out_func()
new_func()

print('-' * 34)
"""
为了验证上面俩个变量地址一致是因为外部函数的局部变量的堆内存未回收，内部函数创建变量复用了
堆内存，我们引入gc.collect()，它的作用就是没有被引用的堆内存立即回收，此时创建内部函数的
变量就会新建堆内存，俩者的内存地址就不一样了
"""
def out_func():
    list_num1 = []
    print("in outer_func id(list_num1):", id(list_num1))
    def inner_func():
        list_num1 =[]
        print("in inner_func id(list_num1):", id(list_num1))

    # inner_func()
    return inner_func

new_func = out_func()
# 立即进行内存回收
gc.collect()
new_func()