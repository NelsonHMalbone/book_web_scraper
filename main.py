import requests
from bs4 import BeautifulSoup

request = requests.get('https://books.toscrape.com/catalogue/category/books_1/index.html') # website request
# print(request) # confirm a request 200

# getting content from request
content = request.text # gets raw html
#print(content) # testing to get content