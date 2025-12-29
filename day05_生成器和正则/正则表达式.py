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
# ^ 匹配字符串的开头。
print(re.findall(r'^abc', "abc123 abc"))

# 匹配账号，只能由数字和字母租场，长度是6-10
r = '^[0-9a-zA-Z]{6,10}$'
print(re.findall(r, "123124235355436"))
print(re.findall(r, "abc12345"))
"""
第二个 "abc"：虽然它的内容也是 "abc"，但它位于字符串的中间（前面有空格和 xyz）。因为它不在字符串的“开头”，所以不符合 ^ 的限制条件。
"""
result = re.findall(r"^abc", "abcxyz abc")
print(result)  # 输出: ['abc']

# $ 匹配字符串的结尾。
"""
第一个 "xyz"：它出现在字符串中间（后面跟着空格和 def...）。对于正则表达式引擎来说，这里不是字符串的终点，因此不满足 $ 的条件。
"""
result = re.findall(r"xyz$", "abcxyz defxyz")
print(result)  # 输出: ['xyz']


# \b：单词边界
#
# 定义：\b 匹配一个单词的边界，他匹配的是一个独立的单词，左右都没有元素相邻。

result = re.findall(r"\bword\b", "word the word is here")
print(result)  # 输出: ['word', 'word']

# \B：非单词边界 位于一个字符串的中间，左右俩边都有字符
#
# 定义：\B 匹配非单词边界。
result = re.findall(r"\Bword\B", "sword worded")
print(result)  # 输出: []

# "word" 左右都被字母包围了
text = "passworded"
result = re.findall(r"\Bword\B", text)

print(result)  # 输出: ['word']

"""
6分组与捕获
"""
result = re.findall(r"(\d+)-(\d+)", "123-456 789-012")
print(result)  # 输出: [('123', '456'), ('789', '012')]




"""
案例
"""
# 匹配qq号，要求都是数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '11234567899'
print(re.findall(r, s))

# 匹配邮箱地址，只允许 qq，163，gmail  \w只匹配数字，字母、下划线，所以还带加上-
r = '^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$'
s = "jia.lei1234@163.cloud"
print(re.findall(r, s))
print(re.match(r, s))


