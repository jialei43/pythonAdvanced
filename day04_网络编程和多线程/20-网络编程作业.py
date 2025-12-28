import logging
import socket
import sys

'''
（1）将字符串“AI人工智能进阶班”转换为二进制bytes类型的结果；将二进制bytes数据 b"AI python"转换为字符串str类型的结果。
（2）通过TCP客户端发送消息：欢迎来传智教育，真牛!通过TCP服务器端接收消息，并打印出来。
'''


# str1 = 'AI人工智能进阶班'
# str1 = str1.encode(encoding='utf-8')
# print(str1)
# str1 = str1.decode(encoding='utf-8')
# print(str1)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True   # Python 3.8+，防止被之前的配置覆盖
)

connent = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connent.connect(('127.0.0.1', 8080))
try:
    while True:
        data = input('请输入你要传入的信息(输入y退出)：')
        if data == 'y':
            connent.close()
            break
        connent.sendall(data.encode('utf-8'))
        logging.info(f'客户端已发送：{data}')
        data = connent.recv(1024).decode()
        logging.info(f'收到服务端回复：{data}')
except Exception as e:
    logging.info("服务端已关闭，连接已移除，请重新启动客户端创建新连接")
finally:
    connent.close()


