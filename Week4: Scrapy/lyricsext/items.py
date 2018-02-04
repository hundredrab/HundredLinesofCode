# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class LyricsextItem(scrapy.Item):
    """Field for items defined here."""

    title = Field()
    lyrics = Field()
    album = Field()
    artist = Field()

    # Housekeeping files
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()
