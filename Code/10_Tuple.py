#创建元组
book1=("Python编程", "张三", 59.00, 10)
book2=("数据结构", "李四", 45.50, 8)
book3=("算法导论", "王五", 89.00, 5)
books=(book1,book2,book3)
print(books)
print("="*30)

#访问与查询
for i in books:
    print(f"书名：{i[0]}，作者：{i[1]}，价格：{i[2]}，库存：{i[3]}")

print(f"第二本书名字：{books[1][0]}，作者：{books[1][1]}，价格：{books[1][2]}，库存{books[1][3]}")
print(f"最后一本名字：{books[-1][0]}，作者：{books[-1][1]}，价格：{books[-1][2]}，库存{books[-1][3]}")
print("="*30)

#尝试修改
# books[0][2]=69.00
# TypeError: 'tuple' object does not support item assignment

#组合与复制
book4=(("数据库", "赵六", 55.00, 12),)
newbooks = books + book4
print(newbooks)
print(f"{("畅销书",)*3}")
print("="*30)

#元组内置函数
print(f"当前图书数量为{len(newbooks)}本")

titles=tuple()
for i in newbooks:
    titles+=((i[0]),)
print(titles)

prices=tuple()
for i in newbooks:
    prices+=((i[2]),)

for i in newbooks:
    if(i[2]==max(prices)):
        print(f"最贵的书为{i[0]}，价格为{max(prices)}元")

print(f"库存最小的书为{min(newbooks[0][3],newbooks[1][3],newbooks[2][3],newbooks[3][3])}")

newbooklist=['新书A', '新书B']
print(f"列表转元组：{tuple(newbooklist)}")
print("="*30)

#成员检查与迭代
if("算法导论" in titles):
    print("算法导论在书名中")

for i in newbooks:
    print(f"书名：{i[0]}，作者：{i[1]}，价格：{i[2]}，库存：{i[3]}")

print("="*30)

#不可变性验证
print(id(books))
books=tuple(newbooklist)
print(id(books))