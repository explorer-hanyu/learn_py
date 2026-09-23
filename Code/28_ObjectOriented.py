# ========== 1. 基类 Book ==========
class Book:
    """书籍基类"""
    total_books = 0  # 类变量，统计书籍总数

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False  # 私有属性 __is_borrowed
        Book.total_books +=1  # 累加

    def borrow(self):
        """借阅书籍"""
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        """归还书籍"""
        self.__is_borrowed = False

    def get_info(self):
        """获取书籍信息"""
        status = "已借出" if self.__is_borrowed else "在馆"
        return f"《{self.title}》- {self.author} [{status}]"

    def __str__(self):
        """运算符重载：字符串表示"""
        return f"《{self.title}》- {self.author}"


# ========== 2. 子类 EBook ==========
class EBook(Book):  # 继承 Book
    """电子书类"""
    def __init__(self, title, author, file_size):
        Book.__init__(self, title, author)  # 调用父类构造方法
        self.file_size = file_size

    def get_info(self):
        """方法重写：添加文件大小信息"""
        parent_info = super().get_info()  # 使用 super() 调用父类方法
        return f"{parent_info} [电子书, {self.file_size}MB]"


# ========== 3. 子类 PrintedBook ==========
class PrintedBook(Book):  # 继承 Book
    """纸质书类"""
    def __init__(self, title, author, pages):
        Book.__init__(self, title, author)  # 调用父类构造方法
        self.pages = pages

    def get_info(self):
        """方法重写：添加页数信息"""
        parent_info = super().get_info()  # 使用 super() 调用父类方法
        return f"{parent_info} [纸质书, {self.pages}页]"


# ========== 4. 测试代码 ==========
if __name__ == "__main__":
    # 创建书籍对象
    book1 = PrintedBook("Python编程", "张三", 350)
    book2 = EBook("数据结构", "李四", 5.2)
    book3 = PrintedBook("算法导论", "王五", 1200)

    print("=" * 40)
    print("图书馆藏书")
    print("=" * 40)

    # 打印所有书籍信息
    for book in [book1, book2, book3]:
        print(book.get_info())  # 调用 get_info

    print(f"\n馆藏总数: {Book.total_books} 本")

    # 借阅测试
    print("\n" + "=" * 40)
    print("借阅测试")
    print("=" * 40)

    print(f"借阅《Python编程》: {'成功' if book1.borrow() else '失败'}")
    print(f"再次借阅《Python编程》: {'成功' if book1.borrow() else '失败'}")

    book1.return_book()
    print(f"归还后再次借阅《Python编程》: {'成功' if book1.borrow() else '失败'}")

    # 验证私有属性不可访问
    print("\n" + "=" * 40)
    print("验证私有属性")
    print("=" * 40)
    try:
        print(book1.__is_borrowed)  # 应报错
    except AttributeError as e:
        print(f"✓ 无法访问私有属性: {e}")