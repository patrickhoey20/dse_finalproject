from bs4 import BeautifulSoup
import requests
import sys
from string import ascii_lowercase


# Get links for all player pages
linklist = []
for i in ascii_lowercase:
 	url = "https://www.baseball-reference.com/players/" + i + "/"
 	r = requests.get(url)
 	soup = BeautifulSoup(r.text, 'html.parser')
 	x = soup.body
 	x = x.find('div',{"class": "section_content"})
 	z = x.find_all('a')
 	for j in z:
 		linklist.append(['href'])


# url = "https://chicago.craigslist.org/search/zip"
# #print(url)
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')

# x = soup.body
# x = x.find(id="search-results")
# x = x.find_all('a', {"class": "result-title hdrlnk"})
# count = 0
# for i in x:
# 	count = count +1
# 	print(i['href'])


# url = "https://www.baseball-reference.com/players/" + "a" + "/"
# r = requests.get(url)
# soup = BeautifulSoup(r.text, 'html.parser')
# x = soup.body
# x = x.find('div',{"class": "section_content"})
# z = x.find_all('a')
# for j in z:
# 	print(j['href'])
