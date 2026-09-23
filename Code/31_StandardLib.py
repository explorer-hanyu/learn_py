import os
import sys
import glob
import re
import random
import math
import datetime
from timeit import Timer

# ========== 1. 文件搜索 ==========
print("=== 1. 文件搜索 ===")
cwd = os.getcwd()  # 获取当前工作目录
print(f"当前目录: {cwd}")

# 查找所有 .py 文件
py_files = glob.glob('*.py')  # glob 搜索
print(f"所有 .py 文件: {py_files}")

# 使用正则表达式筛选包含数字的文件名
pattern = re.compile(r'\d')  # 编译正则表达式，匹配数字
numbered_files = [f for f in py_files if pattern.findall(f)]  # search 或 findall
print(f"包含数字的 .py 文件: {numbered_files}")

# ========== 2. 随机数据生成 ==========
print("\n=== 2. 随机数据 ===")
# 解析命令行参数
count = 20
if len(sys.argv) > 2 and sys.argv[1] == '--count':
    try:
        count = int(sys.argv[2])
    except ValueError:
        print("警告: 参数无效，使用默认值 20")

data = [random.randint(1, 100) for _ in range(count)]  # 生成随机整数
print(f"生成 {len(data)} 个随机数")
print(f"数据: {data[:10]}...")

# 数学计算
total = sum(data)
mean = total / len(data)
# 计算标准差
variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = math.sqrt(variance)  # 计算平方根
print(f"平均值: {mean:.2f}")
print(f"标准差: {std_dev:.2f}")
print(f"最大值: {max(data)}")
print(f"最小值: {min(data)}")

# ========== 3. 日期时间处理 ==========
print("\n=== 3. 日期时间 ===")
now = datetime.datetime.now()  # 获取当前时间
print(f"当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

future = now + datetime.timedelta(days=30)  # 30 天后
print(f"30 天后: {future.strftime('%Y-%m-%d')}")

target = datetime.date(2025, 1, 1)
today = datetime.date.today()  # 获取当前日期
days_left = (target - today).days  # 获取天数
print(f"距离 2025-01-01 还有 {days_left} 天")

# ========== 4. 性能测试 ==========
print("\n=== 4. 性能测试 ===")
def method1():
    return [i**2 for i in range(1000)]

def method2():
    return list(map(lambda x: x**2, range(1000)))

t1 = Timer('method1()', 'from __main__ import method1')
t2 = Timer('method2()', 'from __main__ import method2')

time1 = t1.timeit(10000)  # 执行 timeit,测试去10000次
time2 = t2.timeit(10000)
print(f"列表推导式耗时: {time1:.6f} 秒")
print(f"map + lambda 耗时: {time2:.6f} 秒")
if time1 < time2:
    print("✓ 列表推导式更快")
else:
    print("✓ map + lambda 更快")