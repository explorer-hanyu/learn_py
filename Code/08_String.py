import time
# 字符创建与访问
full_name="Zhang San"
print(f"{full_name}第一个字符为{full_name[0]}")
print(f"{full_name}最后一个字符为{full_name[-1]}")
print(f"{full_name}姓氏为{full_name[:5]}")
print(f"{full_name}名字为{full_name[6:]}")

#字符串更新与拼接
full_name += "feng"
print("Hello, "+full_name)

#转义字符练习
print("姓名：\t张三\n年龄：\t25\n职业：\t工程师")
print(r"C:\Users\name\Documents\file.txt")

for i in range(6):
    print(f"\r{5-i}",end='', flush=True)
    time.sleep(1)

#字符串运算符
print("="*30)
judgeStr="Python3 字符串练习"
if "Python" in judgeStr:
    print(f"Python in {judgeStr}")
if "Java" not in judgeStr:
    print(f"Java is not in {judgeStr}")

#字符串格式化
name="李四"
age=28
score=92.5
print("%s，%d岁，成绩%.1f分" % (name, age, score))

print("{:s}，{:d}岁，成绩{:.1f}分".format(name,age,score))

print(f"{name}，{age+5}岁，成绩{score}分")

#三引号多行字符串
mutiStr=\
'''
========== 用户信息 ==========
姓名：王五
城市：北京
签名：好好学习，天天向上！
================================
'''
print(mutiStr)

#字符串方法练习
text = " hello world! "
print(f"text原文：{text}")
print(f"去除首尾空格：{text.strip()}")
print(f"将首字母大写：{text.capitalize()}")
print(f"所有单词首字母大写：{text.title()}")
print(f"所有字母转大写：{text.upper()}")

intex=text.find("world")
print(f"world替换为Python:{text.replace("world","Pyhon",-1)}")

print(f"将字符串分隔为列表：{text.split()}")
print(F"将列表拼接为字符串，用-连接：{"-".join(text.split())}")

print("请输入你的姓名：", end=" ")
usrname=input()
print("请输入你的年龄", end=" ")
usrage=input()
print(f"你好，{usrname}！你输入的年龄是{usrage}岁，5年后你将{usrage+5}岁。")
