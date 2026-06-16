print("请输入第一位待计算的数字：", end=" ")
num1 = float(input())
print("请输入第一位待计算的数字：", end=" ")
num2 = float(input())

print("算术运算"+"="*20)
print(f"{num1}+{num2}为:{num1+num2}")
print(f"{num1}-{num2}:{num1-num2}")
print(f"{num1}*{num2}:{num1*num2}")
print(f"{num1}/{num2}为{num1/num2}")
print(f"{num1}**{num2}为{num1**num2}")
print(f"{num1}//{num2}为{num1//num2}")
print(f"-{num1}//{num2}为{(-num1)//num2}")

print("比较运算"+"="*20)
if(num1>num2):
    print("num1大于num2")
if(num1<num2):
    print("num1小于num2")
if(num1==num2):
    print("num1等于num2")

print("赋值运算"+"="*20)
if((n:=num1)>0):
    print("n为正数")
else:
    print("n不是正数")

print("逻辑运算"+"="*20)
is_positive1=num1>0
is_positive2=num2>0

if(is_positive1 and is_positive2):
    print("两个数都为正数")
if(is_positive1 or is_positive2):
    print("至少有一个数为正")
else:
    print("两个数都不为正数")


print("成员运算"+"="*20)
number_list=[1,2,3,4,5,6,7,8,9,10]
if(int(num1) in number_list):
    print("num1整数在列表number_list中")

if(int(num2) not in number_list):
    print("num2不在列表number_list中")

print("身份运算"+"="*20)
list_a=[1,2,3]
list_b=list_a
if(list_b is list_a):
    print("list_a和list_b指向同一对象")
else:
    print("list_a和list_b不指向同一对象")

list_c=list_a[:]
if(list_c is list_a):
    print("list_a和list_c指向同一对象")
else:
    print("list_a和list_c不指向同一对象")

if(list_c == list_a):
    print("list_a和list_c相等")
else:
    print("list_a和list_c不相等")

# ==比较值是否相等，is判断是否指向同一对象

print("运算优先级判断"+"="*20)
print(f"5 + 3 * 2 ** 3 // 4 - 1={5 + 3 * 27 // 4 - 1}")
print(f"5 + 3 * 2 ** 3 // 4 - 1={5 + 3 * (27 // 4) - 1}")
print(f"5 + 3 * 2 ** 3 // 4 - 1={5 + (3 * 27) // 4 - 1}")