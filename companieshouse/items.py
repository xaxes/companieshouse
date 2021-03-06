# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanieshouseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field() #
    cnr = scrapy.Field() #
    officers = scrapy.Field()
    address = scrapy.Field() #

class OfficerItem(scrapy.Item):
    name = scrapy.Field()
    surname = scrapy.Field()
    nationality = scrapy.Field()
    address = scrapy.Field()
    companies = scrapy.Field()
