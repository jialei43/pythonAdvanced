import logging
import socket

# HOST = '127.0.0.1'
HOST = '192.168.32.144'

PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))

try:
    while True:
        message = input('请输入要发送的内容')
        if message == 'q':
            break
        client.send(message.encode('utf-8'))
        print(f'已发送消息：{message}')
        rply = client.recv(1024).decode('utf-8')
        print(f'收到服务器回复：{rply}')

except Exception as e:
    logging.exception(e)
finally:
    client.close()