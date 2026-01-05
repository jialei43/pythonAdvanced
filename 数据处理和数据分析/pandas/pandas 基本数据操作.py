from urllib.parse import quote_plus

import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

csv = pd.read_csv("./data/stock_day.csv", encoding="GBK")
print(csv)
print('==' * 34)

# 删除一些列，让数据更简单些，再去做后面的操作
data = csv.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)
print(data.head())

# 索引操作
# 3.1直接使用行列索引(先列后行)
print(data["open"]["2018-02-27"])
# 先行后列式错误的,因为行不是key,是一条数据,只有列是key
# print(data["2018-02-27"]["open"])
print('==' * 34)

# ‼️‼️使用loc:只能指定行列索引的名字,取索引2018-02-27到2018-02-14的open列
print(data.loc["2018-02-27":"2018-02-14", "open"])
print('==' * 34)

# ‼️‼️使用iloc可以通过索引的下标去获取,使用场景是在知道数据位于行列索引的位置的时候
# 获取前3天,前5列的结果
print(data.iloc[:3, :5])
print('==' * 34)

# 赋值操作
# 对 data当中的close列进行赋值,直接修改原来的值
data.close = 1  # 也可以 data["close"] = 1
print(data.head())
print('==' * 34)

# 通过行进行赋值
# 修改指定行的数据 .loc[]是基于行标签和列标签进行赋值
data.loc["2018-02-27", "open"] = 23.54

# data.loc["open", "2018-02-27"] = 23.54
print(data.head())
print('==' * 34)

# 修改多个列的数据
# 修改多个列的数据
# 为了避免FutureWarning，先将相关列转换为float类型
# data[["high", "close"]] = data[["high", "close"]].astype(float)
data.loc["2018-02-27", ["high", "close"]] = [23.54, 23.54]
print(data.head())
print('==' * 34)

# 修改多行多列数据
data.loc["2018-02-26":"2018-02-09", "open":"close"] = 23
print(data.head(10))
print('==' * 34)

randint = np.random.randint(23, 30, (7, 3))
data.loc["2018-02-26":"2018-02-09", "open":"close"] = randint
print(data.head(10))
print('==' * 34)

# 条件赋值
# 如果你想根据某个条件修改数据,可以使用Dataframe的条件索引
data.loc[data["open"] > 23, "price_change"] = 100
print(data.head(10))

# 4. 通过 .at[] 和 .iat[] 赋值
# .at[] 是基于标签（行索引和列标签）进行访问和赋值，速度较快，适合单个元素的修改。
data.at["2018-02-27", "open"] = 26.54
print(data.head(1))
print('==' * 34)

# .iat[] 是基于位置（行索引和列位置）进行访问和赋值，适合修改单个元素。
data.iat[1, 0] = 26.54
print(data.head(2))
print('==' * 34)

# 5. 通过 .apply() 和 .map() 赋值
# .apply() 方法适用于逐行或逐列的函数应用，可以用来对列或行的每个元素进行某种操作。
# 使用 .apply() 对整个列进行操作
data["p_change"] = data["p_change"].apply(lambda x: x * 2)
print(data.head())
print('==' * 34)
# .map() 用于映射列中的每个元素到一个新的值，常用来进行替换或映射。
# 使用 .map() 替换列中的值
data["turnover"] = data["turnover"].map(lambda x: x * 2)
print(data.head())
print('==' * 34)

# map匹配不到的值,会返回NaN
# 解决方案：
# 如果你希望在 map() 操作中保留那些没有匹配到的原始值，而不是填充为 NaN 或其他默认值，可以通过使用 .apply() 和字典的 get() 方法来实现。。
# data["turnover"] = data["turnover"].map({4.78: 3, 3.06: 1.6})
# data["turnover"] = data["turnover"].fillna(data["turnover"])
# print(data.head())
# print('==' * 34)
data["turnover"] = data["turnover"].apply(lambda x: {4.78: 3, 3.06: 1.6}.get(x, x))
print(data.head(10))
print('==' * 34)

# ### DataFrame排序
#
# - 使用df.sort_values(by=, ascending=)
#   - 单个键或者多个键进行排序,
#   - 参数：
#     - by：指定排序参考的键
#     - ascending:默认升序
#       - ascending=False:降序
#       - ascending=True:升序

# 按照开盘价大小进行排序 , 使用ascending指定按照大小排序
print(data.sort_values(by="open", ascending=True).head(10))
print('==' * 34)

# 按照多个键进行排序
data.at["2015-03-02", "open"] = 12.30
print(data.sort_values(by=["open", "high"], ascending=[True, False]).head(10))
print('==' * 34)

# 对索引进行排序
print(data.sort_index(ascending=True).head(10))
print('==' * 34)

# 对series排序
print(data.open.sort_values().head())
print('==' * 34)

"""
四、DataFrame运算
- 应用add等实现数据间的加、减法运算
- 应用逻辑运算符号实现数据的逻辑筛选
- 应用isin, query实现数据的筛选
- 使用describe完成综合统计
- 使用max, min, mean, std完成统计计算
- 使用idxmin、idxmax完成最大值最小值的索引
- 使用cumsum等实现累计分析
- 应用apply函数实现数据的自定义处理
"""

# - add(other)
# 比如进行数学运算加上具体的一个数字
print(data.open.head())
print(data.open.add(1).head())
print('==' * 34)

# - sub(other)
# 比如进行数学运算减去具体的一个数字
print(data.open.sub(1).head())
print('==' * 34)

# - mul(other)
# 比如进行数学运算乘以具体一个数字
print(data.open.mul(2).head())
print('==' * 34)

# - div(other)
# 比如进行数学运算除以具体一个数字
print(data.open.div(2).head())
print('==' * 34)

# ## 逻辑运算符
# - &:逻辑与
print(data[data.open > 34].head(20))
print('==' * 34)
print(data[(data.open > 34) & (data.high > 35)].head(20))
print('==' * 34)

# 逻辑运算函数 可以简化上述的步骤
# - query(expr)
#   - expr:查询字符串
# 通过query使得刚才的过程更加方便简单
print(data.query("open > 34").head(20))
print('==' * 34)
print(data.query("open > 34 & high > 35").head(20))

# - isin(values)
# 例如判断'open'是否为23.53和23.85
print(data[data.open.isin([23.53, 23.85])].head(20))
print('==' * 34)

# 统计运算 - describe()
# 综合分析: 能够直接得出很多统计结果,`count`, `mean`, `std`, `min`, `max` 等

print(data.describe())
# data.describe().max().plot()
# plt.show()

# max() min()
print(data.max())
print('==' * 34)
print(data.min())
print('==' * 34)

# std() var()
print(data.std())
print('==' * 34)
print(data.var())
print('==' * 34)

# * median()：中位数
#
# 中位数为将数据从小到大排列，在最中间的那个数为中位数。如果没有中间数，取中间两个数的平均值
print(data.median())
print('==' * 34)

# idxmax()、idxmin()
print(data.idxmax())
print('==' * 34)
print(data.idxmin())
print('==' * 34)

### 累计统计函数

# | 函数      | 作用                        |
# | --------- | --------------------------- |
# | `cumsum`  | **计算前1/2/3/…/n个数的和** |
# | `cummax`  | 计算前1/2/3/…/n个数的最大值 |
# | `cummin`  | 计算前1/2/3/…/n个数的最小值 |
# | `cumprod` | 计算前1/2/3/…/n个数的积     |
print("累计统计函数")
data.sort_index(ascending=True)
print(data.p_change.cumsum().head())
# data.p_change.cumsum().plot()
# plt.show()

print('==' * 34)
print(data.p_change.cummax().head())
print('==' * 34)
print(data.p_change.cummin().head())
print('==' * 34)
print(data.p_change.cumprod().head())
print('==' * 34)

### apply自定义运算

# - apply(func, axis=0)
#   - func:自定义函数
#   - axis=0:默认是列，axis=1为行进行运算
# - 定义一个对列，最大值-最小值的函数
csv = pd.read_csv("./data/stock_day.csv", encoding="GBK")
# 删除一些列，让数据更简单些，再去做后面的操作
data = csv.drop(["ma5", "ma10", "ma20", "v_ma5", "v_ma10", "v_ma20"], axis=1)
print(data[['open', 'close']].apply(lambda x: x.max() - x.min(), axis=0))
print('==' * 34)

"""
五、文件读取与存储
- 了解Pandas的几种文件读取存储操作
- 应用CSV方式、MySQL方式和JSON方式实现文件的读取和存储
我们的数据大部分存在于文件当中，所以pandas会支持复杂的IO操作，pandas的API支持众多的文件格式，
如CSV、SQL、XLS、JSON、HDF5。
"""
# 读取CSV文件
data = pd.read_csv("./data/stock_day.csv", usecols=["open", "close"])
print(data.head())
print('==' * 34)

# 写入CSV文件
# - DataFrame.to_csv(path_or_buf=None, sep=', ’, columns=None, header=True, index=True, mode='w', encoding=None)
#   - path_or_buf :文件路径
#   - sep :分隔符，默认用","隔开
#   - columns :选择需要的列索引
#   - header :boolean or list of string, default True
#   - index:是否写进行索引,是否写进列索引值
#   - mode:'w'：重写, 'a' 追加
# - 举例：保存读取出来的股票数据
#   - 保存'open'列的数据，然后读取查看结果
data[:10].to_csv("./data/stock_day_10.csv", columns=["open"], index=True)
print(pd.read_csv("./data/stock_day_10.csv"))
print('==' * 34)
data[:10].to_csv("./data/stock_day_10.csv", columns=["open"], index=False)
print(pd.read_csv("./data/stock_day_10.csv"))
print('==' * 34)

# # 以MySQL数据库为例，**此时默认你已经在本地安装好了MySQL数据库**。如果想利用pandas和MySQL数据库进行交互，需要先安装与数据库交互所需要的python包
# index_col=[0] 的作用
# 1. 基本功能
# 将第0列（第一列）作为行索引，而不是将其作为普通数据列读取
# 指定 index_col=[0] 告诉 pandas.read_csv() 函数将第一列用作 DataFrame 的行索引
# 2. 具体效果
# 原数据：第一列原本是普通数据列
# 处理后：第一列成为索引，不再占用数据列的位置
# 结果：DataFrame 的行索引将使用 CSV 文件中第一列的值
# 3. 使用场景
# 时间序列数据：第一列通常是日期或时间戳，适合作为索引
# 唯一标识符：当第一列包含唯一 ID 时，作为索引更便于数据操作
# 避免重复：防止将索引列误认为是普通数据列
# 4. 实际应用价值
# 数据对齐：便于与其他使用相同索引的数据进行合并操作
# 索引访问：可以直接使用原始第一列的值进行数据检索
# 节省空间：避免将索引作为普通列存储，减少内存占用
read_csv = pd.read_csv("./data/csv示例文件.csv", encoding="GBK",
                       sep=',', index_col=[0])
print(read_csv)

# 数据库包导入
from sqlalchemy import create_engine

# mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8
# mysql 表示数据库类型
# pymysql 表示python操作数据库的包
# root:123456 表示数据库的账号和密码，用冒号连接
# 127.0.0.1:3306/test 表示数据库的ip和端口，以及名叫test的数据库
# charset=utf8 规定编码格式
# 创建数据库引擎，传入uri规则的字符串

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/ai_chat_db?charset=utf8")
# 第一个参数为数据表的名称
# 第二个参数engine为数据库交互引擎
# index=False 表示不添加自增主键
# if_exists='append' 表示如果表存在就添加，表不存在就创建表并写入
# read_csv.to_sql("test_pdtosql", engine, index=True, if_exists='append')
print("写入成功")
print('==' * 34)
# 从数据库读取 数据
res = pd.read_sql("test_pdtosql", engine)
print(res)

# 用sql进行读取数据
res = pd.read_sql("select name,AKA from test_pdtosql where `index` > 1", engine)
print(res)

"""
pandas.read_json(
    path_or_buffer=None, 
    orient=None, 
    typ='frame', 
    dtype=None, 
    convert_axes=True, 
    convert_dates=True, 
    keep_default_dates=True, 
    encoding='utf-8', 
    encoding_errors='strict', 
    precise_float=False, 
    date_unit=None, 
    lines=False, 
    chunksize=None, 
    **kwargs
)
常用参数：

path_or_buffer:
读取JSON 数据的路径或类文件对象，支持字符串路径、URL 或文件对象。如果提供的是 URL，会自动从 URL 下载数据。
例如：'file.json'、'http://example.com/data.json' 或 StringIO('{"a": 1, "b": 2}')。

orient:
用于指定 JSON 对象的布局方式，决定 JSON 数据如何解析。可以是以下之一：
'split': 字典结构，{"index": [], "columns": [], "data": []}。
'records': 每条记录为一个字典，[{"col1": val1, "col2": val2}, ...]。
'index': 用索引为键的字典结构，{index: {column: value}}。
'columns': 用列名为键的字典结构，{column: {index: value}}。
'values': 仅返回二维数据结构，[values]。
默认情况下，Pandas 会自动推测并选择最适合的布局。

typ:
指定返回的类型，默认值为 'frame'，即返回一个 DataFrame。如果设置为 'series'，则返回一个 Pandas Series 对象（适用于数据中只有单一列时）。

dtype:
允许指定每一列的数据类型。可以传入字典，键为列名，值为目标数据类型。

convert_axes:
是否转换轴（index 和 columns）。默认值为 True。

convert_dates:
如果为 True，Pandas 会尝试自动解析日期格式并将其转换为 datetime 类型。默认值为 True。

keep_default_dates:
如果为 True，默认日期列会被转换为 datetime 类型。设置为 False 时，默认日期列会被保留为字符串。
encoding:
用于指定文件的字符编码，默认为 'utf-8'。
lines:
如果 JSON 数据是逐行存储的（即每行是一个 JSON 对象），则需要设置为 True。例如，每行表示一个独立的记录。
chunksize:
如果设置为正整数，表示每次返回指定大小的 JSON 数据块，适用于处理大数据集。
"""
print("==" * 34)
read_json = pd.read_json("./data/test.json", orient="records", lines=True, typ="frame", encoding="utf-8")
print(read_json)
print("==" * 34)

"""
DataFrame.to_json(
    path_or_buffer=None, 
    orient=None, 
    date_format='iso', 
    date_unit='ms', 
    default_handler=None, 
    lines=False, 
    compression='infer', 
    index=True, 
    indent=None, 
    **kwargs
)
常用参数：

path_or_buffer:
指定要保存 JSON 的路径或类文件对象。如果提供的是 None，则返回 JSON 字符串。

orient:
与 read_json() 中的 orient 参数相同，决定 DataFrame 如何被转换为 JSON 对象。
可选值：
'split': {"index": [], "columns": [], "data": []}。
'records': 每条记录为一个字典。
'index': 以索引为键。
'columns': 以列名为键。
'values': 仅返回二维数据结构。

date_format:
控制日期的格式。默认 'iso'，表示 ISO 格式。如果设置为 'epoch'，则日期会以 Unix 时间戳形式表示。

date_unit:
如果设置了 date_format='epoch'，可以通过 date_unit 来指定时间单位，默认为 'ms'（毫秒）。

default_handler:
处理非 JSON 可序列化对象的函数。例如，若 DataFrame 中有自定义对象，可以通过这个函数来指定如何将这些对象转换为 JSON。

lines:
如果为 True，每一行将是一个独立的 JSON 对象。适用于逐行写入数据。

compression:
压缩类型，支持 'infer'（自动推测）、'gzip'、'bz2'、'zip'、'xz' 等。

index:
是否将 DataFrame 的索引写入 JSON，默认为 True。如果设置为 False，索引将不会写入。

indent:
用于格式化 JSON 输出的缩进级别。如果为 None，则不进行缩进。设置为一个正整数，表示每个级别的缩进空格数。
"""
read_json.to_json("./data/test_copy.json", mode='a', orient='records', lines=True)
print("写入成功")
print("==" * 34)

"""
六、DataFrame数据的增删改查操作
"""
df = pd.read_csv('./data/1960-2019全球GDP数据.csv', encoding='gbk')
df2 = df.head()

# 增加列
df3 = df2.copy()

# 一列数据都是固定值
df3['new_column 1'] = 33
print(df3.head())
print("==" * 34)

# 新增列数据量必须和行的数据量相等
# print(df.shape)
df3['new_column 2'] = [33, 44, 55, 66, 77]
df3['new_column 3'] = np.random.randint(0, 100, size=df3.shape[0])
print(df3.head())
print("==" * 34)

# # 增加行
# new_row = pd.DataFrame.from_dict({
#     'country': '中国',
#     'year': 2020,
#     'GDP': 1000000000000
# })
# df2 = pd.concat([new_row, df2], ignore_index=True)


# 方式二:df.assign函数新增列
df2 = df2.assign(new_1=np.random.randint(0, 100, size=df2.shape[0]))
print(df2.head())

# 新列名为series对象,该对象索引和def的索引一致,也就是series的长度和def的行数一致
df2 = df2.assign(new_2=pd.Series(np.random.randint(0, 100, size=df2.shape[0])))
print(df2.head())

# 3. 新列名=自定义函数名
# 该自定义函数必须接收df作为参数
# 该自定义函数可以返回：
# 3.1.单个数据
# 3.2.一组数量和df的行数相同的数据
# 3.3.和df索引相同的Series对象
def foo(df):
    # 函数必须传入一个参数,该参数就是被传入的DataFrame对象
    return np.random.randint(0, 100, size=df.shape[0])


df2 = df2.assign(new_3=foo)
print(df2.head())

# df.assign函数可以同时添加多列
df2 = df2.assign(
    new_4=np.random.randint(0, 100, size=df2.shape[0]),
    new_5=np.random.randint(0, 100, size=df2.shape[0]),
    new_6=np.random.randint(0, 100, size=df2.shape[0])
)
print(df2.head())

# 删除与去重
# 直接在df3上修改不返回新的对象 ,axis=1 表示删除列
# df3.drop('new_2', axis=1, inplace=True)
