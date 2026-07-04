#BMI计算
#嵌套运动建议
#边界处理
height=float(input("请输入身高（m）"))
weight=float(input("请输入体重（kg）"))

if(height<=0 or weight<=0):
    print("输入数据无效，请重新运行程序")
    exit()

BMI = weight/(height ** 2)
if BMI < 18.5 :
    print("体重偏轻")
    print("增加营养摄入，适当力量训练")
elif BMI>=18.5 and BMI<24 :
    print("体重正常")
    print("保持现有运动习惯")
elif BMI>=24 and BMI<28 :
    print("超重")
    if BMI<26:
        print("建议每天快走30分钟")
    else:
        print("建议每天慢跑40分钟")
else:
    print("肥胖") 
    print("建议每天慢跑40分钟")

print("="*30)

#年龄分组
age=int(input("请输入年龄"))
if age>=0 and age<=17:
    print("未成年")
elif age>=18 and age<=35:
    print("青年")
elif age>=36 and age<=55:
    print("中年")
elif age>=56:
    print("老年")
else:
    print("年龄输入有误")

#综合健康评估
if BMI>=24 and age>=55:
    print("建议定期体检，关注心血管健康")
elif BMI>=18.5 and BMI<24 and age>=18 and age<=35:
    print("身体状况优秀，继续保持！")

print("="*30)

#match...case
def parse_instruction(ins):
    match ins:
        case ("move", x, y):
            if x>100 or y>100:
                return f"长途移动至({x}, {y})"
            else:
                return f"移动至({x}, {y})"
        case ["attack", target]:
            return f"攻击{target}"
        case {"cmd": "talk", "npc": name, "msg": content}:
            return f"对{name}说：“{content}”"
        case {"cmd": "special", "id": 0}:
            return "释放终极技能"
        case _:
            return "无效指令"

print(parse_instruction(("move", 50, 80)))
print(parse_instruction({"cmd": "talk", "npc": "村长", "msg": "你好"})) 
