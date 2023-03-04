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


'''
Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 10))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic'),
(24, 'Spanish'),
(9, 'Russian'),
(9, 'Portuguese'),
(8, 'Dutch'),
(7, 'German'),
(5, 'Chinese'),
(4, 'Swahili'),
(4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename='./data/countries_data.json', 3))
[(91, 'English'),
(45, 'French'),
(25, 'Arabic')]
'''
def most_spoken_languages(file, n):
    with open(file) as f:
        list = json.loads(f.read())

    languages = []
    for i in range(len(list)):
        languages.extend(list[i]['languages'])
    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1
    # sorting the list of the tuples to get the most spoken languages
    sorted = sorted(lang.items(), key= lambda x:x[1],reverse=True) # contains the languages arranged based on values
    result = [(item[1],item[0]) for item in sorted]
    return result[:n]
print(most_spoken_languages('day_19/countries_data.json',3))