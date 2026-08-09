from collections import deque

#数据准备
text = """apple banana apple orange banana grape apple
orange grape banana apple pear orange grape
banana apple pear orange grape"""

#列表操作（栈+队列）
words = text.split()
print(f"原列表为:{words}")
stack = []
for word in words:
    stack.append(word)
reversed_words = []
for i in range(len(stack)):
    reversed_words.append(stack.pop())
print(f"栈反转后前5个: {reversed_words[:5]}")

queue = deque()
for word in words:
    queue.append(word)

print("队列操作前5个元素依次为", end=" ")
for i in range(5):
    print(f"{queue.popleft()}", end=" ")
print()

#列表推导式
long_words = [word for word in words if len(word)>5]
print(f"长度大于5的单词有：{long_words}")

upper_words = [word.upper() for word in words]
print(f"所有单词转换为大写后为：{upper_words}")

#集合运算
unique_words = set(words)
print(f"一共出现了这些单词：{unique_words}")
fruits = {'apple', 'banana', 'grape', 'orange', 'pear'}
print(f"一共出现了这些水果：{unique_words & fruits}")
print(f"出现的非水果单词有：{unique_words - fruits}")

#字典操作
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"单词出现的次数为：{word_count}")

biggest=0
most_word=""
for key,value in word_count.items():
    if value>biggest:
        biggest=value
        most_word=key
print(f"出现最多的单词为：{most_word},出现{biggest}次")

max_word = max(word_count, key=word_count.get) 
print(f"出现最多的单词: '{max_word}'，出现 {word_count[max_word]} 次")

for key,value in word_count.items():
    print(f"单词{key}出现了{value}次")


#del语句
print(f"del前words长度为{len(words)}")
del words[0:5]
print(f"del后words长度为{len(words)}")

#遍历技巧
print("\n枚举遍历（序号从1开始）:")
for i, word in enumerate(unique_words, start=1):  
    print(f"  {i}. {word}")

# zip 遍历
freq_list = [word_count[w] for w in unique_words]
print("\n单词频率:")
for w, f in zip(unique_words, freq_list):  
    print(f"  {w}: {f}")

# reversed 反向遍历
unique_list = list(unique_words)
print("\n反向遍历:")
for word in reversed(unique_list): 
    print(f"  {word}")

# sorted 排序遍历
print("\n排序遍历:")
for word in sorted(unique_list): 
    print(f"  {word}")
