import socket
import threading

clients = []  # 在线客户端列表
lock = threading.Lock()  # 线程锁

def broadcast(message, sender_conn):
    """向所有在线客户端广播消息"""
    with lock:
        for client in clients:
            if client != sender_conn:
                try:
                    client.sendall(message.encode('utf-8'))  #sendall
                except:
                    pass

def handle_client(conn, addr):
    """处理单个客户端的消息"""
    print(f"新连接: {addr}")
    with lock:
        clients.append(conn)  #append

    try:
        while True:
            data = conn.recv(1024)  #recv
            if not data:
                break
            message = data.decode('utf-8')
            if message.strip().lower() == 'quit':
                break
            broadcast(f"[{addr}]: {message}", conn)
    except ConnectionResetError:  #ConnectionResetError
        print(f"客户端 {addr} 异常断开")
    finally:
        with lock:
            if conn in clients:
                clients.remove(conn)  #remove
        conn.close()  #close
        print(f"客户端 {addr} 已断开")

# 主程序
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 9999))  # bind
server.listen(5)  # listen
print("聊天服务器启动，等待连接...")

while True:
    conn, addr = server.accept()  # accept
    t = threading.Thread(target=handle_client, args=(conn, addr))  # Thread
    t.daemon = True
    t.start()  # start