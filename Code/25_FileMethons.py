# ========== 1. 准备初始数据 ==========
initial_logs = [
    "[2024-01-15 10:00:01] INFO - 应用启动\n",
    "[2024-01-15 10:05:23] ERROR - 数据库连接超时\n",
    "[2024-01-15 10:10:45] INFO - 用户登录成功\n",
    "[2024-01-15 10:15:12] WARNING - 磁盘空间不足\n",
    "[2024-01-15 10:20:33] ERROR - 文件未找到\n",
    "[2024-01-15 10:25:01] INFO - 应用关闭\n",
]

with open("app.log", "w") as f:      # 写入模式
    f.writelines(initial_logs)                # 写入多行

print("✓ 初始日志已创建")

# ========== 2. 读取与分析 ==========
print("\n=== 2. 读取与分析 ===")
with open("app.log", "r") as f:
    lines = f.readlines()                    # 读取所有行
    total = len(lines)
    error_count = 0
    for line in lines:
        if "ERROR" in line:
            error_count += 1
    print(f"总行数: {total}")
    print(f"ERROR 数量: {error_count}")

# ========== 3. 指针操作 ==========
print("\n=== 3. 指针操作 ===")
f = open("app.log", "r")
print(f"初始指针位置: {f.tell()}")      # tell()

# 读取第一行
first_line = f.readline()                   # readline()
print(f"第一行: {first_line.strip()}")
print(f"读取后指针位置: {f.tell()}")    # tell()

# 移回开头
f.seek(0, 0)                            # seek
print(f"重置后指针位置: {f.tell()}")

# 读取并打印所有 ERROR 行
print("\n--- ERROR 日志 ---")
for line in f:
    if "ERROR" in line:
        print(line.strip())
f.close()

# ========== 4. 生成报告 ==========
print("\n=== 4. 生成报告 ===")
with open("app.log", "r") as f:
    all_lines = f.readlines()

with open("report.txt", "w") as f:   # 写入模式
    f.write("=== 日志分析报告 ===\n")    # write()
    f.write(f"总日志数: {len(all_lines)}\n")
    error_lines = [line for line in all_lines if "ERROR" in line]
    f.write(f"ERROR 数: {len(error_lines)}\n")
    f.write("\n--- ERROR 详情 ---\n")
    f.writelines(error_lines)                 # writelines()
print("✓ 报告已生成")

# ========== 5. 追加新日志 ==========
print("\n=== 5. 追加新日志 ===")
with open("app.log", "a") as f:      # 追加模式
    f.write("[2024-01-15 10:30:00] INFO - 清理完成\n")
    f.write("[2024-01-15 10:35:00] ERROR - 磁盘已满\n")
print("✓ 新日志已追加")

# ========== 6. 截断测试 ==========
print("\n=== 6. 截断测试 ===")
f = open("app.log", "r+")             # 读写模式
print(f"截断前指针位置: {f.tell()}")
f.truncate(50)                              # truncate
f.flush()                                # flush
f.close()
print("✓ 文件已截断到50字节")

# 验证截断结果
with open("app.log", "r") as f:
    content = f.read()
    print(f"截断后内容（前100字符）:\n{content[:100]}...")



# ========== 7. 清理并重新生成 ==========
print("\n=== 7. 清理日志（过滤 ERROR）===")
with open("app.log", "r") as f:
    all_lines = f.readlines()

clean_lines = [line for line in all_lines if "ERROR" not in line]

with open("app.log", "w") as f:      # 写入模式（覆盖）
    f.writelines(clean_lines)

print(f"✓ 已清理，保留 {len(clean_lines)} 条日志")

# 验证最终结果
with open("app.log", "r") as f:
    print("最终日志内容：")
    for line in f:
        print(f"  {line.strip()}")