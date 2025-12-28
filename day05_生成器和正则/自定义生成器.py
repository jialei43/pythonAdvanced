"""
自定义生成器
"""
"""
自定义生成器，定义一个函数，内部使用yield关键字将要生成的数据返回给外边即可
"""

def my_generator(n:int):
    for e in range(n):
        print('开始生成')
        # 函数走到这里会卡主，调用next或者for循环进行迭代的时候，yield 返回，返回i
        yield e
        print(f'完成{e+1}次')
        print('==' * 34)


if __name__ == '__main__':
    generatot_nums = my_generator(10)
    for generatot_num in generatot_nums:
        print(generatot_num)