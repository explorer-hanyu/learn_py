#创建集合
user1_movies={"盗梦空间", "星际穿越", "泰坦尼克号", "阿凡达"}
user2_movies=set(["星际穿越", "阿凡达", "复仇者联盟", "盗梦空间"])
common_movies=set()

#集合基本操作
user1_movies.add("流浪地球")
user2_movies.update(["哪吒","姜子牙"])
print(f"user1_movies共有{len(user1_movies)}个参数，user2_movies共有{len(user2_movies)}个参数")
if("泰坦尼克号" in user1_movies):
    print("泰坦尼克号在user1_movies中")
else:
    print("泰坦尼克号不在user1_movies中")

print("="*30)

#集合运算
print(f"两用户都看过{user1_movies & user2_movies}")
print(f"两用户一共看过{user1_movies | user2_movies}")
print(f"user1_movies看过但user2_movies没看过{user1_movies - user2_movies}")
print(f"只有一个用户看过{user1_movies ^ user2_movies}")

print("="*30)

#添加或移除元素
user1_movies.remove("泰坦尼克号")
print("已从user1_movies中移除\"泰坦尼克号\"")
user2_movies.discard("哈利波特")
print("已从user2_movies中移除\"哈利波特\"")
print(f"随机从user1_movies移除{user1_movies.pop()}")

print("="*30)

#集合推导式
movies = ["盗梦空间", "星际穿越", "盗梦空间", "阿凡达", "星际穿越", "流浪地球"]
newset_movies = {X for X in movies if len(X)>3}
print(f"tongg通过推导式创建的集合为{newset_movies}")

print("="*30)

#电影推荐
pushmvies=user1_movies-user2_movies
if(len(pushmvies)>0):
    print(f"推荐你看：{pushmvies}")
else:
    print("没有电影推荐")

print("="*30)

#内置方法练习
user1_copy=user1_movies.copy()
user1_copy.add("战狼2")
print(f"user1_movies为{user1_movies}")
print(f"user1_copy为{user1_copy}")

user1_copy.clear()
print(f"user1_copy清空后：{user1_copy}")