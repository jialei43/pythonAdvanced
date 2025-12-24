"""
装饰器：可以理解对方法的增强，就相当于Java中的动态代理
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
称之为“装饰器”（Decorator）。
"""
from functools import wraps


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2024-6-1')


now()
print('-' * 34)
"""
@log注解就相当于把now()函数当做参数传入到log函数中
"""


def now():
    print('2024-6-1')


# 切结此处传入的是函数名，而不是now()
'''
看这一句👇：
return_func = log(now())
Python 执行顺序是：
① 先执行 now()
now()
它会直接执行：
2024-6-1
⚠️ 注意：
now() 没有 return，所以返回值是None
② 等价于这一句
return_func = log(None)
③ 进入 log(func) 时
此时：
func = None
然后 log 返回 wrapper，但 wrapper 里面有这一句：
func.__name__
💥 None 没有 __name__ 属性
于是就会报错：
AttributeError: 'NoneType' object has no attribute '__name__'
'''
return_func = log(now)
return_func()

print('-' * 34)


# 在now函数执行前后打印日志
def log2(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        func(*args, **kw)
        print("now() 函数执行完毕")
        # return func(*args, **kw)

    return wrapper


@log2
def now2():
    print('2024-6-1')


now2()

print('-' * 34)
# 为什么 functools.wraps 很重要？加了wraps注解，就不需要写func.__name__
'''
wraps 本质是：

def wraps(wrapped):
    def decorator(wrapper):
        wrapper.__wrapped__ = wrapped
        wrapper.__name__ = wrapped.__name__
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__module__ = wrapped.__module__
        wrapper.__annotations__ = wrapped.__annotations__
        return wrapper
    return decorator
@wraps 不是为了“让程序跑”，
而是为了“让程序像原来一样被认识”
把 func 的“元数据”拷贝到 wrapper 上
不是为了执行，是为了 “身份保留”。

二、不写 @wraps 会发生什么？（直接对比）
示例代码
def log(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    """获取当前时间"""
    pass

查看元信息
print(now.__name__)
print(now.__doc__)

输出结果（❌）
wrapper
None


👉 原函数的“身份”已经丢失

加上 @wraps
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

再看结果（✅）
now
获取当前时间
'''


def log3(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        result = func(*args, **kw)
        print("now() 函数执行完毕")
        # 一定要返回result不然now的执行结果会丢失，也会是没有返回值
        return result

    return wrapper


@log3
def now3():
    print('2024-6-1')
    return '打印了 2024-6-1'


a = now3()
print(f'a的值：{a}')

"""
五、带参数的日志装饰器（真实项目常用)
底层思想（一句话）

装饰器通过“闭包 + 包装函数（wrapper）”，
在调用原函数前后插入自定义逻辑

核心公式：

func = decorator(func)


调用时：

wrapper() 
 ├─ 前置逻辑
 ├─ func()
 └─ 后置逻辑
"""
print('-' * 34)


def production_log(level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}]日志模式 开始 {func.__name__}")
            result = func(*args, **kwargs)
            print(f"add方法执行结果：[{result}]")
            print(f"[{level}]日志模式 结束 {func.__name__}")
            return result

        return wrapper

    return decorator


@production_log()
# @production_log("DEBUG")
def add(a, b):
    return a + b


print(f'add返回结果：{add(1, 2)}')

# 带异常保护的完整日志

print('-' * 34)


def production_log2(level="INFO"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                print(f"[{level}]日志模式 开始 {func.__name__}")
                result = func(*args, **kwargs)
                print(f"add方法执行结果：[{result}]")
                print(f"[{level}]日志模式 结束 {func.__name__}")
                return result
            except:
                print(f"[{level}]日志模式 异常 {func.__name__}")
            finally:
                print(f"[{level}]日志模式 最终执行 {func.__name__}")

        return wrapper

    return decorator


@production_log2()
def now(a, b):
    return a / b


print(f'执行结果 %s' % now(10, 2))
print(f'执行结果 %s' % now(10, 0))

print('-' * 34)
"""
多个装饰器
多个装饰器的底层执行顺序 ⭐⭐⭐
@a
@b
@c
def f():
    pass

等价代码
def f():
    pass

f = a(b(c(f)))

执行顺序总结
阶段	顺序
装饰阶段	c → b → a
调用阶段	a → b → c → f

先给结论（直接可用）

🔥 想让「写在最上面的装饰器」的业务效果“最先发生”，
那就把业务增强逻辑写在 func() 之前（前置逻辑）

一句话规则
你想要的效果	增强逻辑放哪
与装饰器书写顺序一致	func() 之前
与装饰器书写顺序相反	func() 之后
包裹型（进出对称）	前 + 后（洋葱模型）
"""


def check_user(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("请输入用户名和密码")
        fn(*args, **kwargs)


    return wrapper


def check_code(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("请输入登录验证码")
        fn(*args, **kwargs)


    return wrapper

@check_code
@check_user
def comment():
    print("发表评论")


comment()
print('-' * 34)


def comment():
    print("发表评论")


# 等价于
comment = check_code(check_user(comment))
comment()
