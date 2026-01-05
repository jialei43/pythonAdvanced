"""
1、手动在当前项目根目录下创建singer.txt文件，内容如下： 沉默是金，张国荣 少女的祈祷，杨千嬅 暗里着迷，刘德华 难念的经，周华健（内容见附件）

2、定义一个singer类(歌手类)，包含初始化init方法： 成员属性: 歌曲名 歌手名字 成员方法：fans()：打印“XXX歌手的YYY歌曲持续打榜，粉丝为喜欢的歌手打call” XXX为对象的歌手名字，YYY为对象的歌曲名。

3、在歌手类外面完成以下功能：

1）通过程序逐行读取singer.txt文件内容，根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。

2）遍历列表，获取元素并调用对象的fans方法
"""



class Singer(object):
    def __init__(self, song, singer):
        self.song = song
        self.singer = singer
    def fans(self):
        print(f'{self.singer}歌手的{self.song}歌曲持续打榜，粉丝为喜欢的歌手打call')

singers = []


with open('singer.txt', 'r', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line:
             break
        singer = Singer(line.split('，')[0], line.split('，')[1])
        singers.append(singer)

if singers:
    for singer in singers:
        singer.fans()
else:
    print('没有歌手')