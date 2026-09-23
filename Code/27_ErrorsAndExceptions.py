import sys
import datetime

# ========== 1. 自定义异常 ==========
class CalculationError(Exception):
    """计算异常基类"""
    pass

class DivisionByZeroError(CalculationError):
    """除零异常"""
    pass

class InvalidOperationError(CalculationError):
    """无效操作异常"""
    pass

# ========== 2. 计算函数 ==========
def calculate(op, a, b):
    """执行计算，遇到错误抛出对应异常"""
    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    elif op == 'divide':
        if b == 0:
            raise DivisionByZeroError("除数不能为零")
        return a / b
    elif op == 'power':
        return a ** b
    else:
        raise InvalidOperationError(f"不支持的操作：{op}")  # 抛出 InvalidOperationError

# ========== 3. 写入日志 ==========
def log_operation(op, a, b, result, error=None):
    """将操作记录写入日志文件"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error:
        log_line = f"[{timestamp}] {op} {a} {b} = ERROR: {error}\n"
    else:
        log_line = f"[{timestamp}] {op} {a} {b} = {result}\n"
    with open("calc.log", "a") as f:  # 追加模式
        f.write(log_line)

# ========== 4. 主程序 ==========
def main():
    print("=== 健壮计算器 ===")
    print("支持操作: add, subtract, multiply, divide, power")
    print("输入格式: 操作 数字1 数字2")
    print("输入 'quit' 退出\n")

    while True:
        user_input = input("请输入: ").strip()
        if user_input.lower() == 'quit':
            print("再见！")
            break

        parts = user_input.split()
        try:
            # 检查参数数量
            if len(parts) != 3:
                 raise IndexError("参数不合规") # 抛出 IndexError（或手动 raise）
                  

            op = parts[0].lower()
            a = float(parts[1])
            b = float(parts[2])

            # 执行计算
            result = calculate(op, a, b)

        except DivisionByZeroError as e:
            error_msg = "除数不能为零"
            print(f"错误：{error_msg}")
            log_operation(op, a, b, None, error_msg)

        except InvalidOperationError as e:
            error_msg = f"不支持的操作 '{op}'"
            print(f"错误：{error_msg}")
            log_operation(op, a, b, None, error_msg)

        except ValueError:
            error_msg = "参数必须是数字"
            print(f"错误：{error_msg}")
            log_operation(op, a, b, None, error_msg)

        except IndexError:
            error_msg = "请提供 操作 数字1 数字2"
            print(f"错误：{error_msg}")
            # 无法记录日志（没有完整参数）

        except Exception as e:
            error_msg = str(e)
            print(f"未知错误: {error_msg}")
            log_operation("unknown", 0, 0, None, error_msg)
            raise  # 重新抛出异常（raise）

        else:  # else 子句
            print(f"结果: {result}")
            log_operation(op, a, b, result, None)

        finally:  # finally 子句
            print("--- 操作完成 ---")

if __name__ == "__main__":  # 填空：程序入口判断
    main()