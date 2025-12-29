"""
演示RDD的成员方法使用
"""
from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r"D:\Users\Administrator\anaconda3\envs\pythonAdvanced\python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD对象
rdd = sc.parallelize(list(range(10)))
# 通过map方法对每个数乘以10
def fn(data):
    return data*10

# 对RDD内的元素逐个处理，并返回一个新的RDD，每次返回的对象都一样，所以我们可以进行链式调用
rdd_map = rdd.map(fn).map(lambda x: x+5)
print(rdd_map.collect())
sc.stop()

