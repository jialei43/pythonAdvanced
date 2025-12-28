"""
演示器生成用法
"""

"""
1、定义一个类，要写__init__方法，接受start和end
2、__fiter__方法，返回对象自己，return self
3、__next__方法，用来迭代，往后走，更新current成员
一定要判断current是否越界，如果越界返回异常，raise StopIteration
"""
class MyIterator(object):
    def __init__(self,end,start = 0):
        self.__current=start
        self.__end=end
    def __iter__(self):
        return  self

    def __next__(self):
        if self.__current>=self.__end:
            raise StopIteration
        self.__current+=1
        return self.__current -1

if __name__ == '__main__':
    # range_iter = range(10)
    # print(range_iter)
    # print(type(range_iter))
    # for i in range_iter:
    #     print(i)

    myIterator =MyIterator(3)
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    # print(myIterator.__next__())
    print(next(myIterator))
    print(next(myIterator))
    print(next(myIterator))
    # print(next(myIterator))

    try:
        print(next(myIterator))
    except StopIteration as e:
        print("StopIteration")

