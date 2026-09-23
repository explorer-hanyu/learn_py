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
    lambda o: operator.gt(o["price"], 500),  # operator.gt
    orders
))
for o in expensive:
    print(f"  {o['id']} - {o['product']} - {o['price']}元")

# ========== 2. 计算订单总价 ==========
print("\n=== 订单总价 ===")
totals = list(map(
    lambda o: operator.mul(o["price"], o["quantity"]),  # operator.mul
    orders
))
for o, t in zip(orders, totals):
    print(f"  {o['id']}: {o['price']} × {o['quantity']} = {t}")

# ========== 3. 提取字段 ==========
print("\n=== 按商品名排序 ===")
sorted_orders = sorted(orders, key=operator.itemgetter('product'))  # operator.itemgetter
for o in sorted_orders:
    print(f"  {o['product']} - {o['price']}元")

# ========== 4. 提取价格列表 ==========
prices = list(map(operator.itemgetter('price'), orders))  # operator.itemgetter
print(f"\n价格列表: {prices}")

# ========== 5. 身份判断 ==========
print("\n=== 身份判断 ===")
list_a = [1, 2, 3]
list_b = list_a
print(f"list_a is list_b: {operator.is_(list_a, list_b)}")  # operator.is_
print(f"not (list_a is list_b): {operator.not_(operator.is_(list_a, list_b))}")  # operator.not_

# ========== 6. 综合管道 ==========
print("\n=== 综合计算 ===")
total_sum = reduce(operator.add, totals)  # operator.add
print(f"所有订单总价之和: {total_sum}")

quantities = list(map(operator.itemgetter('quantity'), orders))
total_product = reduce(operator.mul, quantities)  # operator.mul
print(f"所有订单数量的乘积: {total_product}")