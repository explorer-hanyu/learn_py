import datetime

DIARY_FILE = "diary.txt"
REPORT_FILE = "report.txt"

def view_diary():
    """查看所有日记"""
    try:
        with open(DIARY_FILE, "r") as f:  # 只读模式
            lines = f.readlines()  # 读取所有行
        if not lines:
            print("暂无日记记录")
            return
        print("\n===== 我的日记 =====")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")
    except FileNotFoundError:
        print("暂无日记记录")

def write_diary():
    """写入新日记"""
    content = input("请输入日记内容：")
    if not content.strip():
        print("内容不能为空")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DIARY_FILE, "a") as f:  #追加模式
        f.write("\n[{time}] {cont}".format(time=timestamp,cont=content))  # 写入 "[时间戳] 内容\n"
    print("✓ 日记已保存")

def export_report():
    """导出统计报告"""
    try:
        with open(DIARY_FILE, "r") as f:
            lines = f.readlines()
        if not lines:
            print("暂无日记，无法导出报告")
            return
        count = len(lines)
        first = lines[0].strip()
        last = lines[-1].strip()
        report = """
        {line}
        {title}
        {line}
        总日记数：{count} 条
        第一条：{first}
        最后一条：{last}
        {line}
        """.format(  #使用 format()
            line="=" * 40,
            title="日记统计报告".center(38),
            count=count,
            first=first,
            last=last
        )
        with open(REPORT_FILE, "w") as f:
            f.write(report)
        print(f"✓ 报告已导出到 {REPORT_FILE}")
    except FileNotFoundError:
        print("暂无日记，无法导出报告")

def main():
    """主程序"""
    while True:
        print("\n===== 我的日记本 =====")
        print("1. 查看所有日记")
        print("2. 写新日记")
        print("3. 导出报告")
        print("4. 退出")
        choice = input("请选择（1-4）：")
        if choice == "1":
            view_diary()
        elif choice == "2":
            write_diary()
        elif choice == "3":
            export_report()
        elif choice == "4":
            print("再见！")
            break  # 退出循环
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":  # 程序入口判断
    main()