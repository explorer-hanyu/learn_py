# Python3 with 关键字笔记

## 一、概述

`with` 是 Python 中的一个关键字，用于**上下文管理协议**（Context Management Protocol）。它简化了资源管理代码，特别是那些需要明确释放或清理的资源（如文件、网络连接、数据库连接等）。

> **一句话理解**：`with` 就像一个"自动资源管家"——进入时帮你准备好资源，退出时（不管成功还是出错）自动帮你清理释放。


## 二、为什么需要 with 语句？

### 2.1 传统资源管理的问题

以文件操作为例，传统写法需要使用 `try...finally` 来确保资源被释放：

```python
file = open('example.txt', 'r')
try:
    content = file.read()
    # 处理文件内容
finally:
    file.close()
```

这种写法存在几个问题：
- **容易忘记关闭资源**：如果没有 `try...finally` 块，可能会忘记调用 `close()`
- **代码冗长**：简单的文件操作需要多行代码
- **异常处理复杂**：需要手动处理可能出现的异常

### 2.2 with 语句的优势

`with` 语句通过上下文管理协议解决了这些问题：

| 优势 | 说明 |
|------|------|
| **自动资源释放** | 确保资源在使用后被正确关闭 |
| **代码简洁** | 减少样板代码 |
| **异常安全** | 即使在代码块中发生异常，资源也会被正确释放 |
| **可读性强** | 明确标识资源的作用域 |


## 三、基本语法

```python
with expression [as variable]:
    # 代码块
```

- `expression`：返回一个支持上下文管理协议的对象
- `as variable`：可选的，用于将表达式结果赋值给变量
- 代码块执行完毕后，自动调用清理方法

### 文件操作示例

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# 文件已自动关闭
```

这段代码等价于前面的 `try...finally` 实现，但更加简洁明了。


## 四、工作原理

### 4.1 上下文管理协议

`with` 语句背后是 Python 的上下文管理协议，该协议要求对象实现两个方法：

| 方法 | 调用时机 | 作用 |
|------|----------|------|
| `__enter__()` | 进入 `with` 代码块时 | 执行预处理，返回值赋给 `as` 后的变量 |
| `__exit__()` | 退出 `with` 代码块时 | 执行清理工作（关闭资源、释放锁等） |

### 4.2 执行流程

```
1. 调用 expression 的 __enter__() 方法
2. 将 __enter__() 的返回值赋给 as 后的变量
3. 执行 with 代码块
4. 代码块执行完毕后（无论是否发生异常），调用 __exit__() 方法
```

### 4.3 异常处理机制

`__exit__()` 方法接收三个参数：
- `exc_type`：异常类型
- `exc_val`：异常值
- `exc_tb`：异常追踪信息

- 如果 `__exit__()` 返回 `True`，表示异常已被处理，不会继续传播
- 返回 `False` 或 `None`，异常会继续向外传播


## 五、常见应用场景

### 1. 文件操作

```python
# 单文件
with open('input.txt', 'r') as file:
    content = file.read()

# 同时打开多个文件
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content.upper())
```

> **提示**：从 Python 3.10 起，还可以用括号将多个 `with` 语句括起来。

### 2. 数据库连接

```python
import sqlite3

with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
# 连接自动关闭
```

### 3. 线程锁

```python
import threading

lock = threading.Lock()
with lock:
    # 临界区代码
    print("这段代码是线程安全的")
# 锁自动释放
```

### 4. 临时修改系统状态

```python
import decimal

with decimal.localcontext() as ctx:
    ctx.prec = 42  # 临时设置高精度
    # 执行高精度计算
# 精度自动恢复原设置
```


## 六、创建自定义上下文管理器

### 6.1 类实现方式

通过实现 `__enter__` 和 `__exit__` 方法创建自定义的上下文管理器：

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"耗时: {self.end - self.start:.2f}秒")
        return False  # 异常不吞噬，继续向外传播

# 使用示例
with Timer() as t:
    sum(range(1000000))
# 输出: 耗时: 0.05秒
```

### 6.2 使用 contextlib 模块（更简单）

```python
from contextlib import contextmanager

@contextmanager
def tag(name):
    print(f"<{name}>")
    yield
    print(f"</{name}>")

# 使用示例
with tag("h1"):
    print("hello")
    print("world")
# 输出:
# <h1>
# hello
# world
# </h1>
```

`@contextmanager` 装饰器可以将一个生成器函数转换为上下文管理器：
- `yield` 之前的代码相当于 `__enter__`
- `yield` 之后的代码相当于 `__exit__`


## 七、最佳实践

| 实践 | 说明 |
|------|------|
| **用于资源管理** | 对于文件、数据库和网络连接，首选 `with` |
| **利用内置管理器** | 许多 Python 对象（如文件和锁）已经支持上下文管理 |
| **创建自定义管理器** | 为复杂资源实现 `__enter__`/`__exit__` |
| **使用 contextlib** | 对于简单的上下文管理器，优先使用 `@contextmanager` 装饰器 |


## 八、重点总结

| 知识点 | 要点 |
|--------|------|
| **作用** | 自动管理资源，确保资源被正确释放 |
| **核心协议** | `__enter__()` + `__exit__()` |
| **语法** | `with expression [as variable]:` |
| **常见用途** | 文件操作、数据库连接、线程锁、临时状态修改 |
| **自定义方式** | 类实现（`__enter__`/`__exit__`）或 `@contextmanager` 装饰器 |
| **异常处理** | `__exit__()` 返回 `True` 吞噬异常，返回 `False` 传播异常 |

---


# 📝 综合练习题

## 任务：资源管理器实战

编写一个名为 `resource_manager.py` 的程序，在一个综合场景中运用 `with` 语句的多种用法。

> 本练习覆盖：`with` 文件操作、多文件同时打开、自定义上下文管理器（类实现）、`contextlib.contextmanager` 装饰器


### 场景描述

你需要开发一个**日志分析工具**，读取日志文件、处理数据、生成报告，并确保所有资源都被正确释放。


### 具体要求

**1. 文件读取（基础 with）**

使用 `with` 语句打开文件 `access.log`（内容见下方数据），读取所有行并打印行数。

```python
# access.log 内容（直接写在代码中作为测试数据）
log_data = """192.168.1.1 - - [01/Jan/2024:12:00:01] "GET /index.html" 200 1024
192.168.1.2 - - [01/Jan/2024:12:00:05] "POST /api/login" 200 256
192.168.1.1 - - [01/Jan/2024:12:00:10] "GET /about.html" 404 512
192.168.1.3 - - [01/Jan/2024:12:00:15] "GET /index.html" 200 1024
"""
```

> 提示：由于是练习环境，可以先写入临时文件再读取，或直接使用 `io.StringIO` 模拟。

**2. 多文件操作（同时打开多个文件）**

使用一个 `with` 语句同时打开 `input.txt` 和 `output.txt`，将 `input.txt` 的内容转换为大写后写入 `output.txt`。

**3. 自定义上下文管理器（类实现）**

创建一个 `FileCounter` 类，实现上下文管理协议：
- `__enter__()`：打开文件并返回文件对象，同时打印 `"开始处理文件..."`
- `__exit__()`：关闭文件，统计并打印读取的行数，打印 `"文件处理完成"`
- 使用该类读取 `access.log`，统计包含 `"200"` 的行数

**4. 使用 contextlib（装饰器实现）**

使用 `@contextmanager` 装饰器创建一个上下文管理器 `timed()`：
- 进入时记录开始时间
- `yield` 执行代码块
- 退出时计算并打印耗时（秒）
- 使用 `with timed():` 包裹一段耗时操作（如循环计算）

**5. 异常安全验证**

在自定义上下文管理器中，故意在 `with` 代码块内引发一个异常（如 `1 / 0`），验证 `__exit__()` 是否仍会被执行。


### 代码框架（填空版）

```python
import time
from contextlib import contextmanager

# ========== 数据准备 ==========
log_data = """192.168.1.1 - - [01/Jan/2024:12:00:01] "GET /index.html" 200 1024
192.168.1.2 - - [01/Jan/2024:12:00:05] "POST /api/login" 200 256
192.168.1.1 - - [01/Jan/2024:12:00:10] "GET /about.html" 404 512
192.168.1.3 - - [01/Jan/2024:12:00:15] "GET /index.html" 200 1024
"""

# 写入临时文件供后续使用
with open("access.log", "w") as f:
    f.write(log_data)

# ========== 1. 基础文件读取 ==========
print("=== 1. 读取日志文件 ===")
with ______("access.log", "r") as file:  # 填空：使用 open
    lines = file.readlines()
    print(f"总行数: {len(lines)}")

# ========== 2. 多文件操作 ==========
print("\n=== 2. 多文件操作 ===")
# 创建输入文件
with open("input.txt", "w") as f:
    f.write("hello world\npython with statement")

# 同时打开两个文件
with ______("input.txt", "r") as infile, ______("output.txt", "w") as outfile:
    content = infile.read()
    outfile.write(content.upper())
print("已生成 output.txt")

# ========== 3. 自定义上下文管理器（类实现）==========
print("\n=== 3. 自定义上下文管理器 ===")
class FileCounter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.line_count = 0

    def __enter__(self):
        print("开始处理文件...")
        self.file = ______(self.filename, "r")  # 填空：打开文件
        ______ self.file  # 填空：返回文件对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 统计行数
        if self.file:
            # 重新读取统计行数（实际场景中可在__enter__中统计）
            pass
        print(f"文件处理完成，共 {self.line_count} 行")
        # 关闭文件
        if self.file:
            ______  # 填空：关闭文件
        return False  # 不吞噬异常

# 使用 FileCounter 读取文件并统计包含 "200" 的行数
with FileCounter("access.log") as f:
    for line in f:
        if "200" in line:
            print(f"  [200] {line.strip()}")

# ========== 4. contextlib 装饰器 ==========
print("\n=== 4. contextlib 装饰器 ===")
@contextmanager
def timed():
    """计算代码块执行时间的上下文管理器"""
    start = ______  # 填空：记录开始时间
    ______  # 填空：yield 让出控制权
    end = time.time()
    print(f"耗时: {end - start:.4f}秒")

# 使用 timed 上下文管理器
with timed():
    total = sum(i * i for i in range(1000000))
    print(f"计算完成: {total}")

# ========== 5. 异常安全验证 ==========
print("\n=== 5. 异常安全验证 ===")
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
        ______  # 填空：引发一个异常，如 1 / 0
except ZeroDivisionError:
    print("异常被外部捕获")
```


### 预期输出示例

```
=== 1. 读取日志文件 ===
总行数: 4

=== 2. 多文件操作 ===
已生成 output.txt

=== 3. 自定义上下文管理器 ===
开始处理文件...
  [200] 192.168.1.1 - - [01/Jan/2024:12:00:01] "GET /index.html" 200 1024
  [200] 192.168.1.2 - - [01/Jan/2024:12:00:05] "POST /api/login" 200 256
  [200] 192.168.1.3 - - [01/Jan/2024:12:00:15] "GET /index.html" 200 1024
文件处理完成，共 4 行

=== 4. contextlib 装饰器 ===
计算完成: 333332833500
耗时: 0.0523秒

=== 5. 异常安全验证 ===
资源已获取
执行操作...
资源已释放（即使在异常发生时也会执行）
捕获到异常: ZeroDivisionError
异常被外部捕获
```


### 自测检查清单

- [ ] 是否使用 `with open()` 读取了文件？
- [ ] 是否使用一个 `with` 语句同时打开了两个文件？
- [ ] 是否创建了实现 `__enter__` 和 `__exit__` 的自定义上下文管理器类？
- [ ] 是否使用 `@contextmanager` 装饰器创建了上下文管理器？
- [ ] 是否验证了异常发生时 `__exit__` 仍会被执行？
- [ ] 代码是否无语法错误，能正确运行？
