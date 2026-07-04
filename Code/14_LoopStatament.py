#录入成绩
scores=list()
while True:
    score = float(input("请输入成绩（0-100），输入-1结束："))
    if(score>=0 and score<=100):
        scores.append(score)
    elif(score==-1):
        break
    else:
        print("输入无效")
        continue

print("="*30)

#分析阶段
totalStudent=0
totalScore=0.0
maxScore=0.0
minScore=0.0
avgScore=0.0
for index,grade in enumerate(scores):
    print(f"学生序号：{index}，成绩：{grade}")
    totalStudent+=1
    totalScore+=grade

print(f"总人数为{totalStudent}人，总分为{totalScore},平均分为{totalScore/totalStudent:.2f}，最高分为{max(scores)}，最低分为{min(scores)}")

#查找阶段
for i in scores:
    if int(i)==100:
        print("有满分学生")
        break
else:
    print("无满分学生")

#统计等级
levels = {"优秀": (90, 101), "良好": (80, 90), "中等": (70, 80), 
          "及格": (60, 70), "不及格": (0, 60)}
level_count = {"优秀": 0, "良好": 0, "中等": 0, "及格": 0, "不及格": 0}

for score in scores:      # 外层循环：遍历成绩
    for level, (low, high) in levels.items():  # 内层循环：遍历等级
        if score>=low and score < high:  # 判断成绩是否在该等级区间内
            level_count[level] += 1
            break  # 匹配后跳出内层循环，避免重复计数

print(level_count)

#排名阶段
scores.sort()
#scores.reverse()
num=1
for i in range(len(scores)-1,-1,-1):
    print(f"第{num}名：{scores[i]}")
    num+=1
    pass #后续增加逻辑





