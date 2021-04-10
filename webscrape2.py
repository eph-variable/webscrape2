import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Elon_Musk"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

wantedSoup = soup.find_all('a')

for w in wantedSoup:
	name = w.find(string="Elon Musk")
	if None == name:
		continue
	print(name)
	print(w.text)


