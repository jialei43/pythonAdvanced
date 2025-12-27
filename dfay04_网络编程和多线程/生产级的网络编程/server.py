# 导入 socket 模块，用于网络通信
import socket

# 导入 threading，用于多客户端并发处理
import threading

# struct 用于二进制数据的打包 / 解包（解决粘包问题）
import struct

# logging 用于生产级日志（替代 print）
import logging


# 配置日志格式
logging.basicConfig(
    level=logging.INFO,                     # 日志级别
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# 监听的 IP，0.0.0.0 表示监听所有网卡
HOST = "0.0.0.0"

# 监听端口
PORT = 9000


def recv_all(conn,length):
    """
    从 socket 中接收指定长度的数据
    TCP 是流协议，recv() 可能收不完整
    """
    data = b""                              # 保存已接收的数据
    while len(data) < length :               # 未接收够指定长度
        chunk = conn.recv(length -len(data))  # 继续接收剩余部分
        if not chunk:                       # 客户端断开
            raise ConnectionError("客户端断开")
        data += chunk                       # 拼接数据
    return data                             # 返回完整数据


def recv_message(conn):
    """
    接收一条完整消息（长度 + 数据）
    """
    # 先读取 4 字节消息头（网络字节序）
    header = recv_all(conn, 4)

    # 解包，!I 表示网络字节序的 unsigned int
    msg_len = struct.unpack("!I", header)[0]

    # 再读取真正的数据部分
    return recv_all(conn, msg_len)


def send_message(conn, data: bytes):
    """
    发送一条完整消息
    """
    # 把数据长度打包成 4 字节
    header = struct.pack("!I", len(data))

    # sendall 保证全部发送完
    conn.sendall(header + data)


def handle_client(conn, addr):
    """
    处理单个客户端连接
    """
    logging.info(f"客户端连接：{addr}")

    try:
        while True:
            # 接收客户端发来的完整消息
            data = recv_message(conn)

            # 将字节数据解码为字符串
            msg = data.decode("utf-8")

            logging.info(f"收到 {addr}: {msg}")

            # 构造回复消息
            reply = f"ACK: {msg}".encode("utf-8")

            # 发送回复
            send_message(conn, reply)

    except (ConnectionError, OSError):
        # 客户端断开或网络异常
        logging.info(f"客户端断开：{addr}")

    finally:
        # 关闭连接 socket
        conn.close()


def start_server():
    """
    启动 TCP 服务端
    """
    # 创建 TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 允许端口快速复用（避免 TIME_WAIT）
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定 IP 和端口
    server.bind((HOST, PORT))

    # 开始监听，最大连接队列为 100
    server.listen(100)

    logging.info(f"服务器启动，监听 {HOST}:{PORT}")

    try:
        while True:
            # 接受客户端连接（阻塞）
            conn, addr = server.accept()

            # 为每个客户端创建一个线程
            t = threading.Thread(
                target=handle_client,       # 线程执行函数
                args=(conn, addr),           # 参数
                daemon=True                  # 主线程退出时自动结束
            )

            # 启动线程
            t.start()

    except KeyboardInterrupt:
        # Ctrl + C 优雅退出
        logging.info("服务器关闭")

    finally:
        # 关闭监听 socket
        server.close()


# 程序入口
if __name__ == "__main__":
    start_server()
