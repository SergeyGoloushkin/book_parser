import scrapy
from scrapy.http import HtmlResponse
from book24.items import Book24Item



class Book24ruSpider(scrapy.Spider):
    name = 'book24ru'
    allowed_domains = ['book24.ru']
    start_urls = ['https://book24.ru/knigi-bestsellery/']

    def parse(self, response:HtmlResponse):
        for link in response.css('div.product-card__image-holder a::attr(href)'):
            yield response.follow(link, callback=self.parse_book)
        for i in range(1, 25):
            next_page = f'https://book24.ru/knigi-bestsellery/page-{i}/'
            yield response.follow(next_page, callback=self.parse)

    def parse_book(self, response:HtmlResponse):
        link = response.url
        name = response.css('h1.product-detail-page__title::text').get()
        author = response.css('a.product-characteristic-link.smartLink::text').get()
        price_old = response.css('span.app-price.product-sidebar-price__price-old::text').get()
        price = response.css('span.app-price.product-sidebar-price__price::text').get()
        rating = response.css('span.rating-widget__main-text::text').get()
        yield Book24Item(link=link, name=name, author=author, price_old=price_old, price=price, rating=rating)
