"""Spider to extract lyrics/quotes."""
import scrapy


class LyricSpider(scrapy.Spider):
    """docstring for LyricSpider."""

    name = 'LyricSpider'
    allowed_domains = ['https://genius.com/']

    start_urls = [
        'https://genius.com/Mumford-and-sons-snake-eyes-lyrics',
    ]

    def parse(self, response):
        """Doc go here."""
        self.log("title: %s" % response.xpath(
            '/html//h1/text()').extract())

        self.log("lyrics-----------")

        self.log("album: %s" % response.xpath(
            '/html//*[contains(@class, "metadata_unit")]//a[contains(@href, "albums")]/text()').extract())

        self.log("Lyrics: %s" % response.xpath(
            ('/html//*[contains(@class,"lyric")]//a/text()|/html//*[contains(@class,"lyric")]//p/text()')
            ).extract())
