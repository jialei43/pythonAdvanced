"""
生成器用法
"""

# 列表推导式
list = [e for e in range(10) if e%2 == 0]
print(list)

#生成器推到式,生成器记录的是规则
list = (e for e in range(10))
print(next(list))

print('=' * 34)
# 上面已经next一次，当前元素已经变了，循环就从1开始取
for e in list:
    print(e)
