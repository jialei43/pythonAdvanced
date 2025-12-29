"""
演示通过PySpark代码加载数据，即数据输入
"""
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 通过parallelize方法将python对象加载到spark内，成为RDD对象
rdd1 = sc.parallelize(list(range(10)))
print(list(range(10)))
rdd2 = sc.parallelize(tuple(range(10)))
rdd3 = sc.parallelize(set(range(10)))
rdd4 = sc.parallelize("abcdefg")
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})
# 如果要查看RDD里面有什么内容，需要用到collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

rdd_text = sc.textFile("../student.txt")
print(rdd_text.collect())
sc.stop()