"""
flatmap:对rdd执行map操作，然后进行接触嵌套操作
"""

from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r"D:\Users\Administrator\anaconda3\envs\pythonAdvanced\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD、
rdd = sc.parallelize(["itheima itcast 666", "class method emun", "python java go"])
rdd2 = rdd.map(lambda x: x.split(" "))
# collect方法会将对象的内容输出，类似于python类对象的str方法
print(rdd2.collect())

print('===' * 34)
rdd3 = rdd.flatMap(lambda x: x.split(" "))
# collect方法会将对象的内容输出，类似于python类对象的str方法
print(rdd3.collect())

