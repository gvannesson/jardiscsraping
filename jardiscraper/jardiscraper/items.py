# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JardiscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    marque = scrapy.Field()
    src = scrapy.Field()

class JardicatItem(scrapy.Item):
    titre_categorie = scrapy.Field()
    url_categorie = scrapy.Field()
    is_page_list = scrapy.Field()
    cat_parente = scrapy.Field()
