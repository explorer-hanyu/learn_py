#创建字典
students = {
            "S001":{"name":"张三","score":85},
            "S002":{"name":"李四","score":92},
            "S003":{"name":"王五","score":78}
            }

print("="*30)

#访问与查询
print(f"S002姓名为{students["S002"]["name"]}，成绩为{students["S002"]["score"]}")
print(f"S005学生信息如下：{students.get("S005","学生不存在")}")
print(f"学号列表：{students.keys()}")
print("姓名列表：")
for xh in students.values():
    print(f"{xh["name"]}")

print("="*30)

#修改与添加
students["S002"]["score"]=96
students["S004"]={"name":"赵六", "score":88}
students["S001"]["grade"]="A"

for xh,mes in students.items():
    print(f"学生{xh}:{mes}")

#删除操作
print(f"删除学生S003：{students.pop("S003","没有S003")}")
print(f"最后一对键值对：{students.popitem()}")
print(f"清空字典：{students.clear()}")

students = {
            "S001":{"name":"张三","score":85},
            "S002":{"name":"李四","score":92},
            "S003":{"name":"王五","score":78}
            }

print("="*30)

#字典内置方法
print(f"当前人数为：{len(students)}")
if("S001" in students):
    print("S001在字典中")
else:
    print("S001不在字典中")

students_copy=students.copy()
students_copy["S002"]={"name":"李四","score":100}
print(f"原成绩为{students['S002']["score"]},改之后为{students_copy['S002']["score"]}")

#遍历与统计
for xh,mes in students.items():
    print(f"学号：{xh}，姓名：{mes["name"]}，成绩：{mes["score"]}")

total=0
for value in students.values():
    total+=value["score"]
print(f"目前学生的平均分为：{total/len(students)}")

scorelist=list()
studentslist=list()
for value in students.values():
    scorelist.append(value["score"])
    studentslist.append(value["name"])

first=max(scorelist)
last=min(scorelist)

firstIndex=scorelist.index(first)
lastIndex=scorelist.index(last)

print(f"最高分学生为{studentslist[firstIndex]}：{first}分，最低分学生为{studentslist[lastIndex]}：{last}分")

#统计函数
def count_score_levels(students_dict):
    scoreInfo={"优秀":0,"良好":0,"及格":0,"不及格":0}
    for mes in students_dict.values():
        if(mes["score"]>=90):
            scoreInfo["优秀"] += 1
        if(mes["score"]<90 and mes["score"]>=80):
            scoreInfo["良好"] += 1
        if(mes["score"]<80 and mes["score"]>=60):
            scoreInfo["及格"] += 1
        if(mes["score"]<60):
            scoreInfo["不及格"] += 1
    
    print(f"优秀共{scoreInfo.get("优秀",0)}\n良好共{scoreInfo.get("良好",0)}人\n及格共{scoreInfo.get("及格",0)}人\n不及格共{scoreInfo.get("不及格",0)}人")

count_score_levels(students)

#从序列创建字典
keys = ['A', 'B', 'C']
values = [1, 2, 3]
newdict=dict.fromkeys(keys,0)
zipdict=dict(zip(keys,values))
print(f"fromkeys创建字典：{newdict}")
print(f"zip创建字典：{zipdict}")