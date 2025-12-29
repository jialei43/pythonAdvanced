from docx import Document
import random


# 生成 Word 文档内容
def generate_large_doc(file_path, num_words=100000):
    # 常见的句子和词汇
    sample_text = [
        "我爱编程，编程非常有趣。",
        "词云生成测试，词云是数据可视化的重要手段。",
        "Python编程语言是非常强大的工具。",
        "数据分析和数据可视化已经成为现代企业的核心技术。",
        "深度学习和机器学习正在不断发展和改变世界。",
        "人工智能是未来科技的重要方向。",
        "Python是一个非常流行的编程语言。",
        "通过数据，您可以看到隐藏在背后的趋势。",
        "机器学习不仅仅是一个算法，更是一种思维方式。"
    ]

    # 创建一个新的 Word 文档
    doc = Document()

    # 计算所需的段落数（根据句子长度来估算）
    current_word_count = 0
    while current_word_count < num_words:
        # 随机选取一个句子
        sentence = random.choice(sample_text)
        doc.add_paragraph(sentence)
        current_word_count += len(sentence)

    # 保存文件
    doc.save(file_path)
    print(f"文档已生成，路径为：{file_path}")


# 生成一个大约有10万字的Word文档
generate_large_doc("test_wordcloud_document.docx", num_words=100000)
