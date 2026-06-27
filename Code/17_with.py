import time
from contextlib import contextmanager

#文件读取
log_data = \
"""
192.168.1.1 - - [01/Jan/2024:12:00:01] "GET /index.html" 200 1024
192.168.1.2 - - [01/Jan/2024:12:00:05] "POST /api/login" 200 256
192.168.1.1 - - [01/Jan/2024:12:00:10] "GET /about.html" 404 512
192.168.1.3 - - [01/Jan/2024:12:00:15] "GET /index.html" 200 1024
"""
#写入临时文件
with open("access.log", "w") as f:
    f.write(log_data)

with open("access.log", "r") as file:
    lines=file.readlines()
    print(f"总行数：{len(lines)}")


# 同时打开两个文件
with open("input.txt", "w") as f:
    f.write("hello world\npython with statement")

with open("input.txt","r") as inputfile, open("output.txt","w") as outputfile:
    content = inputfile.read()
    outputfile.write(content.upper())
print("已生成 output.txt")

#自定义上下文管理器
class FileCounter:
    def __init__(self,filename):
        self.filename = filename
        self.file = None
        self.line_count = 0

    def __enter__(self):
        print("开始处理文件...")
        self.file = open(self.filename, "r")  # 填空：打开文件
        return self.file  # 填空：返回文件对象
    
    def __exit__(self, exc_type, exc, tb):
        # 统计行数
        if self.file:
            # 重新读取统计行数（实际场景中可在__enter__中统计）
             # 1. 将文件读写指针移到文件最开头，才能从头重读
            self.file.seek(0)
            self.line_count = 0
            # 2. 循环遍历全部行统计
            for line in self.file:
                self.line_count += 1
        print(f"文件处理完成，共 {self.line_count} 行")
        # 关闭文件
        if self.file:
              self.file.close()
        return False  # 不吞噬异常
    
with FileCounter("access.log") as filecounter:
     for line in filecounter:
         if "200" in line:
             print(f"  [200] {line.strip()}")

#使用 contextlib
@contextmanager
def timed():
    """计算代码块执行时间的上下文管理器"""
    start = time.time()  # 记录开始时间
    yield #yield 让出控制权
    end = time.time()
    print(f"耗时: {end - start:.4f}秒")

# 使用 timed 上下文管理器
with timed():
    total = sum(i * i for i in range(1000000))
    print(f"计算完成: {total}")


#异常安全验证
class SafeResource:
    def __enter__(self):
        print("资源已获取")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("资源已释放（即使在异常发生时也会执行）")
        if exc_type:
            print(f"捕获到异常: {exc_type.__name__}")
        return False  # 不吞噬异常

try:
    with SafeResource() as resource:
        print("执行操作...")
        1/0  # 填空：引发一个异常，如 1 / 0
except ZeroDivisionError:
    print("异常被外部捕获")