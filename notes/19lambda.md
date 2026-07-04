# Python3 lambda（匿名函数）笔记

## 一、什么是 lambda 函数

lambda 函数是 Python 中的一种**小型、匿名的内联函数**。

| 特点 | 说明 |
|------|------|
| **匿名** | 没有函数名称，只能通过赋值给变量或作为参数传递来使用 |
| **单行** | 通常只包含一行代码，适用于简单的函数 |
| **单表达式** | 只能有一个表达式，不能包含多个语句 |
| **自动返回** | 表达式的结果自动作为返回值，不需要 `return` 语句 |

> **核心理解**：lambda 是一个**表达式**而非语句，可以像使用其他表达式一样在任何地方使用 lambda。


## 二、基本语法

```python
lambda arguments: expression
```

| 部分 | 说明 |
|------|------|
| `lambda` | Python 关键字，用于定义 lambda 函数 |
| `arguments` | 参数列表，可以包含零个或多个参数，用逗号隔开 |
| `expression` | 一个表达式，计算并返回函数结果 |


## 三、基础用法示例

### 3.1 无参数 lambda

```python
f = lambda: "Hello, world!"
print(f())   # 输出: Hello, world!
```

### 3.2 单参数 lambda

```python
x = lambda a: a + 10
print(x(5))   # 输出: 15
```

### 3.3 多参数 lambda

```python
# 两个参数相乘
x = lambda a, b: a * b
print(x(5, 6))   # 输出: 30

# 三个参数相加
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))   # 输出: 13
```


## 四、lambda 与内置函数配合使用

lambda 函数最经典的用法是作为参数传递给其他函数。

### 4.1 map() + lambda —— 批量转换数据

`map()` 将 lambda 函数应用于序列的每个元素，返回结果列表。

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)   # 输出: [1, 4, 9, 16, 25]
```

> **map 与 filter 的区别**：`map()` 对每个元素都应用函数并返回结果；`filter()` 只返回满足条件的元素。

### 4.2 filter() + lambda —— 条件筛选

`filter()` 使用 lambda 函数筛选出满足条件的元素。

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)   # 输出: [2, 4, 6, 8]
```

### 4.3 reduce() + lambda —— 累积计算

`reduce()` 来自 `functools` 模块，将 lambda 函数累积应用于序列元素。

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)   # 输出: 120
```


## 五、lambda 的其他应用场景

### 5.1 列表排序（自定义排序规则）

```python
# 按元组第二个元素排序
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)   # 输出: [(1, 'one'), (3, 'three'), (2, 'two')]
```

### 5.2 跳转表（Jump Table）

lambda 可用于创建行为列表或字典：

```python
# 用字典存储不同的操作
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
}
print(operations['add'](5, 3))      # 8
print(operations['multiply'](5, 3)) # 15
```


## 六、lambda vs 普通函数（def）

| 对比项 | lambda | def 函数 |
|--------|--------|----------|
| **名称** | 匿名，无名称 | 有名称 |
| **函数体** | 只能包含**单个表达式** | 可包含多个语句 |
| **返回值** | 自动返回表达式结果 | 需要 `return` 语句 |
| **适用场景** | 简单、一次性的操作 | 复杂、可复用的逻辑 |
| **可读性** | 简洁但过度使用会降低可读性 | 结构清晰，易于理解 |


## 七、注意事项与最佳实践

| 要点 | 说明 |
|------|------|
| **不能包含语句** | lambda 不能包含赋值、循环、条件语句等 |
| **不能包含异常处理** | lambda 内部不能使用 `try...except` |
| **保持简洁** | lambda 适用于简单逻辑，复杂逻辑应使用 `def` |
| **不要过度使用** | 过度使用 lambda 会降低代码可读性 |
| **配合高阶函数** | lambda 最常用于 `map()`、`filter()`、`reduce()`、`sort()` 等 |


## 八、重点总结

| 知识点 | 要点 |
|--------|------|
| **定义** | `lambda 参数: 表达式` |
| **本质** | 匿名、单表达式、自动返回 |
| **与 def 区别** | 无名称、只能单行、无需 return |
| **常见搭档** | `map()`、`filter()`、`reduce()`、`sort(key=...)` |
| **适用场景** | 简单一次性操作、高阶函数参数 |
| **避免场景** | 复杂逻辑、多语句、需要复用的功能 |

---


# 📝 综合练习题

## 任务：电商数据处理工具（lambda 专项练习）

编写一个名为 `lambda_processor.py` 的程序，**仅使用 lambda 表达式**完成以下所有数据处理任务（不允许定义 `def` 函数）。

> 本练习覆盖：lambda 基本用法、多参数 lambda、`map()` + lambda、`filter()` + lambda、`reduce()` + lambda、`sort(key=...)` + lambda


### 场景描述

你有一份电商商品数据，需要利用 lambda 表达式进行各种维度的数据处理和分析。


#### 具体要求

**1. 数据准备**

定义以下商品数据：

```python
products = [
    {"name": "手机", "price": 2999, "stock": 50, "category": "电子"},
    {"name": "耳机", "price": 399, "stock": 200, "category": "电子"},
    {"name": "笔记本", "price": 5999, "stock": 30, "category": "电子"},
    {"name": "T恤", "price": 99, "stock": 500, "category": "服装"},
    {"name": "牛仔裤", "price": 299, "stock": 150, "category": "服装"},
    {"name": "运动鞋", "price": 699, "stock": 80, "category": "服装"},
]
```

**2. 基础 lambda（单参数 + 多参数）**

- 使用 lambda 创建一个**无参数**函数，返回 `"数据处理开始"`
- 使用 lambda 创建一个**单参数**函数，计算商品价格打 8 折后的价格
- 使用 lambda 创建一个**三参数**函数，计算订单总价：`价格 × 数量 × (1 - 折扣)`

**3. map() + lambda（批量转换）**

- 使用 `map()` + lambda 生成所有商品**打折后价格**列表（打 8 折）
- 使用 `map()` + lambda 生成所有商品**名称 + 价格**的字符串列表（格式：`"手机-2999"`）

**4. filter() + lambda（条件筛选）**

- 使用 `filter()` + lambda 筛选出**价格大于 500** 的商品
- 使用 `filter()` + lambda 筛选出**库存小于 100** 的商品

**5. reduce() + lambda（累积计算）**

- 使用 `reduce()` + lambda 计算所有商品的总库存
- 使用 `reduce()` + lambda 计算所有商品的总价值（`价格 × 库存` 之和）

**6. sort() + lambda（自定义排序）**

- 按**价格从高到低**排序商品列表
- 按**库存从低到高**排序商品列表

**7. 综合挑战**

- 使用 `filter()` + `map()` 链式操作：筛选出**价格大于 500** 的商品，然后提取它们的**名称**
- 使用 `reduce()` + lambda 找出**价格最高的商品**（提示：比较两个商品的价格，返回价格更高的那个）


### 代码框架（填空版）

```python
from functools import reduce

# ========== 数据准备 ==========
products = [
    {"name": "手机", "price": 2999, "stock": 50, "category": "电子"},
    {"name": "耳机", "price": 399, "stock": 200, "category": "电子"},
    {"name": "笔记本", "price": 5999, "stock": 30, "category": "电子"},
    {"name": "T恤", "price": 99, "stock": 500, "category": "服装"},
    {"name": "牛仔裤", "price": 299, "stock": 150, "category": "服装"},
    {"name": "运动鞋", "price": 699, "stock": 80, "category": "服装"},
]

# ========== 1. 基础 lambda ==========
print("=== 1. 基础 lambda ===")
# 无参数 lambda
greet = ______               # 填空：返回 "数据处理开始"
print(greet())

# 单参数 lambda（打 8 折）
discount = ______            # 填空：计算价格 * 0.8
print(f"手机打折后: {discount(2999)}")

# 三参数 lambda（计算订单总价：价格 × 数量 × (1 - 折扣)）
calc_total = ______          # 填空：三参数 lambda
print(f"订单总价: {calc_total(2999, 2, 0.1)}")  # 2台手机，9折

# ========== 2. map() + lambda ==========
print("\n=== 2. map() + lambda ===")
# 所有商品打折后价格
discounted_prices = list(map(______, products))  # 填空：提取 price 并打 8 折
print(f"打折后价格: {discounted_prices}")

# 商品名称-价格字符串列表
name_price = list(map(______, products))  # 填空：生成 "名称-价格" 格式
print(f"名称-价格: {name_price}")

# ========== 3. filter() + lambda ==========
print("\n=== 3. filter() + lambda ===")
# 价格大于 500 的商品
expensive = list(filter(______, products))  # 填空：筛选 price > 500
print(f"价格>500: {[p['name'] for p in expensive]}")

# 库存小于 100 的商品
low_stock = list(filter(______, products))  # 填空：筛选 stock < 100
print(f"库存<100: {[p['name'] for p in low_stock]}")

# ========== 4. reduce() + lambda ==========
print("\n=== 4. reduce() + lambda ===")
# 总库存
total_stock = reduce(______, products, 0)  # 填空：累加 stock
print(f"总库存: {total_stock}")

# 总价值（价格 × 库存 之和）
total_value = reduce(______, products, 0)  # 填空：累加 price * stock
print(f"总价值: {total_value}")

# ========== 5. sort() + lambda ==========
print("\n=== 5. sort() + lambda ===")
# 按价格从高到低
products_by_price = sorted(products, key=______, reverse=True)  # 填空：按 price 排序
print(f"价格从高到低: {[p['name'] for p in products_by_price]}")

# 按库存从低到高
products_by_stock = sorted(products, key=______)  # 填空：按 stock 排序
print(f"库存从低到高: {[p['name'] for p in products_by_stock]}")

# ========== 6. 综合挑战 ==========
print("\n=== 6. 综合挑战 ===")
# 价格 > 500 的商品名称（filter + map 链式）
expensive_names = list(map(______, filter(______, products)))  # 填空：提取名称 + 筛选条件
print(f"高价商品名称: {expensive_names}")

# 价格最高的商品（reduce 比较）
most_expensive = reduce(______, products)  # 填空：比较两个商品的价格，返回更高的
print(f"最贵商品: {most_expensive['name']} - {most_expensive['price']}元")
```


### 预期输出示例

```
=== 1. 基础 lambda ===
数据处理开始
手机打折后: 2399.2
订单总价: 5398.2

=== 2. map() + lambda ===
打折后价格: [2399.2, 319.2, 4799.2, 79.2, 239.2, 559.2]
名称-价格: ['手机-2999', '耳机-399', '笔记本-5999', 'T恤-99', '牛仔裤-299', '运动鞋-699']

=== 3. filter() + lambda ===
价格>500: ['手机', '笔记本', '运动鞋']
库存<100: ['手机', '笔记本', '运动鞋']

=== 4. reduce() + lambda ===
总库存: 1010
总价值: 401450

=== 5. sort() + lambda ===
价格从高到低: ['笔记本', '手机', '运动鞋', '耳机', '牛仔裤', 'T恤']
库存从低到高: ['笔记本', '手机', '运动鞋', '牛仔裤', '耳机', 'T恤']

=== 6. 综合挑战 ===
高价商品名称: ['手机', '笔记本', '运动鞋']
最贵商品: 笔记本 - 5999元
```


### 自测检查清单

- [ ] 是否使用了无参数、单参数、多参数的 lambda？
- [ ] 是否使用了 `map()` + lambda 进行批量转换？
- [ ] 是否使用了 `filter()` + lambda 进行条件筛选？
- [ ] 是否使用了 `reduce()` + lambda 进行累积计算？
- [ ] 是否使用了 `sort(key=...)` + lambda 进行自定义排序？
- [ ] 是否实现了 `filter()` 和 `map()` 的链式操作？
- [ ] 代码是否**仅使用 lambda**，没有定义 `def` 函数？
- [ ] 代码是否无语法错误，能正确运行？