# Python3 输入和输出笔记

## 一、输出格式美化

Python 有两种输出值的方式：**表达式语句**和 **`print()` 函数**。此外，还可以使用文件对象的 `write()` 方法，标准输出文件可以用 `sys.stdout` 引用。

### 1.1 str() 与 repr() 的区别

如果你希望将输出的值转成字符串，可以使用 `repr()` 或 `str()` 函数：

| 函数 | 特点 |
|------|------|
| `str()` | 返回**用户易读**的表达形式 |
| `repr()` | 产生**解释器易读**的表达形式，会转义特殊字符 |

```python
>>> s = 'Hello, Runoob'
>>> str(s)
'Hello, Runoob'
>>> repr(s)
"'Hello, Runoob'"          # 注意多了一层引号
>>> hello = 'hello, runoob\n'
>>> repr(hello)
"'hello, runoob\\n'"        # 转义字符被保留
>>> repr((10, 20, ('Google', 'Runoob')))
"(10, 20, ('Google', 'Runoob'))"
```

### 1.2 字符串对齐方法

| 方法 | 作用 |
|------|------|
| `rjust(n)` | 字符串靠右，左边填充空格 |
| `ljust(n)` | 字符串靠左，右边填充空格 |
| `center(n)` | 字符串居中 |
| `zfill(n)` | 在数字左边填充 0 |

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)   # 长度已够，不填充
'3.14159265359'
```

**示例：打印平方与立方表（使用 rjust）**

```python
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))
```

### 1.3 str.format() 格式化（推荐）

`str.format()` 是较新的字符串格式化方法，**建议优先使用**。

**基本用法：**

```python
>>> print('{}网址："{}!"'.format('菜鸟教程', 'www.runoob.com'))
菜鸟教程网址："www.runoob.com!"
```

**按位置引用：**

```python
>>> print('{0} 和 {1}'.format('Google', 'Runoob'))
Google 和 Runoob
>>> print('{1} 和 {0}'.format('Google', 'Runoob'))
Runoob 和 Google
```

**关键字参数：**

```python
>>> print('{name}网址：{site}'.format(name='菜鸟教程', site='www.runoob.com'))
菜鸟教程网址：www.runoob.com
```

**位置与关键字结合：**

```python
>>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
站点列表 Google, Runoob, 和 Taobao。
```

**转换标识符 `!`：**

| 标识符 | 作用 |
|--------|------|
| `!s` | 使用 `str()` 转换 |
| `!r` | 使用 `repr()` 转换 |
| `!a` | 使用 `ascii()` 转换 |

```python
>>> import math
>>> print('常量 PI 的值近似为：{!r}。'.format(math.pi))
常量 PI 的值近似为：3.141592653589793。
```

**格式说明符 `:`：**

```python
>>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
常量 PI 的值近似为 3.142。
```

**美化表格：**

```python
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> for name, number in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, number))
Google     ==>          1
Runoob     ==>          2
Taobao     ==>          3
```

**通过字典解包：**

```python
>>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
>>> print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
Runoob: 2; Google: 1; Taobao: 3
```

### 1.4 旧式字符串格式化（% 操作符）

```python
>>> import math
>>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
常量 PI 的值近似为：3.142。
```

> ⚠️ **注意**：旧式格式化最终会从 Python 中移除，**建议使用 `str.format()`**。


## 二、读取键盘输入

Python 提供 `input()` 内置函数从标准输入读入一行文本，默认的标准输入是键盘。

```python
#!/usr/bin/python3
str = input("请输入：")
print("你输入的内容是: ", str)
```

**运行效果：**
```
请输入：菜鸟教程
你输入的内容是: 菜鸟教程
```


## 三、读写文件

### 3.1 open() 函数

`open()` 函数返回一个文件对象（file object），用于后续的读取或写入操作。

```python
open(filename, mode)
```

- `filename`：要访问的文件路径（字符串）
- `mode`：文件打开模式，可选，默认值为 `r`（只读）

### 3.2 文件打开模式速查表

| 模式 | 描述 |
|------|------|
| `r` | 只读（默认），文件必须存在，指针在开头 |
| `rb` | 二进制只读，文件必须存在 |
| `r+` | 读写，文件必须存在，指针在开头 |
| `rb+` | 二进制读写，指针在开头 |
| `w` | 只写，文件存在则清空，不存在则创建 |
| `wb` | 二进制只写，存在则清空，不存在则创建 |
| `w+` | 读写，存在则清空，不存在则创建 |
| `wb+` | 二进制读写，存在则清空，不存在则创建 |
| `a` | 追加，存在则追加到末尾，不存在则创建 |
| `ab` | 二进制追加 |
| `a+` | 读写，指针在末尾（追加模式） |
| `ab+` | 二进制读写，指针在末尾 |

> 在模式后添加 `b` 表示以二进制方式操作文件，常用于处理图片、音频等非文本文件。

### 3.3 写入示例

```python
#!/usr/bin/python3
f = open("/tmp/foo.txt", "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
f.close()
```


## 四、文件对象方法

### 4.1 f.read(size)

读取一定数目的数据，作为字符串或字节对象返回。

- `size` 为可选参数，省略或为负数时读取整个文件

```python
f = open("/tmp/foo.txt", "r")
str = f.read()
print(str)
f.close()
```

### 4.2 f.readline()

读取单独的一行，换行符为 `\n`。返回空字符串表示已到达文件末尾。

```python
f = open("/tmp/foo.txt", "r")
str = f.readline()
print(str)
f.close()
```

### 4.3 f.readlines()

返回文件中包含的所有行组成的列表。

```python
f = open("/tmp/foo.txt", "r")
str = f.readlines()
print(str)   # ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
f.close()
```

### 4.4 迭代文件对象

可以直接迭代文件对象逐行读取：

```python
f = open("/tmp/foo.txt", "r")
for line in f:
    print(line, end='')
f.close()
```

> **注意**：`readline()` 和直接迭代文件对象的处理机制不同，最好不要混用。

### 4.5 f.write(string)

将字符串写入文件，返回写入的字符数。

```python
f = open("/tmp/foo.txt", "w")
num = f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
print(num)   # 29
f.close()
```

如果要写入非字符串内容，需要先进行转换：

```python
value = ('www.runoob.com', 14)
s = str(value)
f.write(s)
```

### 4.6 f.tell()

返回文件当前的读/写位置（从文件开头开始的字节数偏移量）。

### 4.7 f.seek(offset, whence)

移动文件指针到指定位置。

| `whence` 值 | 含义 |
|-------------|------|
| `0` | 从文件开头开始 |
| `1` | 从当前位置开始 |
| `2` | 从文件结尾开始 |

```python
>>> f = open('/tmp/foo.txt', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)          # 移动到第6个字节
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)      # 移动到倒数第3个字节
13
>>> f.read(1)
b'd'
```

### 4.8 f.close()

关闭文件并释放系统资源。关闭后再次调用该文件会抛出异常。

### 4.9 with 关键字（最佳实践）

使用 `with` 关键字可以自动关闭文件，比 `try...finally` 更简洁：

```python
with open('/tmp/foo.txt', 'r') as f:
    read_data = f.read()
# 文件已自动关闭
print(f.closed)   # True
```


## 五、pickle 模块（序列化）

`pickle` 模块实现了基本的数据**序列化**和**反序列化**，可以将程序运行中的对象保存到文件，永久存储。

### 5.1 基本接口

| 函数 | 作用 |
|------|------|
| `pickle.dump(obj, file, protocol)` | 将对象序列化并写入文件 |
| `pickle.load(file)` | 从文件读取并反序列化对象 |

### 5.2 示例：保存对象

```python
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j], 'b': ('string', 'Unicode string'), 'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')
pickle.dump(data1, output)
pickle.dump(selfref_list, output, -1)   # -1 表示使用最高协议
output.close()
```

### 5.3 示例：读取对象

```python
import pprint, pickle

pkl_file = open('data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
```


## 六、重点总结

| 知识点 | 要点 |
|--------|------|
| **str() vs repr()** | `str()` 用户友好，`repr()` 解释器友好，会转义特殊字符 |
| **str.format()** | 推荐使用的格式化方法，支持位置、关键字、格式说明符 |
| **旧式 % 格式化** | 逐渐被淘汰，建议使用 `str.format()` |
| **input()** | 从键盘读取一行输入 |
| **open()** | 打开文件，返回文件对象；mode 参数控制读写模式 |
| **f.read()** | 读取整个文件或指定大小 |
| **f.readline()** | 读取一行 |
| **f.readlines()** | 读取所有行，返回列表 |
| **f.write()** | 写入字符串 |
| **f.tell()** | 获取文件指针位置 |
| **f.seek()** | 移动文件指针 |
| **with 语句** | 自动管理文件资源，推荐使用 |
| **pickle** | 对象序列化/反序列化，永久存储 |

---


# 📝 综合练习题

## 任务：日记本程序

编写一个名为 `diary.py` 的程序，综合运用输入输出的各种知识完成以下功能。

> 本练习覆盖：`input()` 读取键盘输入、文件读写（`r`/`w`/`a` 模式）、`readlines()`、`write()`、`with` 语句、`str.format()` 格式化、`repr()` 的使用


### 场景描述

你需要开发一个**简单的日记本程序**，用户可以：
1. 查看所有历史日记
2. 写入新日记（自动添加时间戳）
3. 将日记数据导出为格式化报告


### 具体要求

**1. 日记文件存储格式**

- 日记保存在 `diary.txt` 文件中
- 每条日记的格式为：`[2024-01-15 14:30:00] 今天学习了 Python 输入输出`
- 每条日记占一行

**2. 查看所有日记（readlines）**

编写函数 `view_diary()`：
- 使用 `with open()` 以只读模式打开 `diary.txt`
- 使用 `readlines()` 读取所有行
- 如果文件不存在或为空，打印 `"暂无日记记录"`
- 否则逐条打印日记（带序号）

**3. 写入新日记（write + 时间戳）**

编写函数 `write_diary()`：
- 使用 `input()` 提示用户输入日记内容
- 使用 `datetime` 模块获取当前时间，格式化为 `"%Y-%m-%d %H:%M:%S"`
- 使用 `with open()` 以**追加模式**打开 `diary.txt`
- 将 `"[时间戳] 日记内容\n"` 写入文件
- 打印 `"日记已保存"`

**4. 导出报告（format 格式化）**

编写函数 `export_report()`：
- 读取所有日记，统计总条数
- 使用 `str.format()` 生成如下格式的报告并写入 `report.txt`：

```
========================================
            日记统计报告
========================================
总日记数：5 条
第一条：[2024-01-15 14:30:00] 今天学习了 Python
最后一条：[2024-01-16 20:15:00] 准备睡觉
========================================
```

> 提示：读取所有行后，第一条是 `lines[0]`，最后一条是 `lines[-1]`

**5. 主菜单（循环 + 输入）**

使用 `while True` 循环显示菜单：
```
===== 我的日记本 =====
1. 查看所有日记
2. 写新日记
3. 导出报告
4. 退出
请选择（1-4）：
```

根据用户输入调用对应函数，输入 `4` 时使用 `break` 退出。


### 代码框架（填空版）

```python
import datetime

DIARY_FILE = "diary.txt"
REPORT_FILE = "report.txt"

def view_diary():
    """查看所有日记"""
    try:
        with open(DIARY_FILE, "______") as f:  # 填空：只读模式
            lines = f.______()  # 填空：读取所有行
        if not lines:
            print("暂无日记记录")
            return
        print("\n===== 我的日记 =====")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("暂无日记记录")

def write_diary():
    """写入新日记"""
    content = input("请输入日记内容：")
    if not content.strip():
        print("内容不能为空")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIARY_FILE, "______") as f:  # 填空：追加模式
        f.write(______)  # 填空：写入 "[时间戳] 内容\n"
    print("✓ 日记已保存")

def export_report():
    """导出统计报告"""
    try:
        with open(DIARY_FILE, "r") as f:
            lines = f.readlines()
        if not lines:
            print("暂无日记，无法导出报告")
            return
        count = len(lines)
        first = lines[0].strip()
        last = lines[-1].strip()
        report = """{line}
{title}
{line}
总日记数：{count} 条
第一条：{first}
最后一条：{last}
{line}""".______(  # 填空：使用 format()
            line="=" * 40,
            title="日记统计报告".center(38),
            count=count,
            first=first,
            last=last
        )
        with open(REPORT_FILE, "w") as f:
            f.write(report)
        print(f"✓ 报告已导出到 {REPORT_FILE}")
    except FileNotFoundError:
        print("暂无日记，无法导出报告")

def main():
    """主程序"""
    while True:
        print("\n===== 我的日记本 =====")
        print("1. 查看所有日记")
        print("2. 写新日记")
        print("3. 导出报告")
        print("4. 退出")
        choice = input("请选择（1-4）：")
        if choice == "1":
            view_diary()
        elif choice == "2":
            write_diary()
        elif choice == "3":
            export_report()
        elif choice == "4":
            print("再见！")
            ______  # 填空：退出循环
        else:
            print("无效选择，请重新输入")

if __name__ == "______":  # 填空：程序入口判断
    main()
```


### 运行效果示例

```
===== 我的日记本 =====
1. 查看所有日记
2. 写新日记
3. 导出报告
4. 退出
请选择（1-4）：2
请输入日记内容：今天学习了 Python 输入输出
✓ 日记已保存

===== 我的日记本 =====
请选择（1-4）：1

===== 我的日记 ===
1. [2024-01-15 14:30:00] 今天学习了 Python 输入输出

===== 我的日记本 =====
请选择（1-4）：3
✓ 报告已导出到 report.txt

===== 我的日记本 =====
请选择（1-4）：4
再见！
```

**导出的 report.txt 内容：**
```
========================================
          日记统计报告
========================================
总日记数：1 条
第一条：[2024-01-15 14:30:00] 今天学习了 Python 输入输出
最后一条：[2024-01-15 14:30:00] 今天学习了 Python 输入输出
========================================
```


### 自测检查清单

- [ ] 是否使用 `input()` 读取用户输入？
- [ ] 是否使用 `with open()` 管理文件资源？
- [ ] 是否使用了 `r`、`w`、`a` 三种不同的文件打开模式？
- [ ] 是否使用 `readlines()` 读取所有行？
- [ ] 是否使用 `write()` 写入文件？
- [ ] 是否使用 `str.format()` 格式化报告？
- [ ] 是否使用 `if __name__ == "__main__":` 作为程序入口？
- [ ] 代码是否无语法错误，能正确运行？
