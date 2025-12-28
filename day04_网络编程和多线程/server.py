import logging
import socket
import threading

# 配置日志格式
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True   # Python 3.8+，防止被之前的配置覆盖
)
def handle_client(conn, addr):
    logging.info(f"客户端连接：{addr}")
    try:
        while True:
            data = conn.recv(1024)
            msg = data.decode("utf-8")
            logging.info(f"收到 {addr}: {msg}")
            if not msg:
                raise ConnectionRefusedError("Connection closed")

            reply = f"ACK: {msg}".encode("utf-8")
            #        给客户端去发送消息
            conn.send(reply)
    except ConnectionRefusedError:
        logging.info(f"客户端{addr}: {msg}连接断开")



def start_server():
    HOST = '0.0.0.0'
    PORT = 8080
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(100)
    logging.info(f"服务器启动，监听 {HOST}:{PORT}")
    try:
        while True:
            conn, addr = server.accept()
            t = threading.Thread(
                name=f'{addr} + "thread:" ',
                target=handle_client,
                args=(conn, addr),
                daemon=True
            )
            t.start()
    except Exception as e:
        if (type(e) == ConnectionError):
            logging.info("客户端连接关闭")
        else:
            logging.exception(f"服务异常:{e}")
            logging.info("服务器关闭")

    finally:
        server.close()


if __name__ == '__main__':
    start_server()
