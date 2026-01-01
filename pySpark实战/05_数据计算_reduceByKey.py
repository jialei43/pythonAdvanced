"""
功能：针对KV（二元元组）类型RDD，自动按照key进行分组，然后根据你提供的聚合
"""

from pyspark import SparkConf,SparkContext
import os
# 设置PYSPARK_PYTHON环境变量，指定Python解释器路径
os.environ['PYSPARK_PYTHON'] = r"D:\Users\Administrator\anaconda3\envs\pythonAdvanced\python.exe"

# 配置Spark应用，设置本地运行模式和应用名称
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# 创建SparkContext对象
sc = SparkContext(conf = conf)
# 生成rdd对象，将python的容器转换为rdd
rdd = sc.parallelize([('男',99),('男',88),('女',99),('女',66)])
# 按照key进行分组并聚合，将相同key的value相加,元组的第一个元素作为key为key，第二个元素为value
result = rdd.reduceByKey(lambda a, b: a + b)
# 收集结果并打印
print(result.collect())
