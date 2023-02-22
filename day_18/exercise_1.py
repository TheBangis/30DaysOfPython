import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
words = paragraph.replace('.','').split(' ')
dict = {}
for word in words:
    dict[word] = dict.get(word,0) + 1
sort_keysval = sorted(dict.items(),key = lambda x:x[1], reverse=True)
print(sort_keysval)


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
pattern = r'[^\w\s]'
clean_sentence = re.sub(pattern, "", sentence)
print(clean_sentence)
