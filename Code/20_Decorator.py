import time
from functools import wraps

# ========== 全局配置 ==========
current_user_permission = "user"  # 模拟当前用户权限

# 基础装饰器 —— 日志记录
# 处理带参数的函数
def log_decorator(func):
    """打印函数调用信息和返回值"""
    @wraps(func)  # 保留原函数的元信息（名称、文档等）
    def wrapper(*args, **kwargs):
        print(f"调用函数：{func}，参数：{args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值：{result}")
        return result
    return wrapper 

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# 带参数的装饰器 —— 权限控制
def require_permission(level):
    """权限验证装饰器工厂"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            global current_user_permission
            if current_user_permission==level :
                 return func(*args, **kwargs)
            else:
                print(f"权限不足！需要 {level} 权限")
                return None
        return wrapper
    return decorator

# 类装饰器 —— 接口缓存
class CacheDecorator:
    """类装饰器：缓存函数结果"""
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        # 生成缓存键（简单起见，用 args 和 kwargs 的字符串表示）
        key = str(args) + str(kwargs)
        if key in self.cache:
            print("从缓存获取结果")
            return self.cache[key]  # 填空：返回缓存值
        result = self.func(*args, **kwargs)
        self.cache[key] = result
        return result

# 多个装饰器堆叠
@CacheDecorator
@log_decorator
@require_permission("admin")
def get_user_info(user_id):
    """模拟获取用户信息的耗时操作"""
    time.sleep(1)  # 模拟耗时
    return f"用户{user_id}的信息"

# 测试代码
print("=== 测试日志装饰器 ===")
print(add(3, 5))
print(greet("Alice"))
print(greet("Bob", greeting="Hi"))

print("\n=== 测试权限装饰器 ===")
# 当前权限为 "user"，调用需要 "admin" 权限的函数
result = get_user_info(1001)
print(f"结果：{result}")

print("\n=== 测试缓存 ===")
# 第二次调用应该从缓存获取
result2 = get_user_info(1001)
print(f"第二次调用结果：{result2}")

# 修改权限为 admin 后再测试
print("\n=== 修改权限后测试 ===")
current_user_permission = "admin"
result3 = get_user_info(1002)
print(f"结果：{result3}")