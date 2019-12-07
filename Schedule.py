# -*- coding: utf-8 -*-
import scrapy


class ScheduleSpider(scrapy.Spider):
    name = 'Schedule'
    allowed_domains = ['https://9anime.to/schedule']
    start_urls = ['https://9anime.to/schedule/']

    def parse(self, response):

        for sched in response.css('div.day-block'):
            item = {
                'Date':sched.css('div.date::text').extract(),
                'Name':sched.css('a.name::text').extract(),
                'Info':sched.css('div.release::text').extract()
                }
            yield item
            
        prev_page = response.css('span.prev > a::attr(href)').extract_first()
        if (prev_page):
            prev_prev = response.urljoin(prev_page)
            yield scrapy.Request(url = prev_prev, callback = self.parse)
        
