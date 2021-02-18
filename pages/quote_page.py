from bs4 import BeautifulSoup

from scraper_project.locator.quotes_page_locator import QuotesPageLocator
from scraper_project.parser.quote import QuoteParser

"""
 In Beautiful soup everything thing that comes inside the Tags.
"""

class QuotesPages:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotesPageLocator.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
