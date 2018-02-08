# -*- coding: utf-8 -*-
# strip replace("1", "2")
#//span[contains(@class, "vote-post")]
import scrapy


class XiamiSpider(scrapy.Spider):
    name = 'xiami'
    allowed_domains = ['xiami.com']
    start_urls = ['http://www.xiami.com/u/53530979?spm=0.0.0.0.NOaCka']

    def parse(self, response):
        recent_songs = response.xpath("//td[@class='song_name']")
        songs = recent_songs.xpath("a[1]/text()").extract()
        singers = recent_songs.xpath("a[2]/text()").extract()
        for i in songs:
            print(i)
        for j in singers:
            print(j)

