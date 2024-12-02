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
    nombre_consommateur = scrapy.Field()
    nbre_rater = scrapy.Field()
    src = scrapy.Field()
    id_product = scrapy.Field()