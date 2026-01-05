import pandas as pd
import matplotlib.pyplot as plt


# 读取1960-2019年全球GDP数据CSV文件，使用GBK编码
df = pd.read_csv("./data/1960-2019全球GDP数据.csv", encoding="GBK")
print(type(df))
# 筛选中国GDP数据
china_gdp = df[df.country == "中国"]
# china_gdp.head(10)
print(china_gdp.head(10))

# 将year年份设置为索引
china_gdp.set_index("year", inplace=True)
print(china_gdp.head())  #默认显示前5条

# print(china_gdp.plot())


