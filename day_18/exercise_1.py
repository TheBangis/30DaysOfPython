import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.replace('.','').split(' ')
dict = {}
for word in words:
    dict[word] = dict.get(word,0) + 1
sort_keysval = sorted(dict.items(),key = lambda x:x[1], reverse=True)
print(sort_keysval)