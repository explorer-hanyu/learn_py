#数据准备
orders = [
    {"id": 1, "product": "手机", "price": 2999, "quantity": 2, "city": "北京"},
    {"id": 2, "product": "耳机", "price": 399, "quantity": 5, "city": "上海"},
    {"id": 3, "product": "充电器", "price": 89, "quantity": 10, "city": "北京"},
    {"id": 4, "product": "手机", "price": 2999, "quantity": 1, "city": "深圳"},
    {"id": 5, "product": "手表", "price": 1299, "quantity": 3, "city": "上海"},
    {"id": 6, "product": "耳机", "price": 399, "quantity": 2, "city": "北京"},
]

#列表推导式
total_amounts=[deal["price"]*deal["quantity"] for deal in orders]
print(f"总金额列表：{total_amounts}")

beijing_products=[deal["product"] for deal in orders if deal["city"]=="北京"]
print(f"北京地区的产品列表：{beijing_products}")

high_value_orders=[deal for deal in orders if deal["price"]*deal["quantity"]>2000]
print(f"金额大于2000的订单列表为：{high_value_orders}")

#字典推导式
product_list=list({order["product"] for order in orders})
product_total={name:sum(order["price"]*order["quantity"] for order in orders if order["product"]==name ) for name in product_list}
print(product_total)

city_list=list({order["city"] for order in orders})
city_order_count={name:sum(1 for order in orders if order["city"]==name) for name in city_list}
print(city_order_count)            

#集合推导式
unique_products={order["product"] for order in orders}
print(f"共有以下商品：{unique_products}")

#元组推导式
totalsale = sum(order["price"]*order["quantity"] for order in orders)
print(f"总销售额为：{totalsale}")

highprice=(order["product"] for order in orders if order["price"]>500)
expensive_products=tuple(highprice)
print(f"单价大于500的商品有：{expensive_products}")
