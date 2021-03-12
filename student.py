# 开发时间: 2021/3/9 19:13
import jieba as jb

txt = open('三国演义.txt', 'r', encoding='utf-8').read()
words = jb.lcut(txt)
count = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        count[word] = count.get(word, 0)+1

items = list(count.items())

items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, counts = items[i]
    print("{0:<10}{1:>5}".format(word, counts))










