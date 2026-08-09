def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        raise ValueError("Cannot divide by zero")
    else:
        return a/b

# 自测代码（仅在直接运行时执行）
if __name__ == '__main__':
    print("basic module self-test passed")