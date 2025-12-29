import os
import glob
import re
from datetime import datetime

import jieba
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import simpledialog

from sympy.physics.control.control_plots import matplotlib
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from tkinter import messagebox
from docx import Document

matplotlib.use('TkAgg')


# 1. 选择目录，获取目录下的所有Word文件
def select_directory():
    folder_selected = filedialog.askdirectory()  # 弹出文件夹选择对话框
    if folder_selected:
        word_files = glob.glob(os.path.join(folder_selected, "*.docx"))
        return word_files
    else:
        return []


# 2. 读取Word文件的内容并进行分词
def read_and_tokenize_files(word_files):
    text = ""
    for file in word_files:
        doc = Document(file)
        print(f"正在读取文件：{file}")  # 打印正在读取的文件
        for para in doc.paragraphs:
            print(f"段落内容：{para.text}")  # 打印每个段落的内容
            text += para.text
            text = re.sub(r'[^\w\s]', '', text)
            print(f'去掉非数字和空格的text:{text}')

    if not text:
        print("警告：文件内容为空")

    # 使用 jieba 进行中文分词
    words = jieba.cut(text)
    # print("分词后的结果：", "/".join(words))  # 打印分词结果
    # return " ".join(words)
    return "/".join(words)


# 3. 人工干预修改分词词库
def manual_intervention():
    words = simpledialog.askstring("输入词语", "输入需要添加到分词词库的词语（用空格隔开）：")
    if words:
        for word in words.split():
            jieba.add_word(word)  # 添加新的词语到jieba分词词库
        messagebox.showinfo("提示", "词库已更新")


# 4. 生成词云
def generate_wordcloud(text, threshold=1, layout_type="random"):
    print("生成词云的文本：", text)
    word_count = {}
    for word in text.split("/"):
        word = word.strip()  # 去除前后空格
        if word and re.match(r'^[\u4e00-\u9fa5a-zA-Z0-9]+$', word):
            print(f'word:{word}')
            word_count[word] = word_count.get(word, 0) + 1
    print("词频统计：", word_count)
    filtered_text = " ".join([word for word in word_count if word_count[word] >= threshold])
    print(f'filtered_text:{filtered_text}')

    if not filtered_text:
        print("警告：没有有效的词语生成词云")
        return

    # 选择词云布局
    if layout_type == "random":
        wc = WordCloud(font_path="C:/Windows/Fonts/simhei.ttf", width=800, height=400, background_color="white", max_words=200,collocations=False)
    elif layout_type == "vertical":
        wc = WordCloud(font_path="C:/Windows/Fonts/simhei.ttf", width=800, height=400, background_color="white", max_words=200,
                       prefer_horizontal=0,collocations=False)
    elif layout_type == "horizontal":
        wc = WordCloud(font_path="C:/Windows/Fonts/simhei.ttf", width=800, height=400, background_color="white", max_words=200,
                       prefer_horizontal=1,collocations=False)
    else:
        wc = WordCloud(font_path="C:/Windows/Fonts/simhei.ttf", width=800, height=400, background_color="white", max_words=200,collocations=False)

    wc.generate(filtered_text)
    # 获取当前日期和时间（到秒）
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 弹出文件保存对话框，让用户选择保存位置和文件名
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             initialfile=f"wordcloud_{current_time}.png")

    if save_path:
        wc.to_file(save_path)  # 保存词云图
        messagebox.showinfo("保存成功", f"词云图已保存到：{save_path}")
        print(f"词云图已保存到：{save_path}")

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# 5. 设置阈值并选择布局类型
def wordcloud_gui():
    # 创建主窗口
    root = Tk()
    root.title("Word文档词云生成系统")

    # 选择目录按钮
    def on_select_folder():
        word_files = select_directory()
        if word_files:
            text = read_and_tokenize_files(word_files)
            print(f'text:{text}')
            # 选择是否进行词库干预
            intervene = messagebox.askyesno("词库干预", "是否需要添加新的词语到词库？")
            if intervene:
                manual_intervention()
            # 选择阈值
            threshold = simpledialog.askinteger("设置词云阈值", "请输入词云词频阈值：", minvalue=1, maxvalue=50, initialvalue=1)
            if threshold is None:
                threshold = 1

            # 选择词云布局
            # layout_type = simpledialog.askstring("选择布局", "请输入词云布局类型（random、vertical、horizontal）：")
            # if layout_type not in ["random", "vertical", "horizontal"]:
            #     layout_type = "random"

            # 选择词云布局
            layout_type = layout_combobox.get()  # 获取下拉框选中的布局
            print(f"选择的布局类型: {layout_type}")

            # 生成词云
            generate_wordcloud(text, threshold, layout_type)
        else:
            messagebox.showerror("错误", "未选择文件夹或文件夹为空！")

    select_button = Button(root, text="选择Word文档目录", command=on_select_folder)
    select_button.pack(pady=20)

    layout_combobox = ttk.Combobox(root, values=["random", "vertical", "horizontal"])
    layout_combobox.set("random")  # 设置默认选择
    layout_combobox.pack(pady=5)

    # 退出按钮
    exit_button = Button(root, text="退出", command=root.quit)
    exit_button.pack(pady=20)

    # 运行主事件循环
    root.mainloop()


if __name__ == "__main__":
    wordcloud_gui()
