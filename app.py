import requests

from scraper_project.pages.quote_page import QuotesPages

page_content = requests.get('http://quotes.toscrape.com').content
page = QuotesPages(page_content)

for quote in page.quotes:
    print(quote)