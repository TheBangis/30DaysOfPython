# Day 20: 30 days of python programming


# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import re
import requests
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
text = response.text
text = re.sub(r'[^\w\s]','',text)
words = text.split()
words_dict = {}
for word in words:
    words_dict[word] = words_dict.get(word,0) + 1
words_sorted = sorted(words_dict.items(),key=lambda x:x[1],reverse=True)
result = [(word[1],word[0]) for word in words_sorted]
print(result[:10]) # it worked, yay!!!!!
        

'''
Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
the min, max, mean, median, standard deviation of cats' weight in metric units.
the min, max, mean, median, standard deviation of cats' lifespan in years.
Create a frequency table of country and breed of cats
'''
cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)

if response.status_code == 200:
    cat_breeds = response.json()
else:
    print("Failed to retrieve information from API")

'''getting the list of the weights of all the cats in metric units, 
has upper and lower limits'''
cat_weight_metric = []
for i in range(len(cat_breeds)):
  cat_weight_metric.append(cat_breeds[i]['weight']['metric'])
cat_weight_metric[:5]

# Doing same for lifespan
cat_weight_lifespan = []
for i in range(len(cat_breeds)):
  cat_weight_lifespan.append(cat_breeds[i]['life_span'])
cat_weight_lifespan[:5]

# getting a function to make them integers and get two lists of upper and lower limits
def convert_to_numbers(string):
    start, end = map(int, string.split(" - "))
    return start, end

# converting the weights to numbers using the function to get upper and lower weight limits for each, two lists:
cat_weight_metric_number = list(map(convert_to_numbers,cat_weight_metric))
lower_cat_weight_metric,upper_cat_weight_metric = [i[0] for i in cat_weight_metric_number],[i[1]for i in cat_weight_metric_number]

# same for lifespans in years
cat_lifespan_number = list(map(convert_to_numbers,cat_weight_lifespan))
lower_cat_lifespan,upper_cat_lifespan = [i[0] for i in cat_lifespan_number],[i[1]for i in cat_lifespan_number]

# Using statistics module to get the descriptive statistics (mean,median and std) 
# for the lower and upper limits, can use the min and max list methods
import statistics as stats
print(f'Max of upper limit of cat\'s weights in metric units is: {max(upper_cat_weight_metric)} ')
print(f'Min of upper limit of cat\'s weights in metric units is: {min(upper_cat_weight_metric)} ')
print(f'Mean of upper limit of cat\'s weights in metric units is: {stats.mean(upper_cat_weight_metric)} ')
print(f'Median of upper limit of cat\'s weights in metric units is: {stats.median(upper_cat_weight_metric)} ')
print(f'Std of upper limit of cat\'s weights in metric units is: {stats.stdev(upper_cat_weight_metric)} ')

# Will use the function below to get the parameters
def stats_params(list):
    '''
    Takes a list and returns a dictionary of certain statistics parameters of the list
    '''
    import statistics as stats
    stat = {}
    stat['Max'] = max(list)
    stat['Minimum'] = min(list)
    stat['Mean'] = stats.mean(list)
    stat['Median'] = stats.median(list)
    stat['std'] = stats.stdev(list)
    return stat
print(stats_params(upper_cat_weight_metric))



print(f'Upper limit of cat weights in metric units: {stats_params(upper_cat_weight_metric)}, lower limit of cat weights in metric units: {stats_params(lower_cat_weight_metric)},upper limit of cat lifespan in years : {stats_params(upper_cat_lifespan)},lower limits of cat lifespan in years: {stats_params(lower_cat_lifespan)}')
answer_dict = {}
answer_dict['Upper limit stats of cat weights in metric units'] = stats_params(upper_cat_weight_metric)
answer_dict['Lower limit stats of cat weights in metric units'] = stats_params(lower_cat_weight_metric)
answer_dict['Upper limit stat of cat lifespan in years'] = stats_params(upper_cat_lifespan)
answer_dict['Lower limit stats of cat lifespan in years'] = stats_params(lower_cat_lifespan)
print(f'Answer to first two sub questions of question 2: {answer_dict}')


# Third sub-question
from collections import defaultdict
# Getting the frequency table 
frequency_table = defaultdict(int)
breed_info = {}
for breed in cat_breeds:
    breed_info[breed['name']] = breed['origin']
for breed in breed_info.values():
    frequency_table[breed] += 1

print(frequency_table)


'''Read the countries API and find
the 10 largest countries
the 10 most spoken languages
the total number of languages in the countries API

# Webpage is not working!

UCI is one of the most common places to get data sets for data science and machine learning.
Read the content of UCI (https://archive.ics.uci.edu/ml/datasets.php). 
Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
 '''

import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup4
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table that contains the list of data sets
table = soup.find('table', {'border': '1'})

# Extract the name of each data set from the table rows, for now, a humble goal due to my current limited skills
rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td')
    name = cells[0].text.strip()
    # Gives the names of all the datasets in the table
    print(f'{name}')
