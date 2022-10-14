from dataclasses import replace
from bs4 import BeautifulSoup
import requests
import json


url= "https://finans.mynet.com/borsa/hisseler/"

page = requests.get(url)



soup = BeautifulSoup(page.content, 'html.parser')


tables = soup.find('tbody')


titles = []
for index,table in enumerate(tables.find_all('a',href=True)):
    title = table.text
    #titles.append(title)
    url3 = table['href']
    page3 = requests.get(url3)
    soup3 = BeautifulSoup(page3.content, 'html.parser')
    tables3 = soup3.find('div', class_="flex-list-2-col")
    for table3 in tables3.find_all('li', class_="flex"):
        a = table3.text
        x = a.replace("\n","")
        last = {
        'title' : title,
        'description' : x
        }
        #titles.append(a)
        titles.append(last)
    
    print(index)
    

with open('proje.json','w') as f:
    json.dump(titles,f)

print(titles)