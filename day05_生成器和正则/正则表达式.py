import re

"""
二、字符匹配规则（每条一个案例）
"""

# \d匹配数字 +匹配一次或者无数次，至少一次
print(re.findall(r"\d+", "231sdhfs435346ks但实455际3上4"))

# . 规则：匹配任意字符（不含换行）
print(re.findall(r"a.c", "abc aec a-c a\nc"))

# \d 数字
print(re.findall(r"\d", "a1b2c3"))

# \D 非数字
print(re.findall(r"\D", "a1b2"))

# \w 数字字母下划线
print(re.findall(r"\w", "ab_12-@"))

# 非字母数字 \W
print(re.findall(r"\W", "ab_12-@"))

# 空白符 \s 包含空格，tag减缩进，\n 换行 都属于空白符
print(re.findall(r"\s", "a b\tc\n"))

# 非空白符 \S
print(re.findall(r"\S", "a b\tc\n"))

"""
三、数量词（次数控制）
"""
#  * (0次或者是多次)
"""
核心原因：* 代表“0 次或多次”
在正则表达式 ab* 中：
a 是必须存在的字符。
b* 表示字符 b 匹配 0 次或多次。
当你匹配第一个单词 a 时：
正则引擎找到了 a。
正则引擎接着寻找 b。
它发现后面没有 b，但因为 * 允许 b 出现 0 次，所以这被视为一个成功的匹配
"""
print(re.findall(r"ab*", "a ab abb abbb"))

# +（1 次或多次）
print(re.findall(r"ab+", "a ab abb"))

# ?（0 或 1 次）
print(re.findall(r"ab?", "a ab abb abbb"))

# {n} 表示匹配的次数
print(re.findall(r"\d{3}", "12345 678"))

# {n,} 表示匹配大于等于n次
print(re.findall(r"\d{2,}", "1 12 123"))

# {n,m} 表示匹配大于等于n次,小于等于m次
print(re.findall(r"\d{2,3}", "1 12 123 1234"))

"""
字符集合[]
"""
print(re.findall(r"[abc]", "abcdef"))
print(re.findall(r"[a-z]", "aB3_"))

# [^] 取反
print(re.findall(r"[^0-9]", "a1b2"))

"""
边界控制（非常重要）
"""
print(re.findall(r'^abc', "abc123 abc"))

