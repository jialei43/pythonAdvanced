import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



# 读取1960-2019年全球GDP数据CSV文件，使用GBK编码
df = pd.read_csv("./data/1960-2019全球GDP数据.csv", encoding="GBK")
print(type(df))
# 筛选中国GDP数据
china_gdp = df[df.country == "中国"]
china_gdp.head(10)
print(china_gdp.head(10))

# 将year年份设置为索引
china_gdp.set_index("year")
print(china_gdp.head())  #默认显示前5条
# 由于year现在是索引，所以绘图时不需要指定x参数，pandas会自动使用索引作为x轴
# 正常情况是:china_gdp.plot(x='year',y='GDP', title='GDP over Time')
# china_gdp.plot(y='GDP', title='GDP over Time')
# plt.show()

# china_gdp = df[df.country=='中国'].set_index('year')
# us_gdp = df[df.country=='美国'].set_index('year')
# jp_gdp = df[df.country=='日本'].set_index('year')
# jp_gdp.GDP.plot()
# china_gdp.GDP.plot()
# us_gdp.GDP.plot()
# plt.show()

# 按条件选取数据
# china_gdp = df[df.country=='中国'].set_index('year')
# us_gdp = df[df.country=='美国'].set_index('year')
# jp_gdp = df[df.country=='日本'].set_index('year')
# # 出图并添加图例
# jp_gdp.GDP.plot(legend=True)
# china_gdp.GDP.plot(legend=True)
# us_gdp.GDP.plot(legend=True)
# plt.show()

# 修改列名使图例显示为各国名称
# 在 Pandas 中，inplace=True 是一个常用的参数，它的作用是直接在原 DataFrame 上修改数据，而不返回新的 DataFrame。也就是说，设置 inplace=True 会让修改操作在原地进行，而不是创建并返回一个新的对象。
#
# 解释 inplace=True：
#
# 当你对 DataFrame 进行某些操作时，比如 设置索引、删除列、填充缺失值 等，你可以选择是否返回新的 DataFrame 或直接在原 DataFrame 上修改。
#
# 如果 inplace=True，操作会直接在原 DataFrame 上生效，返回值为 None。如果 inplace=False（默认值），则返回一个新的修改后的 DataFrame，原 DataFrame 不受影响。
# 设置中文字体（macOS 兼容版本）
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'PingFang SC', 'Heiti SC']
plt.rcParams['axes.unicode_minus'] = False


jp_gdp = df[df.country == "日本"].set_index("year")
china_gdp = df[df.country == "中国"].set_index("year")
us_gdp = df[df.country == "美国"].set_index("year")

# 对指定列名进行修改
china_gdp.rename(columns={"GDP":"中国"}, inplace=True)
us_gdp.rename(columns={"GDP":"美国"}, inplace=True)
jp_gdp.rename(columns={"GDP":"日本"}, inplace=True)

# 画图
jp_gdp.日本.plot(legend=True)
china_gdp.中国.plot(legend=True)
us_gdp.美国.plot(legend=True)
plt.show()


