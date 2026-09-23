# Python3 File(文件) 方法笔记

## 一、open() 方法

`open()` 方法用于打开一个文件，并返回文件对象。如果文件无法被打开，会抛出 `OSError`。

> ⚠️ **重要**：使用 `open()` 方法一定要保证关闭文件对象，即调用 `close()` 方法。

### 基本语法

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `file` | **必需**，文件路径（相对或绝对路径） |
| `mode` | 可选，文件打开模式 |
| `buffering` | 设置缓冲 |
| `encoding` | 一般使用 `utf-8` |
| `errors` | 报错级别 |
| `newline` | 区分换行符 |
| `closefd` | 传入的 file 参数类型 |
| `opener` | 设置自定义开启器，返回值必须是一个打开的文件描述符 |

### mode 参数详解

| 模式 | 描述 |
|------|------|
| `r` | **只读**（默认）。文件指针放在开头，文件必须存在 |
| `rb` | 二进制格式只读。文件指针放在开头 |
| `r+` | 读写。文件指针放在开头，文件必须存在 |
| `rb+` | 二进制格式读写。文件指针放在开头 |
| `w` | **只写**。文件存在则清空内容，不存在则创建 |
| `wb` | 二进制格式只写。存在则清空，不存在则创建 |
| `w+` | 读写。存在则清空，不存在则创建 |
| `wb+` | 二进制格式读写。存在则清空，不存在则创建 |
| `a` | **追加**。文件指针放在结尾，不存在则创建 |
| `ab` | 二进制格式追加。指针在结尾，不存在则创建 |
| `a+` | 读写（追加模式）。指针在结尾，不存在则创建 |
| `ab+` | 二进制格式读写（追加模式）。指针在结尾 |
| `t` | **文本模式**（默认） |
| `b` | **二进制模式** |
| `x` | 写模式，新建文件，如果文件已存在则报错 |
| `+` | 打开文件进行更新（可读可写） |

> **提示**：默认为文本模式，如需二进制模式，加上 `b`。


## 二、file 对象常用方法

`file` 对象使用 `open()` 函数创建，下表列出常用方法：

### 2.1 close() —— 关闭文件

关闭文件。关闭后文件不能再进行读写操作。

```python
f = open("test.txt", "r")
f.close()
```

### 2.2 flush() —— 刷新缓冲区

刷新文件内部缓冲，**立刻将缓冲区中的数据写入文件**，而不是被动等待输出缓冲区写入。

```python
f = open("test.txt", "wb")
f.write(b"Hello")
f.flush()   # 立即写入文件
f.close()
```

> **注意**：文件关闭后会自动刷新缓冲区，但有时需要在关闭前手动刷新。

### 2.3 fileno() —— 返回文件描述符

返回一个整型的**文件描述符**（file descriptor），可用于底层操作系统 I/O 操作。

```python
f = open("test.txt", "wb")
fd = f.fileno()
print(fd)   # 如: 3
f.close()
```

### 2.4 isatty() —— 检测是否连接终端

如果文件连接到一个**终端设备**返回 `True`，否则返回 `False`。

```python
f = open("test.txt", "wb")
print(f.isatty())   # False
f.close()
```

### 2.5 read([size]) —— 读取文件

从文件读取指定的字节数，如果未给定或为负则**读取所有**。

```python
f = open("test.txt", "r")
content = f.read()      # 读取全部
partial = f.read(100)   # 读取100个字符
f.close()
```

### 2.6 readline([size]) —— 读取一行

读取整行，包括 `\n` 字符。

```python
f = open("test.txt", "r")
line = f.readline()     # 读取一行
f.close()
```

### 2.7 readlines([sizeint]) —— 读取所有行

读取所有行并返回**列表**。若给定 `sizeint > 0`，返回总和大约为 `sizeint` 字节的行。

```python
f = open("test.txt", "r")
lines = f.readlines()   # ['第一行\n', '第二行\n']
f.close()
```

### 2.8 seek(offset[, whence]) —— 移动文件指针

移动文件读取指针到指定位置。

| `whence` 值 | 含义 |
|-------------|------|
| `0`（默认） | 从文件**开头**开始算起 |
| `1` | 从**当前位置**开始算起 |
| `2` | 从文件**末尾**开始算起 |

```python
f = open("test.txt", "rb+")
f.write(b'0123456789abcdef')
f.seek(5)           # 移动到第6个字节
f.read(1)           # b'5'
f.seek(-3, 2)       # 移动到倒数第3个字节
f.read(1)           # b'd'
f.close()
```

> `offset` 为负数表示从倒数第几位开始。

### 2.9 tell() —— 返回文件指针位置

返回文件当前位置（从文件开头开始的字节数偏移量）。

```python
f = open("test.txt", "r")
pos = f.tell()      # 当前位置
f.close()
```

### 2.10 truncate([size]) —— 截断文件

从文件首行首字符开始截断，截断文件为 `size` 个字节。无 `size` 表示从**当前位置截断至末尾**。

```python
f = open("test.txt", "r+")
f.truncate(30)      # 保留前30个字节
f.close()
```

> **注意**：Windows 系统下换行代表 **2 个字节**大小。

### 2.11 write(str) —— 写入字符串

将字符串写入文件，**返回写入的字符长度**。

```python
f = open("test.txt", "w")
length = f.write("Hello World")
print(length)       # 11
f.close()
```

> **注意**：在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，文件中看不到写入的内容。如果文件打开模式带 `b`，写入内容需用 `encode` 方法转为 `bytes` 形式。

### 2.12 writelines(sequence) —— 写入多行

向文件写入一个**序列字符串列表**（如列表或元组），如需换行需自己加入 `\n`。

```python
lines = ["第一行\n", "第二行\n", "第三行"]
f = open("test.txt", "w")
f.writelines(lines)
f.close()
```


## 三、方法速查表

| 方法 | 描述 |
|------|------|
| `close()` | 关闭文件 |
| `flush()` | 刷新缓冲区，立即写入文件 |
| `fileno()` | 返回整型文件描述符 |
| `isatty()` | 判断是否连接终端设备 |
| `read([size])` | 读取指定字节数，默认读取全部 |
| `readline([size])` | 读取一行 |
| `readlines([sizeint])` | 读取所有行，返回列表 |
| `seek(offset[, whence])` | 移动文件指针 |
| `tell()` | 返回文件指针当前位置 |
| `truncate([size])` | 截断文件 |
| `write(str)` | 写入字符串，返回写入长度 |
| `writelines(sequence)` | 写入字符串序列 |


## 四、重点总结

| 知识点 | 要点 |
|--------|------|
| **open()** | 打开文件，返回文件对象，需配合 `close()` 使用 |
| **模式** | `r` 只读、`w` 写入（覆盖）、`a` 追加、`b` 二进制、`+` 读写 |
| **读取** | `read()` 全部、`readline()` 一行、`readlines()` 全部行列表 |
| **写入** | `write()` 写字符串、`writelines()` 写字符串序列 |
| **指针操作** | `seek()` 移动指针、`tell()` 获取当前位置 |
| **缓冲区** | `flush()` 手动刷新缓冲区 |
| **截断** | `truncate()` 截断文件到指定大小 |
| **最佳实践** | 使用 `with open()` 自动管理文件关闭 |

---


# 📝 综合练习题

## 任务：日志文件分析工具

编写一个名为 `log_analyzer.py` 的程序，在一个综合场景中运用文件方法的各类知识。

> 本练习覆盖：`open()` 不同模式（`r`/`w`/`a`/`r+`）、`read()`/`readline()`/`readlines()`、`write()`/`writelines()`、`seek()`/`tell()`、`truncate()`、`flush()`、`close()`


### 场景描述

你有一个应用程序的日志文件 `app.log`，需要开发一个分析工具来读取、处理、清理和生成报告。


### 具体要求

**1. 准备初始日志数据**

使用 `open()` 的 `w` 模式创建 `app.log` 文件，写入以下内容：

```
[2024-01-15 10:00:01] INFO - 应用启动
[2024-01-15 10:05:23] ERROR - 数据库连接超时
[2024-01-15 10:10:45] INFO - 用户登录成功
[2024-01-15 10:15:12] WARNING - 磁盘空间不足
[2024-01-15 10:20:33] ERROR - 文件未找到
[2024-01-15 10:25:01] INFO - 应用关闭
```

**2. 读取与分析（readlines + tell/seek）**

- 使用 `readlines()` 读取所有日志行，统计总行数
- 统计 `ERROR` 出现的次数（逐行判断）
- 使用 `tell()` 获取当前文件指针位置，打印
- 使用 `seek(0, 0)` 将指针移回文件开头

**3. 读取指定行（readline + 指针操作）**

- 使用 `seek(0, 0)` 回到开头
- 使用 `readline()` 逐行读取，只打印**包含 `ERROR` 的行**
- 再次打印 `tell()` 查看指针位置

**4. 写入分析报告（write + writelines）**

- 以 `w` 模式打开 `report.txt`
- 使用 `write()` 写入报告标题和统计信息
- 使用 `writelines()` 写入所有 ERROR 日志行（每行需带 `\n`）

**5. 追加新日志（追加模式 a）**

- 以 `a` 模式打开 `app.log`
- 追加两条新的日志：
  - `[2024-01-15 10:30:00] INFO - 清理完成`
  - `[2024-01-15 10:35:00] ERROR - 磁盘已满`

**6. 截断日志（truncate + flush）**

- 以 `r+` 模式打开 `app.log`
- 使用 `truncate(50)` 截断文件到前 50 个字节，观察效果
- 使用 `flush()` 刷新缓冲区
- 关闭文件后重新打开查看截断后的内容

**7. 综合清理与重新生成**

- 使用 `w` 模式重新打开 `app.log`，写入清理后的日志（只保留 INFO 和 WARNING，过滤掉 ERROR）
- 验证新文件内容


### 代码框架（填空版）

```python
# ========== 1. 准备初始数据 ==========
initial_logs = [
    "[2024-01-15 10:00:01] INFO - 应用启动\n",
    "[2024-01-15 10:05:23] ERROR - 数据库连接超时\n",
    "[2024-01-15 10:10:45] INFO - 用户登录成功\n",
    "[2024-01-15 10:15:12] WARNING - 磁盘空间不足\n",
    "[2024-01-15 10:20:33] ERROR - 文件未找到\n",
    "[2024-01-15 10:25:01] INFO - 应用关闭\n",
]

with open("app.log", "______") as f:      # 填空：写入模式
    f.______(initial_logs)                # 填空：写入多行

print("✓ 初始日志已创建")

# ========== 2. 读取与分析 ==========
print("\n=== 2. 读取与分析 ===")
with open("app.log", "r") as f:
    lines = f.______()                    # 填空：读取所有行
    total = len(lines)
    error_count = 0
    for line in lines:
        if "ERROR" in line:
            error_count += 1
    print(f"总行数: {total}")
    print(f"ERROR 数量: {error_count}")

# ========== 3. 指针操作 ==========
print("\n=== 3. 指针操作 ===")
f = open("app.log", "r")
print(f"初始指针位置: {f.______()}")      # 填空：tell()

# 读取第一行
first_line = f.______()                   # 填空：readline()
print(f"第一行: {first_line.strip()}")
print(f"读取后指针位置: {f.______()}")    # 填空：tell()

# 移回开头
f.______(0, 0)                            # 填空：seek
print(f"重置后指针位置: {f.tell()}")

# 读取并打印所有 ERROR 行
print("\n--- ERROR 日志 ---")
for line in f:
    if "ERROR" in line:
        print(line.strip())
f.close()

# ========== 4. 生成报告 ==========
print("\n=== 4. 生成报告 ===")
with open("app.log", "r") as f:
    all_lines = f.readlines()

with open("report.txt", "______") as f:   # 填空：写入模式
    f.______("=== 日志分析报告 ===\n")    # 填空：write()
    f.write(f"总日志数: {len(all_lines)}\n")
    error_lines = [line for line in all_lines if "ERROR" in line]
    f.write(f"ERROR 数: {len(error_lines)}\n")
    f.write("\n--- ERROR 详情 ---\n")
    f.______(error_lines)                 # 填空：writelines()
print("✓ 报告已生成")

# ========== 5. 追加新日志 ==========
print("\n=== 5. 追加新日志 ===")
with open("app.log", "______") as f:      # 填空：追加模式
    f.write("[2024-01-15 10:30:00] INFO - 清理完成\n")
    f.write("[2024-01-15 10:35:00] ERROR - 磁盘已满\n")
print("✓ 新日志已追加")

# ========== 6. 截断测试 ==========
print("\n=== 6. 截断测试 ===")
f = open("app.log", "______")             # 填空：读写模式
print(f"截断前指针位置: {f.tell()}")
f.______(50)                              # 填空：truncate
f.______()                                # 填空：flush
f.close()
print("✓ 文件已截断到50字节")

# 验证截断结果
with open("app.log", "r") as f:
    content = f.read()
    print(f"截断后内容（前100字符）:\n{content[:100]}...")

# ========== 7. 清理并重新生成 ==========
print("\n=== 7. 清理日志（过滤 ERROR）===")
with open("app.log", "r") as f:
    all_lines = f.readlines()

clean_lines = [line for line in all_lines if "ERROR" not in line]

with open("app.log", "______") as f:      # 填空：写入模式（覆盖）
    f.writelines(clean_lines)

print(f"✓ 已清理，保留 {len(clean_lines)} 条日志")

# 验证最终结果
with open("app.log", "r") as f:
    print("最终日志内容：")
    for line in f:
        print(f"  {line.strip()}")
```


### 自测检查清单

- [ ] 是否使用了 `r`、`w`、`a`、`r+` 四种不同的打开模式？
- [ ] 是否使用了 `readlines()` 读取所有行？
- [ ] 是否使用了 `readline()` 读取单行？
- [ ] 是否使用了 `write()` 和 `writelines()` 写入文件？
- [ ] 是否使用了 `seek()` 移动文件指针？
- [ ] 是否使用了 `tell()` 获取指针位置？
- [ ] 是否使用了 `truncate()` 截断文件？
- [ ] 是否使用了 `flush()` 刷新缓冲区？
- [ ] 是否使用了 `close()` 关闭文件？
- [ ] 代码是否无语法错误，能正确运行？
