import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'
request = requests.get(url) # website request
# print(request) # confirm a request 200


# getting content from request
content_soup = BeautifulSoup(request.text, 'html.parser')
print(content_soup)
print("Book Price Scraper")
print("==================\n")
print("Scraping Book Information\n")

# title
for titles in content_soup.find_all('a'):
    gather_titles = titles.get('title')
    print(gather_titles)

# price
#availability

# completion
print("Scraping Complete")

# total books found
print(f"Total books Found: ")