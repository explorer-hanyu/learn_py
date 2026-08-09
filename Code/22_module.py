import sys
from cli_tool import basic as b
from cli_tool import advanced as a

def print_usage():
    print("用法: python 22_module.py <操作> <参数...>")
    print("支持的操作: add, subtract, multiply, divide, power, sqrt, factorial")
    print("示例: python 22_module.py add 3 5")

def main():
    args = sys.argv[:]

    if len(args) < 2:
        print_usage()
        return

    operation = args[1]

    # 解析数字参数
    try:
        if operation in ['sqrt', 'factorial']:
            if len(args) < 3:
                print("错误：需要 1 个参数")
                return
            num = float(args[2])
            # 调用对应函数
        else:
            if len(args) < 4:
                print("错误：需要 2 个参数")
                return
            num1 = float(args[2])
            num2 = float(args[3])
            # 调用对应函数
    except ValueError:
        print("错误：参数必须是数字")
        return

    # 根据操作调用对应的函数
    result = None
    if operation == 'add':
        result = b.add(num1, num2)
    elif operation == 'subtract':
        result = b.subtract(num1, num2)
    elif operation == 'multiply':
        result = b.multiply(num1, num2)
    elif operation == 'divide':
        result = b.divide(num1, num2)
    elif operation == 'power':
        result = a.power(num1, num2)
    elif operation == 'sqrt':
        result = a.sqrt(num)
    elif operation == 'factorial':
        # 阶乘需要整数
        result = a.factorial(int(num))
    else:
        print(f"错误：不支持的操作 '{operation}'")
        print_usage()
        return

    print(f"结果: {result}")

if __name__ == '__main__':
    main()
