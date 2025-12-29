import jieba

test_text = "我爱编程"
words = jieba.cut(test_text)
print("分词结果：", "/".join(words))
