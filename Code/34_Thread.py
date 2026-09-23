import threading
import queue
import time

# ========== 全局变量 ==========
task_queue = queue.Queue()          # 创建 FIFO 队列
log_lock = threading.Lock()        # 创建锁
exit_flag = False

# ========== 下载线程类 ==========
class DownloadThread(threading.Thread):
    def __init__(self, thread_id, name, q, lock):
        threading.Thread.__init__(self)  # 调用父类构造方法
        self.thread_id = thread_id
        self.name = name
        self.q = q
        self.lock = lock

    def run(self):
        with self.lock:
            print(f"开启线程：{self.name}")
        while not exit_flag:
            try:
                # 从队列获取任务，超时 1 秒
                filename = self.q.get(timeout=1)  # get
                download_file(self.name, filename, self.lock)
                self.q.task_done()  # task_done
            except queue.Empty:  # Empty
                continue
        with self.lock:
            print(f"退出线程：{self.name}")

# ========== 下载处理函数 ==========
def download_file(thread_name, filename, lock):
    with lock:
        print(f"[{thread_name}] 开始下载: {filename}")
    time.sleep(1)  # 模拟下载耗时
    with lock:
        print(f"[{thread_name}] 下载完成: {filename}")

# ========== 主程序 ==========
if __name__ == "__main__":
    # 待下载文件列表
    files = ["file1.zip", "file2.mp4", "file3.pdf",
             "file4.jpg", "file5.doc", "file6.mp3"]

    # 填充队列
    for f in files:
        task_queue.put(f)  # put

    # 创建并启动下载线程
    threads = []
    for i in range(1, 4):
        thread = DownloadThread(i, f"Downloader-{i}", task_queue, log_lock)
        thread.start()  # start
        threads.append(thread)  # append

    # 等待所有线程完成
    for t in threads:
        t.join()  # join

    # 通知线程退出
    exit_flag = True

    # 等待队列清空
    task_queue.join()  # join

    print("\n所有下载任务完成")