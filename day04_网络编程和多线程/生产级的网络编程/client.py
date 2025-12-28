# 导入 socket 模块
import socket

# struct 用于打包 / 解包消息头
import struct


# 服务器 IP
HOST = "127.0.0.1"

# 服务器端口
PORT = 9000


def recv_all(sock, length):
    """
    接收指定长度的数据
    """
    data = b""
    while len(data) < length:
        chunk = sock.recv(length - len(data))
        if not chunk:
            raise ConnectionError("服务器断开")
        data += chunk
    return data


def recv_message(sock):
    """
    接收一条完整消息
    """
    # 先接收 4 字节长度头
    header = recv_all(sock, 4)

    # 解包长度
    msg_len = struct.unpack("!I", header)[0]

    # 再接收真实数据
    return recv_all(sock, msg_len)


def send_message(sock, data: bytes):
    """
    发送一条完整消息
    """
    # 打包数据长度
    header = struct.pack("!I", len(data))

    # 发送长度 + 数据
    sock.sendall(header + data)


def start_client():
    """
    启动客户端
    """
    # 创建 TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    sock.connect((HOST, PORT))

    try:
        while True:
            # 从终端读取输入
            msg = input("请输入(q退出)：")

            if msg == "q":
                break

            # 发送消息
            send_message(sock, msg.encode("utf-8"))

            # 接收服务器回复
            reply = recv_message(sock)

            print("服务器回复:", reply.decode("utf-8"))

    finally:
        # 关闭 socket
        sock.close()


# 程序入口
if __name__ == "__main__":
    start_client()
