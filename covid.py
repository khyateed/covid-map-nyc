import re
import csv
import json
from datetime import date
import requests
from bs4 import BeautifulSoup



# base_url = 'https://www.worldometers.info/coronavirus/#countries'
# r = requests.get(base_url)
# outfile = open(str(date.today()) + '.html', 'w')
# outfile.write(r.text.encode('utf8'))
# outfile.close()

df =[]
t = open("2020-04-14" + '.html','r')
soup = BeautifulSoup(t, "html.parser")
table = soup.find(id='main_table_countries_yesterday')

headers = table.find('thead').find('tr')
headers = headers.text.encode('utf8').split('\n')
headers[12] = 'Tests/1M pop'
headers[13] = 'Continent'
df.append(headers[1:14])

countries = table.find('tbody').findAll('tr')
for country in countries[7:]:
	items=[]
	items = country.text.encode('utf8').split('\n')
	df.append(items[1:])
print(df)
# with open(str(date.today()) + '.csv', "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(df)
	
