import re, json, os, csv

'''
Write a function which count number of lines and number of words in a text. 
All the files are in the data the folder: 
a) Read obama_speech.txt file and count number of lines and words 
b) Read michelle_obama_speech.txt file and count number of lines and words
c) Read donald_speech.txt file and count number of lines and words 
d) Read melina_trump_speech.txt file and count number of lines and words
'''

def count_number_lines(files):
    with open(files) as f:
       lines = f.readlines()

       words = []

       for line in lines:
           line = re.sub(r'[^\w\s]','',line)
           words.extend(line.split())

    print(f'The number of lines and words in the file are {len(lines)} and {len(words)}')

count_number_lines('day_19/obama_speech.txt')
count_number_lines('day_19/donald_speech.txt')
count_number_lines('day_19/michelle_obama_speech.txt')

