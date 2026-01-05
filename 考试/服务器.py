# 题目：使用套接字编程完成TCP客户端开发，连接服务器地址：192.168.108.88，端口号为8000，客户端主动向服务器端发送文本"hello，itheima"，并接受服务器端返回结果。
import logging
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('192.168.108.88',8000))
server.listen(128)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True
)
logging.info("服务器启动，等待连接...")

def accept(conn, addr):
    try:
        while True:
            data = conn.recv(1024)
            if not data:  # 客户端关闭
                logging.info("客户端断开：{addr}")
                break
            logging.info(f"收到{addr}：{data.decode()}")
            conn.sendall(data)  # 回写
            logging.info(f'回复客户端：{data.decode()}')
    except Exception as e:
        logging.info("服务端发生异常")
        logging.exception(e)
    finally:
        conn.close()

while True:
    conn, addr = server.accept()   # ✅ 只在“新连接”时返回，不然一直阻塞
    logging.info(f'客户端{addr}已连接')
    threading.Thread(target=accept, args=(conn, addr),name=f'{addr}客户端线程').start()