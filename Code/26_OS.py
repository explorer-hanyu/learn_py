import os
import time

def list_current_dir():
    """列出当前目录内容"""
    cwd = os.getcwd()  # 获取当前工作目录
    print(f"\n当前目录: {cwd}")
    print("-" * 40)
    items = os.listdir('.')  # 列出目录内容
    for item in sorted(items):
        full_path = os.path.join('.', item)
        if os.path.isdir(full_path):  # 判断是否为目录
            print(f"[DIR]  {item}")
        elif os.path.isfile(full_path):  # 判断是否为文件
            print(f"[FILE] {item}")
    print("-" * 40)

def change_dir(path):
    """切换工作目录"""
    try:
        os.chdir(path)  # 切换目录
        print(f"✓ 已切换到: {os.getcwd()}")
    except FileNotFoundError:
        print("✗ 目录不存在")

def create_dir(path):
    """创建目录"""
    try:
        if '/' in path or '\\' in path:
            os.makedirs(path)  # 填空：递归创建多层目录
        else:
            os.mkdir(path)  # 填空：创建单层目录
        print(f"✓ 目录已创建: {path}")
    except FileExistsError:
        print("✗ 目录已存在")

def delete_dir(path):
    """删除空目录"""
    if not os.path.isdir(path):
        print("✗ 不是有效的目录")
        return
    contents = os.listdir(path)  # 列出目录内容
    if contents:
        print("✗ 目录非空，无法删除")
        return
    os.rmdir(path)  # 删除空目录
    print(f"✓ 目录已删除: {path}")

def delete_file(path):
    """删除文件"""
    if not os.path.isfile(path):
        print("✗ 文件不存在")
        return
    os.remove(path)  # 删除文件
    print(f"✓ 文件已删除: {path}")

def rename_item(old, new):
    """重命名文件或目录"""
    try:
        os.rename(old, new)  # 重命名
        print(f"✓ 已重命名: {old} → {new}")
    except FileNotFoundError:
        print("✗ 源文件不存在")

def file_info(path):
    """查看文件信息"""
    if not os.path.exists(path):  # 判断路径是否存在
        print("✗ 文件或目录不存在")
        return
    print(f"\n=== {path} 的信息 ===")
    print(f"绝对路径: {os.path.abspath(path)}")  # 获取绝对路径
    if os.path.isfile(path):
        size = os.path.getsize(path)  #获取文件大小
        print(f"大小: {size} 字节")
        mtime = os.path.getmtime(path)  # 获取修改时间
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
        print(f"修改时间: {time_str}")

def main():
    """主程序"""
    while True:
        print("\n" + "=" * 30)
        print("     文件管理器")
        print("=" * 30)
        print("1. 浏览当前目录")
        print("2. 切换目录")
        print("3. 创建目录")
        print("4. 删除目录")
        print("5. 删除文件")
        print("6. 重命名")
        print("7. 查看文件信息")
        print("8. 退出")
        choice = input("请选择（1-8）：")

        if choice == "1":
            list_current_dir()
        elif choice == "2":
            path = input("请输入目录路径：")
            change_dir(path)
        elif choice == "3":
            path = input("请输入目录名：")
            create_dir(path)
        elif choice == "4":
            path = input("请输入目录名：")
            delete_dir(path)
        elif choice == "5":
            path = input("请输入文件名：")
            delete_file(path)
        elif choice == "6":
            old = input("请输入原名称：")
            new = input("请输入新名称：")
            rename_item(old, new)
        elif choice == "7":
            path = input("请输入文件或目录名：")
            file_info(path)
        elif choice == "8":
            print("再见！")
            break  # 退出循环
        else:
            print("无效选择")

if __name__ == "__main__":  # 填空：程序入口判断
    main()