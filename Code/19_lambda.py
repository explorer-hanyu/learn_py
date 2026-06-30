from functools import reduce
#数据准备
products = [
    {"name": "手机", "price": 2999, "stock": 50, "category": "电子"},
    {"name": "耳机", "price": 399, "stock": 200, "category": "电子"},
    {"name": "笔记本", "price": 5999, "stock": 30, "category": "电子"},
    {"name": "T恤", "price": 99, "stock": 500, "category": "服装"},
    {"name": "牛仔裤", "price": 299, "stock": 150, "category": "服装"},
    {"name": "运动鞋", "price": 699, "stock": 80, "category": "服装"},
]

# 基础lambda
start = lambda :"数据处理开始"
print(start())
  
offset8 = lambda x:x*0.8
print(f"手机打折后: {offset8(2999)}")

totalscore = lambda price, num, offset:price*num*(1-offset)
print(f"订单总价: {totalscore(2999, 2, 0.1)}") 

# map() + lambda
offsetprice=list(map(lambda x:round(x["price"]*0.8, 2), products))
print(f"打折后价格: {offsetprice}")

prouctprice=list(map(lambda x:x["name"]+"-"+str(x["price"]), products))
print(f"商品-价格列表：{prouctprice}")

# filter() + lambda
highprice = list(filter(lambda x:x["price"]>500 , products))
print(f"价格大于500的高价商品：{[p["name"] for p in highprice]}")

lowprice = list(filter(lambda x:x["price"]<100 , products))
print(f"价格小于100的低价商品：{[p["name"] for p in lowprice]}")

# reduce() + lambda
totalstock = reduce(lambda acc,x : acc+x["stock"], products, 0)
print(f"各商品总库存为：{totalstock}")

# sort() + lambda
products.sort(key= lambda x:x["price"], reverse=True)
print(f"价格从高到低: {[p['name'] for p in products]}")

backproducts = sorted(products,key= lambda x:x["price"], reverse=False)
print(f"库存从低到高: {[p['name'] for p in backproducts]}")

# 综合练习
highpricelist=list(map(lambda x:x["name"], filter(lambda y: y["price"]>500, products)))
print(f"价格大于500的商品：{highpricelist}")

most_expensive = reduce(lambda y,x:y if y["price"] > x["price"] else x, products) 
print(f"最贵商品: {most_expensive['name']} - {most_expensive['price']}元")