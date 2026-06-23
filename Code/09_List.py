#创建列表
students=list()
scores=list()

students.append("张三")
scores.append(85)
students.append("李四")
scores.append(92)
students.append("王五")
scores.append(78)
students.append("赵六")
scores.append(88)
students.append("孙七")
scores.append(95)

#访问与查询
for i in range(5):
    print(f"姓名：{students[i]}, 成绩：{scores[i]}")

print(f"第三位学生是：{students[2]}, 成绩为：{scores[2]}")

print(f"最后一位学生是：{students[-1]}, 成绩为：{scores[-1]}")

print("第2到4位学生是" , students[1:4])

#修改与更新
scores[1]=96
students.append("周八")
scores.append(82)
students.insert(2,"吴九")
scores.insert(2,90)

print("更新后成绩单为：")
for i in range(students.__len__()):
    print(f"姓名：{students[i]}, 成绩：{scores[i]}")

#删除操作
del students[1]
del scores[1]
students.pop()
scores.pop()
scores.pop(students.index("王五"))
students.remove("王五")

print("删除后成绩单为：")
for i in range(students.__len__()):
    print(f"姓名：{students[i]}, 成绩：{scores[i]}")

#列表方法与函数
print(f"当前列表共有{students.__len__()}人")
print(f"目前列表中最高分为{max(scores)}，最低分为{min(scores)}")
print(f"目前列表总分为{sum(scores)}，平均分为{sum(scores)/students.__len__()}")
print(f"赵六在列表中索引为{students.index("赵六")}")
print(f"成绩为90分的同学有{scores.count(90)}个")

#扩展与反转
new_students = ['钱十', '陈十一']
new_scores = [88, 76]
students.extend(new_students)
scores.extend(new_scores)
print("扩展后成绩单为：")
for i in range(students.__len__()):
    print(f"姓名：{students[i]}, 成绩：{scores[i]}")

students_bp=students[:]
students_bp.reverse()
print(f"反转后学生列表为{students_bp}")
print(students)

scores_bp=scores[:]
scores_bp.sort()
print(f"排序后成绩列表为{scores_bp}")

#综合输出
print(f"姓名和成绩列表+处理：{students+scores}")
print(f"姓名列表*2：{students*2}")
if "张三" in students:
    print("张三在列表中")
else:
    print("张三不在列表中")

print(f"('A', 'B', 'C')元组转列表：{list(('A', 'B', 'C'))}")