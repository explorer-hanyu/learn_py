# Python3 __name__ 与 __main__ 笔记

## 一、概述

在 Python 中，`__name__` 和 `__main__` 是两个与**模块和脚本执行方式**相关的特殊变量。

它们通常用于控制代码的执行方式，尤其是在模块**既可以作为独立脚本运行，也可以被其他模块导入**时。

> **一句话理解**：`if __name__ == "__main__":` 就像在问："这个文件是被直接运行，还是被别人导入使用的？"——如果是直接运行，就执行下面的代码；如果是被导入，就跳过。


## 二、__name__ 变量

`__name__` 是一个**内置变量**，用于表示当前模块的名称。

### __name__ 的值取决于模块的使用方式：

| 使用方式 | `__name__` 的值 |
|----------|-----------------|
| 模块作为**主程序直接运行** | `"__main__"` |
| 模块被**其他模块导入** | 模块的文件名（不含 `.py` 后缀） |

### 示例

假设有一个 `module.py` 文件：

```python
print(f"模块的 __name__ 值: {__name__}")
```

- **直接运行** `python module.py` → 输出：`模块的 __name__ 值: __main__`
- **被导入** `import module` → 输出：`模块的 __name__ 值: module`


## 三、__main__ 的含义

`__main__` 是一个**特殊的字符串**，用于表示当前模块是作为**主程序**运行的。

当 Python 解释器执行一个 `.py` 文件时，该文件的 `__name__` 变量会被自动设置为 `"__main__"`。

> **注意**：`__main__` 是 Python 解释器自动赋予的标识，**不是**由程序员手动设置的。


## 四、if \_\_name\_\_ == "\_\_main\_\_": 的典型用法

### 4.1 基本语法

在模块的末尾（或合适位置）添加以下代码块：

```python
if __name__ == "__main__":
    # 这里的代码只有在模块作为主程序运行时才会执行
    main()
```

### 4.2 完整示例

假设有一个名为 `example.py` 的模块：

```python
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")
```

**场景一：直接运行 `example.py`**

```bash
$ python example.py
该脚本正在直接运行。
来自 example 模块的问候！
```

此时 `__name__` 的值是 `"__main__"`，`if` 块中的代码被执行。

**场景二：在另一个脚本中导入 `example.py`**

```python
# another_script.py
import example
example.greet()
```

```bash
$ python another_script.py
该脚本作为模块被导入。
来自 example 模块的问候！
```

此时 `__name__` 的值是 `"example"`（模块名），`if` 块中的代码**不会**被执行。


## 五、为什么要使用这个模式？

### 核心目的

**让一个 `.py` 文件既能被导入使用，又能作为独立脚本运行**

### 具体好处

| 好处 | 说明 |
|------|------|
| **模块测试** | 可以在模块中编写测试代码，直接运行模块进行测试，而导入时不会执行测试代码 |
| **代码复用** | 模块中的函数和类可以被其他程序导入使用 |
| **清晰入口** | 明确标识程序的入口点，提高代码可读性 |
| **避免副作用** | 防止导入模块时意外执行不应该执行的代码 |


## 六、最佳实践

| 实践 | 说明 |
|------|------|
| **将主逻辑封装在 `main()` 函数中** | 不要在 `if` 块中直接写大量代码，而是调用 `main()` 函数 |
| **保持 `if` 块简洁** | `if __name__ == "__main__":` 块中只放少量启动代码 |
| **每个模块都可选添加** | 并非每个模块都必须有，但建议为可独立运行的模块添加 |


## 七、常见误区

| 误区 | 正确理解 |
|------|----------|
| `if __name__ == "__main__":` 是程序的"入口" | 它**不是**指定程序入口，而是判断当前文件是否被**直接运行** |
| `__main__` 是固定不变的 | `__main__` 是字符串，但 `__name__` 的值会根据执行方式变化 |
| 导入模块时 `__name__` 是 `"__main__"` | 导入时 `__name__` 是**模块名**，不是 `"__main__"` |


## 八、重点总结

| 知识点 | 要点 |
|--------|------|
| **`__name__`** | 内置变量，表示当前模块的名称 |
| **直接运行时** | `__name__ = "__main__"` |
| **被导入时** | `__name__ = 模块文件名` |
| **`if __name__ == "__main__":`** | 条件判断，仅当模块被直接运行时执行代码块 |
| **核心价值** | 让模块既可被导入，又可独立运行 |
| **最佳实践** | 将主逻辑放在 `main()` 函数中，`if` 块中只调用它 |

---


# 📝 综合练习题

## 任务：双模式工具包


### 场景描述

你需要开发一个**字符串处理工具模块**，包含几个常用的字符串操作函数。同时，这个模块要能够在被直接运行时执行自测，展示所有功能。


### 具体要求

**1. 定义工具函数**

在 `string_utils.py` 中定义以下三个函数：

| 函数 | 参数 | 返回值 | 功能 |
|------|------|--------|------|
| `count_vowels(s)` | 字符串 `s` | 整数 | 统计字符串中元音字母（a, e, i, o, u，不区分大小写）的个数 |
| `reverse_words(s)` | 字符串 `s` | 字符串 | 将字符串中的单词顺序反转（单词间用空格分隔） |
| `is_palindrome(s)` | 字符串 `s` | 布尔值 | 判断字符串是否为回文（忽略大小写和空格） |

**2. 添加自测代码**

在模块末尾使用 `if __name__ == "__main__":` 添加测试代码：

- 分别调用三个函数，使用至少两个不同的测试用例
- 以清晰的格式打印测试结果
- 直接运行 `python string_utils.py` 时，应输出完整的测试报告

**3. 验证导入行为**

- 在另一个 Python 文件（如 `test_import.py`）中导入 `string_utils` 模块
- 调用其中的函数，验证功能正常
- 确认导入时**不会**执行自测代码中的 `print` 输出


### 代码框架（填空版）

```python
# ========== string_utils.py ==========
"""字符串处理工具模块"""

def count_vowels(s):
    """统计字符串中元音字母的个数（不区分大小写）"""
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            ______  # 填空：累加计数
    return count

def reverse_words(s):
    """将字符串中的单词顺序反转"""
    words = s.______()  # 填空：按空格分割
    reversed_words = words[______]  # 填空：使用切片反转列表
    return ' '.join(reversed_words)

def is_palindrome(s):
    """判断字符串是否为回文（忽略大小写和空格）"""
    # 去除空格并转为小写
    cleaned = ''.join(s.split()).lower()
    # 判断 cleaned 是否等于其反转
    return cleaned == cleaned[______]  # 填空：使用切片反转

# ========== 自测代码 ==========
if ______ == '______':  # 填空：__name__ 判断
    print("=" * 40)
    print("字符串工具模块自测")
    print("=" * 40)

    # 测试 count_vowels
    test1 = "Hello World"
    print(f"count_vowels('{test1}') = {count_vowels(test1)}")  # 应为 3

    # 测试 reverse_words
    test2 = "Hello World Python"
    print(f"reverse_words('{test2}') = '{reverse_words(test2)}'")  # 应为 "Python World Hello"

    # 测试 is_palindrome
    test3 = "A man a plan a canal Panama"
    print(f"is_palindrome('{test3}') = {is_palindrome(test3)}")  # 应为 True

    test4 = "Hello"
    print(f"is_palindrome('{test4}') = {is_palindrome(test4)}")  # 应为 False

    print("=" * 40)
    print("自测完成")
```

```python
# ========== test_import.py（验证导入行为）==========
import string_utils

print("导入 string_utils 模块成功！")
print(f"count_vowels('Apple'): {string_utils.count_vowels('Apple')}")
print(f"reverse_words('one two three'): '{string_utils.reverse_words('one two three')}'")
print(f"is_palindrome('racecar'): {string_utils.is_palindrome('racecar')}")
```


### 预期输出

**直接运行 `string_utils.py`：**

```
========================================
字符串工具模块自测
========================================
count_vowels('Hello World') = 3
reverse_words('Hello World Python') = 'Python World Hello'
is_palindrome('A man a plan a canal Panama') = True
is_palindrome('Hello') = False
========================================
自测完成
```

**运行 `test_import.py`：**

```
导入 string_utils 模块成功！
count_vowels('Apple'): 2
reverse_words('one two three'): 'three two one'
is_palindrome('racecar'): True
```

> **关键点**：注意对比两种运行方式的输出——直接运行 `string_utils.py` 时，自测代码被执行；而通过 `test_import.py` 导入时，自测代码**不会**被执行。


### 自测检查清单

- [ ] 是否定义了三个工具函数（`count_vowels`、`reverse_words`、`is_palindrome`）？
- [ ] 是否使用了 `if __name__ == "__main__":` 包裹自测代码？
- [ ] 直接运行 `string_utils.py` 时，是否输出了自测结果？
- [ ] 在另一个文件中导入 `string_utils` 时，自测代码是否**没有**被执行？
- [ ] 导入后是否能正常调用模块中的函数？
- [ ] 代码是否无语法错误，能正确运行？
