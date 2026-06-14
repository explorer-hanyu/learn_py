# 定义各类变量
num= 42
pi = 3.14159
greeting = "hello world"
is_python_fun=True
fruits = ["apple","bananna","cherry"]
coordinates = (10,20)
unique_nums={1,2,3,4,5}
persion={"name":"Alice","age":30}

#输出各类变量的类型
print(type(num))
print(type(pi))
print(type(greeting))
print(type(is_python_fun))
print(type(fruits))
print(type(coordinates))
print(type(unique_nums))
print(type(persion))

#判断fruits是否为list类型
if(isinstance(fruits,list)):
    print("fruits is a list")
else:
    print("fruits is not a list")

# 一些数学运算
num1=num+8
num2=num/5
num3=num%7
num4=num**2

print("num1:%d,num2:%d,num3:%d,num4:%d" % (num1, num2, num3, num4))

#字符串操作
print(greeting)
print(greeting[0:5])
print(greeting[0::3])
print(greeting*3)

# 列表fruits操作
fruits.append("orange")
print(fruits)
fruits.remove(fruits[1])
print(fruits)
print(fruits[-1])

# 集合操作
unique_nums.add(6)
print(unique_nums)
unique_nums.add(3)
print(unique_nums)

if(4 in unique_nums):
    print("4在unique_nums中")
else:
    print("4不在unique_nums中")

# 字典操作
persion["email"] = "alice@example.com"
persion["age"] = 31
print(persion)