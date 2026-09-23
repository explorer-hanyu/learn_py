# Python3 operator 模块 笔记
## 一、operator 模块概述

在 Python2.x 版本中，使用 `cmp()` 函数来比较两个列表、数字或字符串等的大小关系。**Python 3.X 的版本中已经没有 `cmp()` 函数**，如果你需要实现比较功能，需要引入 `operator` 模块，它适合任何对象。

`operator` 模块提供了一套与 Python **内置运算符对应的高效率函数**。例如，`operator.add(x, y)` 与表达式 `x + y` 相同。

### 核心价值

| 场景 | 说明 |
|------|------|
| **函数式编程** | 将运算符作为函数参数传递，如 `map(operator.add, list1, list2)` |
| **替代 lambda** | `operator.add` 比 `lambda a, b: a + b` 更简洁高效 |
| **排序键函数** | 使用 `operator.itemgetter()` 作为 `sorted()` 的 `key` 参数 |
| **多维数据操作** | 配合 `map()`、`reduce()` 对多个序列同时运算 |


## 二、比较运算函数

对象比较函数适用于**所有对象**，函数名根据它们对应的比较运算符命名。

| 运算符 | 函数 | 示例 |
|--------|------|------|
| `<` | `operator.lt(a, b)` | `a < b` |
| `<=` | `operator.le(a, b)` | `a <= b` |
| `==` | `operator.eq(a, b)` | `a == b` |
| `!=` | `operator.ne(a, b)` | `a != b` |
| `>=` | `operator.ge(a, b)` | `a >= b` |
| `>` | `operator.gt(a, b)` | `a > b` |

### 实例

```python
import operator

# 数字比较
x = 10
y = 20
print("operator.lt(x,y): ", operator.lt(x, y))  # True
print("operator.gt(y,x): ", operator.gt(y, x))  # True
print("operator.eq(x,x): ", operator.eq(x, x))  # True
print("operator.ne(y,y): ", operator.ne(y, y))  # False
```

### 列表比较

```python
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]

print("operator.eq(a,b): ", operator.eq(a, b))  # False
print("operator.eq(c,b): ", operator.eq(c, b))  # True
```


## 三、算术运算函数

| 运算符 | 函数 | 说明 |
|--------|------|------|
| `+` | `operator.add(a, b)` | 加法 |
| `-` | `operator.sub(a, b)` | 减法 |
| `*` | `operator.mul(a, b)` | 乘法 |
| `/` | `operator.truediv(a, b)` | 除法（浮点） |
| `//` | `operator.floordiv(a, b)` | 整除 |
| `%` | `operator.mod(a, b)` | 取模 |
| `**` | `operator.pow(a, b)` | 幂运算 |
| `-a` | `operator.neg(a)` | 取反（算术） |
| `+a` | `operator.pos(a)` | 正数 |
| `@` | `operator.matmul(a, b)` | 矩阵乘法 |

### 实例

```python
import operator

a = 4
b = 3

print("add() 运算结果 :", operator.add(a, b))   # 7
print("sub() 运算结果 :", operator.sub(a, b))   # 1
print("mul() 运算结果 :", operator.mul(a, b))   # 12
```


## 四、位运算函数

| 运算符 | 函数 | 说明 |
|--------|------|------|
| `&` | `operator.and_(a, b)` | 按位与 |
| `\|` | `operator.or_(a, b)` | 按位或 |
| `^` | `operator.xor(a, b)` | 按位异或 |
| `~` | `operator.invert(a)` | 按位取反 |
| `<<` | `operator.lshift(a, b)` | 左移 |
| `>>` | `operator.rshift(a, b)` | 右移 |


## 五、序列操作函数

| 运算符 | 函数 | 说明 |
|--------|------|------|
| `seq1 + seq2` | `operator.concat(seq1, seq2)` | 序列拼接 |
| `obj in seq` | `operator.contains(seq, obj)` | 包含测试 |
| `obj[k]` | `operator.getitem(obj, k)` | 索引取值 |
| `obj[k] = v` | `operator.setitem(obj, k, v)` | 索引赋值 |
| `del obj[k]` | `operator.delitem(obj, k)` | 索引删除 |
| `seq[i:j]` | `operator.getitem(seq, slice(i, j))` | 切片取值 |
| `seq[i:j] = values` | `operator.setitem(seq, slice(i, j), values)` | 切片赋值 |
| `del seq[i:j]` | `operator.delitem(seq, slice(i, j))` | 切片删除 |
| `s % obj` | `operator.mod(s, obj)` | 字符串格式化 |


## 六、逻辑与身份运算

| 运算符 | 函数 | 说明 |
|--------|------|------|
| `not a` | `operator.not_(a)` | 逻辑取反 |
| `a is b` | `operator.is_(a, b)` | 身份判断 |
| `a is not b` | `operator.is_not(a, b)` | 身份判断（否定） |
| `obj` | `operator.truth(obj)` | 真值测试 |


## 七、函数命名规则

许多函数名与特殊方法名相同，只是**没有双下划线**。为了向后兼容性，也保留了许多包含双下划线的函数。为了表述清楚，**建议使用没有双下划线的函数**。

```python
# 推荐使用
operator.add(a, b)

# 不推荐（但兼容）
operator.__add__(a, b)
```


## 八、重点总结

| 知识点 | 要点 |
|--------|------|
| **模块用途** | 将内置运算符封装为函数，支持函数式编程风格 |
| **比较函数** | `lt`、`le`、`eq`、`ne`、`ge`、`gt` |
| **算术函数** | `add`、`sub`、`mul`、`truediv`、`floordiv`、`mod`、`pow` |
| **位运算函数** | `and_`、`or_`、`xor`、`invert`、`lshift`、`rshift` |
| **序列函数** | `concat`、`contains`、`getitem`、`setitem`、`delitem` |
| **身份/逻辑** | `is_`、`is_not`、`not_`、`truth` |
| **命名规范** | 优先使用无下划线版本，双下划线版本仅用于兼容 |


# 📝 综合练习题

## 任务：函数式数据处理管道

编写一个名为 `operator_pipeline.py` 的程序，**在一个综合场景中**运用 `operator` 模块的各类函数，构建一个函数式的数据处理管道。

> 本练习覆盖：比较函数、算术函数、序列操作函数、身份/逻辑函数、`operator` 与 `map`/`sorted`/`reduce` 的配合


### 场景描述

你有一个电商订单系统，需要对订单数据进行**排序、过滤、计算、合并**等操作，所有操作使用 `operator` 模块的函数完成，避免使用 `lambda`。


### 具体要求

**1. 订单数据准备**

```python
orders = [
    {"id": "A001", "product": "手机", "price": 2999, "quantity": 2},
    {"id": "A002", "product": "耳机", "price": 399, "quantity": 5},
    {"id": "A003", "product": "充电器", "price": 89, "quantity": 10},
    {"id": "A004", "product": "手机", "price": 2999, "quantity": 1},
    {"id": "A005", "product": "手表", "price": 1299, "quantity": 3},
]
```

**2. 比较运算：筛选高价订单（`filter` + `operator.gt`）**

- 使用 `filter()` 配合 `operator.gt` 筛选出 `price > 500` 的订单
- 打印筛选结果

**3. 算术运算：计算订单总价（`map` + `operator.mul`）**

- 使用 `map()` 配合 `operator.mul` 计算每个订单的 `price * quantity`
- 打印所有订单的总价列表

**4. 序列操作：提取字段（`operator.itemgetter`）**

- 使用 `operator.itemgetter('product')` 作为 `sorted()` 的 `key` 参数，按商品名排序
- 使用 `operator.itemgetter('price')` 提取所有订单的价格列表

**5. 身份与逻辑运算（`operator.is_` + `operator.not_`）**

- 创建两个列表 `list_a = [1, 2, 3]` 和 `list_b = list_a`
- 使用 `operator.is_(list_a, list_b)` 判断是否同一对象
- 使用 `operator.not_(operator.is_(list_a, list_b))` 进行逻辑取反

**6. 综合管道（`reduce` + `operator`）**

- 使用 `reduce()` 配合 `operator.add` 计算所有订单的总价之和
- 使用 `reduce()` 配合 `operator.mul` 计算所有订单数量的乘积（模拟）

**7. 输出要求**

- 所有操作使用 `operator` 模块函数完成，**禁止使用 `lambda`**
- 打印格式清晰


### 代码框架（填空版）

```python
import operator
from functools import reduce

# ========== 订单数据 ==========
orders = [
    {"id": "A001", "product": "手机", "price": 2999, "quantity": 2},
    {"id": "A002", "product": "耳机", "price": 399, "quantity": 5},
    {"id": "A003", "product": "充电器", "price": 89, "quantity": 10},
    {"id": "A004", "product": "手机", "price": 2999, "quantity": 1},
    {"id": "A005", "product": "手表", "price": 1299, "quantity": 3},
]

# ========== 1. 筛选高价订单 ==========
print("=== 高价订单（price > 500）===")
expensive = list(filter(
    lambda o: ______(o["price"], 500),  # 填空：operator.gt
    orders
))
for o in expensive:
    print(f"  {o['id']} - {o['product']} - {o['price']}元")

# ========== 2. 计算订单总价 ==========
print("\n=== 订单总价 ===")
totals = list(map(
    lambda o: ______(o["price"], o["quantity"]),  # 填空：operator.mul
    orders
))
for o, t in zip(orders, totals):
    print(f"  {o['id']}: {o['price']} × {o['quantity']} = {t}")

# ========== 3. 提取字段 ==========
print("\n=== 按商品名排序 ===")
sorted_orders = sorted(orders, key=______('product'))  # 填空：operator.itemgetter
for o in sorted_orders:
    print(f"  {o['product']} - {o['price']}元")

# ========== 4. 提取价格列表 ==========
prices = list(map(______('price'), orders))  # 填空：operator.itemgetter
print(f"\n价格列表: {prices}")

# ========== 5. 身份判断 ==========
print("\n=== 身份判断 ===")
list_a = [1, 2, 3]
list_b = list_a
print(f"list_a is list_b: {______(list_a, list_b)}")  # 填空：operator.is_
print(f"not (list_a is list_b): {______(operator.is_(list_a, list_b))}")  # 填空：operator.not_

# ========== 6. 综合管道 ==========
print("\n=== 综合计算 ===")
total_sum = reduce(______, totals)  # 填空：operator.add
print(f"所有订单总价之和: {total_sum}")

quantities = list(map(operator.itemgetter('quantity'), orders))
total_product = reduce(______, quantities)  # 填空：operator.mul
print(f"所有订单数量的乘积: {total_product}")
```


### 预期输出示例

```
=== 高价订单（price > 500）===
  A001 - 手机 - 2999元
  A004 - 手机 - 2999元
  A005 - 手表 - 1299元

=== 订单总价 ===
  A001: 2999 × 2 = 5998
  A002: 399 × 5 = 1995
  A003: 89 × 10 = 890
  A004: 2999 × 1 = 2999
  A005: 1299 × 3 = 3897

=== 按商品名排序 ===
  充电器 - 89元
  手机 - 2999元
  手机 - 2999元
  手表 - 1299元
  耳机 - 399元

价格列表: [2999, 399, 89, 2999, 1299]

=== 身份判断 ===
list_a is list_b: True
not (list_a is list_b): False

=== 综合计算 ===
所有订单总价之和: 15779
所有订单数量的乘积: 300
```


### 自测检查清单

- [ ] 是否使用了 `operator.gt()` 进行大小比较？
- [ ] 是否使用了 `operator.mul()` 进行乘法运算？
- [ ] 是否使用了 `operator.itemgetter()` 提取字典字段？
- [ ] 是否使用了 `operator.is_()` 和 `operator.not_()` 进行身份与逻辑判断？
- [ ] 是否使用了 `reduce()` 配合 `operator.add` 和 `operator.mul` 进行累积计算？
- [ ] 所有操作是否**没有使用 `lambda`**，而是使用 `operator` 模块函数？
- [ ] 代码是否无语法错误，能正确运行？