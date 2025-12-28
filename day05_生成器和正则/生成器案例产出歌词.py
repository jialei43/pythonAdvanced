"""
因为歌词在文件中，需要从文件读取
按照行进行读取，将歌词放入到列表中
生成器是一个函数，内部使用yield返回一个子列表（对原列表进行切片操作）
"""
import itertools
import math


def database_loader(batch_size):

    with open('./jaychou_lyrics.txt', mode='r', encoding='utf-8') as file:
        # 读取所有行，每行数据作为列表的元素进行存储
        file_lines = file.readlines()
        lines_list = []
        # 需要取多少次
        n = math.ceil(len(file_lines) / batch_size)
        for i in range(1, n + 1):
            yield file_lines[(i - 1) * batch_size:i * batch_size - 1:]

# 上面的方法将文件一次性读取，比较占用内存，我们采取每次读取8行
def database_loader2(batch_size):

    with open('./jaychou_lyrics.txt', mode='r', encoding='utf-8') as file:
        while True:
            # itertools.islice()可以用来逐步切割文件，不会将整个文件读入内存，适合大文件。
            chunk = list(itertools.islice(file, batch_size))  # 读取指定数量的行
            if not chunk:
                break
            yield chunk


#   手动来控制批次
def read_file_in_chunks(file_path, chunk_size):
    with open(file_path, 'r') as file:
        lines = []
        for i, line in enumerate(file, 1):
            lines.append(line.strip())  # 去除换行符
            if i % chunk_size == 0:
                yield lines
                lines = []
        if lines:
            yield lines  # 处理最后剩余的行
if __name__ == '__main__':
    # 方式一
    # data_generator = database_loader(8)
    # for data in data_generator:
    #     print(data)

    # 方式二
    # data_generator = database_loader2(8)
    # for e in data_generator:
    #     print(e)
    # 方式三
    file_path = './jaychou_lyrics.txt'
    file_lines = read_file_in_chunks(file_path,8)
    for file_line in file_lines:
        print(file_line)
