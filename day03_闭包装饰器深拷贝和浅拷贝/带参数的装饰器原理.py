"""
一句“面试级总结”

带参数装饰器 = 返回装饰器的函数

第1层：接收装饰器参数

第2层：接收被装饰函数

第3层：包裹原函数逻辑

本质等价：

func = decorator(args)(func)
decorator(args)(func) 并不是一次调用，而是两次连续调用
第一次返回一个函数，第二次调用这个返回的函数
这是 Python 函数作为“一等公民”的直接体现

func = decorator(args)(func) 函数嗲用等价于：
tmp = decorator(args)   # 第一次函数调用
result = tmp(func)      # 第二次函数调用

程序加载阶段：
--------------------------------
log("INFO")           # 执行
└── decorator         # 返回

decorator(now)        # 执行
└── wrapper           # 返回

now = wrapper

--------------------------------
运行阶段：
now() → wrapper()

"""
def log(arg=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            level = arg if isinstance(arg, str) else "INFO"
            print(f"[{level}] {func.__name__}")
            return func(*args, **kwargs)
        return wrapper

    if callable(arg):
        return decorator(arg)
    return decorator
@log
def a(): pass

@log("DEBUG")
def b(): pass
a()
b()
print('-' * 34)
"""
装饰器多参数进阶写法
"""

def log2(*d_args, **d_kwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("decorator args:", d_args)
            print("decorator kwargs:", d_kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# @log2("INFO", "调用", enable=True, retry=3)
# def now():
#     pass
#
# now()

# 等价于
def now2():
    return "我是now()2"

now2 = log2("INFO", "调用", enable=True, retry=3)(now2)
print(now2())

