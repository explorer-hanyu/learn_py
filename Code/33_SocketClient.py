import socket
import threading
import sys

def receive_messages(sock):
    """持续接收服务器消息"""
    while True:
        try:
            data = sock.recv(1024)  # recv
            if not data:
                break
            print(f"\n{data.decode('utf-8')}")
        except:
            break

# 连接服务器
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(('localhost', 9999))  # connect
except ConnectionRefusedError:  # ConnectionRefusedError
    print("无法连接服务器，请确认服务器已启动")
    sys.exit()

# 启动接收线程
t = threading.Thread(target=receive_messages, args=(client,))
t.daemon = True
t.start()  # start

print("已连接到聊天室，输入消息发送（输入 quit 退出）")

while True:
    msg = input()
    if msg.strip().lower() == 'quit':
        break
    client.sendall(msg.encode('utf-8'))  # sendall

client.close()