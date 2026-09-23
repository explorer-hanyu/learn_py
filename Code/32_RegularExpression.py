import re

log_data = """
192.168.1.1 - admin [01/Jan/2024:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - guest [01/Jan/2024:12:00:05 +0000] "POST /api/login HTTP/1.1" 200 256
192.168.1.1 - admin [01/Jan/2024:12:00:10 +0000] "GET /about.html HTTP/1.1" 404 512
192.168.1.3 - - [01/Jan/2024:12:00:15 +0000] "GET /index.html HTTP/1.1" 200 1024
192.168.1.2 - guest [01/Jan/2024:12:00:20 +0000] "GET /dashboard.html HTTP/1.1" 403 0
"""

# ========== 1. 提取所有 IP 地址 ==========
print("=== 1. 提取 IP 地址 ===")
ip_pattern = r'\d+\.\d+\.\d+\.\d+'
ips = re.findall(ip_pattern, log_data)  #findall
unique_ips = set(ips)
print(f"所有 IP: {ips}")
print(f"去重后: {unique_ips}")

# ========== 2. 提取所有状态码（finditer）==========
print("\n=== 2. 提取状态码 ===")
status_pattern = re.compile(r'\b\d{3}\b')
for match in re.finditer(status_pattern, log_data):  #finditer
    print(f"状态码: {match.group()}, 位置: {match.span()}")

# ========== 3. 提取请求方法和路径 ==========
print("\n=== 3. 提取请求方法和路径 ===")
request_pattern = r'"(\w+) (/\S+) HTTP/\d\.\d"'
for line in log_data.strip().split('\n'):
    match = re.search(request_pattern, line)  #search
    if match:
        method = match.group(1)  #group
        path = match.group(2)
        print(f"方法: {method}, 路径: {path}")

# ========== 4. 替换敏感信息 ==========
print("\n=== 4. 替换 IP 为 *** ===")
masked_log = re.sub(ip_pattern, '***', log_data)  #sub
print(masked_log)

# ========== 5. 分割日志字段 ==========
print("\n=== 5. 提取用户名 ===")
for line in log_data.strip().split('\n'):
    # 按空格或 - 分割
    parts = re.split(r'[\s-]+', line)  #split
    if len(parts) >= 3:
        print(f"用户名: {parts[2]}")

# ========== 6. 编译正则表达式（综合提取）==========
print("\n=== 6. 完整日志解析 ===")
# 编译完整的日志匹配模式
full_pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) \S+ (\S+) \[([^\]]+)\] "(\w+) (/\S+) HTTP/\d\.\d" (\d{3}) (\d+)'
)

for line in log_data.strip().split('\n'):
    match = full_pattern.search(line)  #search
    if match:
        ip, user, date, method, path, status, size = match.groups()  #groups
        print(f"IP: {ip}, 用户: {user}, 日期: {date}")
        print(f"  请求: {method} {path}, 状态: {status}, 大小: {size}")

# ========== 7. 统计分析 ==========
print("\n=== 7. 统计分析 ===")
status_counts = {}
ip_counts = {}

for line in log_data.strip().split('\n'):
    match = full_pattern.search(line)
    if match:
        ip, user, date, method, path, status, size = match.groups()
        status_counts[status] = status_counts.get(status, 0) + 1  #get
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

print("状态码统计:")
for status, count in status_counts.items():
    print(f"  {status}: {count} 次")

print("\nIP 请求统计:")
for ip, count in ip_counts.items():
    print(f"  {ip}: {count} 次")