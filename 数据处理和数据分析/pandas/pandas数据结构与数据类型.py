import numpy as np
import pandas as pd

# 创建series对象
s = pd.Series([1, 2, 3, 4, 5])
print(s)
# print(s.index)
# print(s.values)
print('==' * 34)

s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
print('==' * 34)

tuples = (1, 2, 3, 4, 5, 6, 7)
s = pd.Series(tuples, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(s)
print('==' * 34)

dicts = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
s = pd.Series(dicts)
print(s)
print('==' * 34)
s = pd.Series(np.arange(1, 10))
print(s)
print(s.index)
print(s.values)
print('==' * 34)
print(s[0:0])
print(s[0:3])

# 创建DataFrame对象
# dataframe时一个类似二维数组或表格(如 excel)的对象,既有行索引,也有列索引
# 将字典转换为datafram
df1_data = {
    "日期": ['2020-01-01', '2020-01-02', '2020-01-03', '2020-01-04', '2020-01-05'],
    "温度": [10, 12, 14, 16, 18],
    "湿度": [10, 12, 14, 16, 18]
}
frame = pd.DataFrame(df1_data)
print(frame)
print('=' * 34)

# 元组转换为datafarm
df2_data = [
    ("2020-01-01", "25", "81"),
    ("2020-01-02", "24", "80"),
    ("2020-01-03", "23", "79")
]
data_frame = pd.DataFrame(data=df2_data, columns=['日期', '温度', '湿度'], index=['row1', 'row2', 'row3'])
print(data_frame)

# 使用numpy的random 生成
randint = np.random.randint(40, 100, (10, 5))
print(randint)
print('=' * 34)
pd_data_frame = pd.DataFrame(
    data=randint,
    columns=["数学","语文","英语","物理","化学"],
    index=[f'同学{i}' for i in range(1,11)]
)
print(pd_data_frame)
print('=' * 34)

# 属性 shape属性
print(pd_data_frame.shape)
print('=' * 34)

# index-属性
print(pd_data_frame.index)
print('=' * 34)

# columns-属性
print(pd_data_frame.columns)
print('=' * 34)

# values-属性 直接获取其中的array
print(pd_data_frame.values)
print('=' * 34)

# data.T 行列翻转
print(pd_data_frame.T)
print('=' * 34)

# head 显示前n行内容,默认显示5行
# 查看默认显示多少行, 使用pd.get_option('display.max_rows'),设置显示行数(不是设置默认值),pd.set_option('display.max_rows', 5)
print(pd.get_option('display.max_rows'))
# pd.set_option('display.max_rows', 5)
print(pd_data_frame.head(10))
print('=' * 34)

# tail显示后n行内容,默认显示五行,和head一样可以设置行数(不是默认行数)
print(pd_data_frame.tail(3))
print('=' * 34)

# dataframe设置索引
print(pd_data_frame.shape)
pd_data_frame.index = [f'同学{i}' for i in range(pd_data_frame.shape[0])]
print(pd_data_frame)
print('=' * 34)

# 重置索引 drop=True,表示不保留原索引列,inplace=True,默认为False,表示直接修改原对象,不返回新的对象,默认为False
# index  数学  语文  英语  物理  化学
# 0   同学0  84  46  42  87  59
# 1   同学1  88  43  71  65  59
# 2   同学2  84  49  71  69  86
# 3   同学3  65  68  54  53  55
# 4   同学4  94  82  69  80  75
# 5   同学5  78  55  84  48  75
# 6   同学6  54  61  72  62  92
# 7   同学7  76  79  60  76  76
# 8   同学8  63  59  53  72  57
# 9   同学9  89  75  77  60  71
pd_reset_index = pd_data_frame.reset_index(drop=False, inplace=False)
print(pd_reset_index)
print('=' * 34)
#      数学  语文  英语  物理  化学
# 同学0  69  76  46  42  85
# 同学1  99  83  59  69  63
# 同学2  74  55  71  58  87
# 同学3  84  82  50  63  90
# 同学4  62  92  72  90  72
# 同学5  61  70  51  75  92
# 同学6  68  53  58  60  74
# 同学7  83  96  57  95  49
# 同学8  42  45  62  87  47
# 同学9  86  71  64  56  92
# 所以可以看出来上面的inplace=False,表示不修改原对象,返回新的对象,源对象的索引不变
print(pd_data_frame)
print('=' * 34)

# ==================================
# None
# =================================
# 之所以是None是因为inplace=True在在源对象上修改了索引,不返回新对象,所以返回None
pd_reset_index = pd_data_frame.reset_index(drop=True, inplace=True)
print(pd_reset_index)
print(pd_data_frame)
print('=' * 34)

# 设置某列为索引,将会把这列从dataframe删除,索引名默认为该列名
set_index = pd_data_frame.set_index('语文', inplace=False)
print(set_index)
print('=' * 34)
print(pd_data_frame)
print('=' * 34)

# 设置多个索引
multi_set_index = set_index = pd_data_frame.set_index(['语文', '数学'], inplace=False)
print(multi_set_index)
print('=' * 34)

# pandas 的数据类型
print(s.dtypes)
print('=' * 34)
print(pd_data_frame.dtypes)
print('=' * 34)
print(pd_data_frame.info())  # servis对象没有info方法
print('=' * 34)

# 几种特殊数据类型的展示
# pd.to_datetime 创建一个datetime类型的series
start = pd.to_datetime("2020-01-01")
end = pd.to_datetime("2022-01-01")
delta = end - start
print(delta)
print('=' * 34)

"""
category类型,通常用于有限集合中的数据类型,例如性别,颜色,产品类型等.这种类型的优点在于
占用更少的内存,并且对分类数据的操作更快
"""
series_category = pd.Series(['apple', 'banana', 'orange', 'apple', 'banana'], dtype='category')
print(series_category)






