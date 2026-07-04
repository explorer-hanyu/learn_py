#使用生成器读取数据流
def read_data_stream(n):
    """生成器函数：逐条生成模拟数据"""
    for i in range(1,n+1):
        yield f"第{i}条数据, 值={i*10}"

print("=== 原始数据流 ===")
stream=read_data_stream(8)
print(stream)
for data in stream:
    print(data)

#使用生成器处理数据（yield 链式处理）
def filter_positive(generator):
    """生成器函数：过滤出值大于50的数据"""
    for item in generator:
        # 解析出数值部分（假设格式固定为 "值=数字"）
        value = int(item.split("值=")[1])
        if value>50:  # 判断 value > 50
            yield item # 使用 yield 返回符合条件的 item

print("\n=== 过滤后（值 > 50）===")
stream=read_data_stream(8) #生成器是“一次性”的迭代器，无法回退或重置，此处需重新声明
filtered = filter_positive(stream)
for data in filtered:
    print(data)

#自定义迭代器类
class Counter :
    """实现 __iter__ 和 __next__ 的自定义迭代器"""
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # 返回 self

    def __next__(self):
        if self.current <= self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration  # 抛出 StopIteration 异常

print("\n=== 自定义迭代器（1 到 5）===")
for num in Counter(1, 5):
    print(num, end=" ")
print()

#手动控制迭代（next + StopIteration 处理）
print("\n=== 手动迭代 ===")
data_list = [10, 20, 30, 40, 50]
it = iter(data_list)  # 创建迭代器

# 手动获取前 3 个
print(f"第1个: {next(it)}")  # 使用 next()
print(f"第2个: {next(it)}")
print(f"第3个: {next(it)}")

# 安全遍历剩余元素
print("剩余元素：", end="")
while True:
    try:
        print(next(it), end=" ")  # 使用 next()
    except StopIteration:  # 捕获 StopIteration
        print("\n遍历结束")
        break  # 跳出循环