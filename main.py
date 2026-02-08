import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
request = requests.get(url) # website request
# print(request) # confirm a request 200

# getting content from request
content_soup = BeautifulSoup(request.text, 'html.parser')

# gather price, title, and availability

# elem title
elems_title = content_soup.select('h3 > a')
for elem in elems_title:
    print(elem.text)
