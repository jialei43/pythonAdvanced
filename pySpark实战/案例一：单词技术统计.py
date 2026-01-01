"""
单词计数统计案例
功能：读取文本文件，统计每个单词出现的次数
"""

from pyspark import SparkContext, SparkConf
import os

# 设置Python解释器路径（确保PySpark使用正确的Python环境）
os.environ['PYSPARK_PYTHON'] = r"D:\Users\Administrator\anaconda3\envs\pythonAdvanced\python.exe"

# 创建Spark配置对象
# local[*] 表示在本地运行，使用所有可用核心
# test_spark 是应用程序名称
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")

# 创建SparkContext对象（Spark应用程序的入口点）
sc = SparkContext(conf=conf)

# 读取输入文本文件，创建RDD（弹性分布式数据集）
# 每行文本成为RDD中的一个元素
text_file = sc.textFile("input")

# 链式操作开始：
word_counts = (text_file
    # 1. flatMap操作：将每行文本拆分为单词，并展平结果
    # 输入：一行文本 输出：多个单词
    # 例如："hello world" -> ["hello", "world"]
    .flatMap(lambda line: line.split(" "))

    # 2. map操作：将每个单词转换为(单词, 1)的键值对
    # 为后续reduceByKey做准备
    # 例如："hello" -> ("hello", 1)
    .map(lambda word: (word, 1))

    # 3. reduceByKey操作：按单词(key)分组，并对值(1)进行累加
    # 相同单词的计数值会被相加
    # 例如：("hello",1), ("hello",1) -> ("hello",2)
    .reduceByKey(lambda a, b: a + b))

# 将结果保存到output目录中
# 会生成多个part文件（因为Spark是分布式处理的）
# word_counts.saveAsTextFile("output")
print(word_counts.collect())
# 注意：实际应用中应该调用sc.stop()来释放资源
# 但在脚本结束时SparkContext会自动关闭
sc.stop()
