from ClassAndObject import s
# 方法对象，在调用类的方法不会立即去执行,当调用这个方法对象时才会去执行方法内的逻辑
properties = s.getProperties
# 打印的是方法的对象地址
print(properties)
# 当调用时去执行方法的内容
print(f'properties: {properties()}')