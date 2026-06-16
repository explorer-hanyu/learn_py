#Comment.py- 学习注释的示例代码
#author ： Nick
#data：20260616
import inspect

class Employee:
    '''
    员工类，包含员工的姓名、id、薪资等个人信息，及员工收入计算方法
    '''
    def __init__(self, emp_id, name, salary):
        '''
        初始化员工信息
        emp_id:员工ID
        name:员工姓名
        salary:当前薪资
        '''
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def annual_income(self):
        '''
        计算员工收入，返回年收入
        '''
        return self.salary * 12 #月薪×月份数得到年薪

    '''
    给员工加薪函数
    percent为加薪百分比
    '''
    def give_raise(self, percent):
        self.salary = self.salary * (1 + percent / 100)



# 待办、未完成项标记，用于标注需要后续补充、修改、实现的内容
#TODO: 后续可增加年终加计算功能
#FIXME: 修复数组越界bug（缺陷修复专用）
#NOTE/TIP: 预留扩展接口



def get_employee_info(emp):
    info = f"员工ID: {emp.emp_id}\n姓名: {emp.name}\n月薪: {emp.salary}" # f"" 格式化字符串，字符串 {} 大括号里嵌入变量、对象属性、表达式，自动拼接成完整文本
    return info

emp1 = Employee("E001", "张三", 8000)
emp2 = Employee("E002", "李四", 9500) #初始化员工李四

print(Employee.__doc__)
print("="*30)
help(Employee.annual_income)
print("="*30)
print(inspect.getdoc(Employee.__init__))