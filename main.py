import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
request = requests.get(url) # website request
# print(request) # confirm a request 200


# getting content from request
content_soup = BeautifulSoup(request.text, 'html.parser')
print(content_soup)
