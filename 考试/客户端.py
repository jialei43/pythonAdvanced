import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.108.88', 8000))
data = 'hello，itheima'
client.send(data.encode('utf-8'))
print(f'已发送：{data}')
apy = client.recv(1024).decode('utf-8')
print(f'收到：{apy}')
client.close()
print('已关闭')


