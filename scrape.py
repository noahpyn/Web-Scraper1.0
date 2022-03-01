# webscraping with bs4
# 1. GET Requests 
# 2.  parse keywords. find_all()
# 3.  check it scraper is connected

from urllib.parse import quote_plus
import requests
from bs4 import BeautifulSoup


#### 01. GET REQUEST - > get url details for quotes, authors, tags etc. #####

url = ('https://quotes.toscrape.com/')
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')


##### 02. PARSE DATA FOR KEY WORDS ####

# iterate through each quote 
# print out quotes 
# print out the author quotes

for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
    
    
    # 03. Check if parser is connected 
        print(quoteTag.text)

