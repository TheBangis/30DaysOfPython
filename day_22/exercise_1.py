import requests, json
from bs4 import BeautifulSoup

'''Scrape the following website and store the data as json file
(url = 'http://www.bu.edu/president/boston-university-facts-stats/').


url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text())
print(soup.body.get_text())'''


'''Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file'''



import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content 
soup = BeautifulSoup(content, 'html.parser') 
print(soup.title.get_text()) 

tables = soup.find_all('table', {'cellpadding':'3'})

table = tables[0] 
for td in table.find('tr').find_all('td'):
    print(json.dumps(td.text))