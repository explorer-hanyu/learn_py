#用户输入阶段
print("请输入账户余额：", end="")
balance_str = str(input())
balance = float(balance_str)
print("请输入开户行年份：", end="")
open_year = int(input())
print("请输入账户状态（0或1）：", end="")
is_activate = bool(input())

#利息计算
interest_rate=float(100)*0.03
years=2026-open_year
total_interest=(balance/100)*interest_rate*years

#进制转换
numstr="FF"
num=int(numstr,16)
print("字符numstr:%s,转换后num:%d" % (numstr,num))

#格式化和输出
print("您好，您目前账号余额为" + str(balance) + "元")
print("您已开户%d年，利息总额为" % years + str(total_interest) + "元")
if(is_activate):
    print("账户状态：活跃")
else:
    print("账户状态：冻结")

# 数据转换挑战
account_info = {"张三", "balance", "is_activate"}
accout_info_tuple = tuple(account_info)
print("账户信息元组：", accout_info_tuple)
account_set = set("122342563465")
print("集合：", account_set)

account_info_dict = dict([("name", "张三"), ("balance", balance), ("years", years)])
print("账户信息字典：", account_info_dict)