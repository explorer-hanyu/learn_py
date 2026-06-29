#定义统计函数
def calc_stats(scores):

    if(len(scores)==0):
        return (0, 0, 0, None, None)
    totalnum=len(scores)
    totalscore=sum(scores)
    avgscore=totalscore/totalnum
    maxsocre=max(scores)
    minscore=min(scores)
    return (totalnum,totalscore,avgscore,maxsocre,minscore)

#定义成绩函数
def get_grade(score, passing=60):
    if(score>=90):
        return "优秀"
    elif(score>=80):
        return "良好"
    elif(score>=70):
        return "中等"
    elif(score>=passing):
        return "及格"
    else:
        return "不及格"
    
#定义添加成绩函数
def add_scores(scores_list, *new_scores):
    newscores_list=[x for x in new_scores]
    scores_list+=newscores_list
    print(f"新增成绩：{newscores_list}")

#定义生成报告函数
def generate_report(**info):
    for key,value in info.items():
        print(f"{key}: {value}")

scores=list()
add_scores(scores,85, 92, 78, 88, 45)
add_scores(scores,100, 76, 93)
scoreinfo=calc_stats(scores)
print(f"总人数：{scoreinfo[0]}，总分：{scoreinfo[1]}，平均分：{scoreinfo[2]}，最高分：{scoreinfo[3]}，最低分:{scoreinfo[4]}")

for score in scores:
    print(f"成绩：{score}，等级：{get_grade(score)}")

generate_report(name="Nick",total=461,avg=98.2)

#使用 lambda 进行数据转换
str_scores = list(map(lambda x: str(x)+"分", scores))  # 填空：map + lambda
print(f"\n成绩（字符串格式）: {str_scores}")