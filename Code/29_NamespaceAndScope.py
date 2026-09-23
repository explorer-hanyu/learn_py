# ========== 1. 定义变量和嵌套函数 ==========
global_counter = 0          # 全局变量

def outer():
    outer_counter = 0       # 外层函数变量（enclosing）
    print(f"[outer] 初始 outer_counter = {outer_counter}")

    def inner():
        inner_counter = 0   # 内层函数变量（local）
        global global_counter   # global 声明
        nonlocal outer_counter   # nonlocal 声明
        print(f"\n[inner] 初始值: global={global_counter}, outer={outer_counter}, inner={inner_counter}")

        # ========== 2. 修改全局变量 ==========
        global_counter += 1   # 自增
        print(f"[inner] 修改后 global = {global_counter}")

        # ========== 3. 修改外层变量 ==========
        outer_counter  +=1   # 自增
        print(f"[inner] 修改后 outer = {outer_counter}")

        # ========== 4. 修改局部变量 ==========
        inner_counter += 1   # 自增（不加关键字）
        print(f"[inner] 修改后 inner = {inner_counter}")

        return outer_counter, inner_counter

    # ========== 5. 观察 UnboundLocalError ==========
    def test_unbound():
        # 下面的代码会报错，因为 global_counter 被赋值，
        # Python 将其视为局部变量，但赋值前又被引用
        # global_counter = global_counter + 1  # 取消注释会报 UnboundLocalError
        pass

    return inner

# ========== 6. 执行测试 ==========
if __name__ == "__main__":
    print("=" * 40)
    print("嵌套计数器系统")
    print("=" * 40)

    inner_func = outer()

    # 调用 inner 三次
    for i in range(3):
        print(f"\n--- 第 {i+1} 次调用 inner ---")
        inner_func()

    print("\n" + "=" * 40)
    print("最终结果")
    print("=" * 40)
    print(f"global_counter = {global_counter}")
    # 注意：outer_counter 和 inner_counter 是局部变量，无法从外部访问
    # 只能通过函数返回值获取，这里演示作用域的限制