"""
演示获取Pyspark的执行环境入库对象：SparkContext
并通过SparkContext获取当前pyspark的版本
"""

# 导包
from pyspark import SparkConf, SparkContext
# 创建sparkconf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 基于sparkconf类对象创建sparkcontext对象
sc = SparkContext(conf=conf)
# 打印pyspark的运行环境
print(sc.version)
# 停止sparkcontext对象运行（停止PySpark程序）
sc.stop()