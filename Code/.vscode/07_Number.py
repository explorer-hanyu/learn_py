a=10
b=3.5
c=2+3j
print("a=10,type="+str(type(a)))
print("b=2.5,type="+str(type(b)))
print("c=2+3j,type="+str(type(c)))

d=0xff
e=0o377
print("d=%d,e=%d" % (d,e))

print(f"3.99转为整数为：{int(3.99)}")
print(f"complex(5)为{complex(5)},complex(5,2)为{complex(5,2)}")

print(f"(15+7)*3/2={(15+7)*3/2}")
print(f"17/4={17/4}")
print(f"17//4={17//4}")
print(f"2**10={2**10}")

f=5*2.5/2
print(f"5*2.5/2={5*2.5/2},type={type(f)}")

salary=8500.5
month=12
annual=salary*month
saving=annual*0.2
print(f"salary={salary}\nmonth={month}\nannual={annual}\nsaving={saving}")