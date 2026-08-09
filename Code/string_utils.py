"""字符串处理工具模块"""

def count_vowels(s):
    """统计字符串中元音字母的个数（不区分大小写）"""
    vowels = 'aeiou'
    count = 0
    for char in s.lower():
        if char in vowels:
            count+=1
    return count

def reverse_words(s):
    """将字符串中的单词顺序反转,按空格分割"""
    words = s.split()  #按空格分割
    reversed_words = words[::-1]  #使用切片反转列表
    return ' '.join(reversed_words)

def is_palindrome(s):
    """判断字符串是否为回文（忽略大小写和空格）"""
    # 去除空格并转为小写
    cleaned =''.join(s.split()).lower()
    # 判断 cleaned 是否等于其反转
    return cleaned == cleaned[::-1]  #使用切片反转

# ========== 自测代码 ==========
if __name__ == '__main__':  #__name__ 判断
    print("=" * 40)
    print("字符串工具模块自测")
    print("=" * 40)

    # 测试 count_vowels
    test1 = "Hello World"
    print(f"count_vowels('{test1}') = {count_vowels(test1)}")  # 应为 3

    # 测试 reverse_words
    test2 = "Hello World Python"
    print(f"reverse_words('{test2}') = '{reverse_words(test2)}'")  # 应为 "Python World Hello"

    # 测试 is_palindrome
    test3 = "A man a plan a canal Panama"
    print(f"is_palindrome('{test3}') = {is_palindrome(test3)}")  # 应为 True

    test4 = "Hello"
    print(f"is_palindrome('{test4}') = {is_palindrome(test4)}")  # 应为 False

    print("=" * 40)
    print("自测完成")