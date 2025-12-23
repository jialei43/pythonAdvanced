"""
在绑定属性时，如果我们直接把属性暴漏出去，虽然写起来很简单，但是没办法检验参数，导致可以把成绩随便改
"""
class Student(object):
    pass
s = Student()
s.score = 9999
print(s.score)

