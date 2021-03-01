import requests
from bs4 import BeautifulSoup
response=requests.get('http://example.com/')
page1 = BeautifulSoup(response.text,'html.parser')
#print(page1.body)
tag = page1.find('p')
#print(tag)
page_links=page1.select('a[href]')
#print(page_links)


page2=page1.find('a')
#print(page2)
new_page2=BeautifulSoup(page2.text,'html.parser')
#print(new_page2)
table_new_page=page2.find_all('table')
print(table_new_page)