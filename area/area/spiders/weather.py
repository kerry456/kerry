# -*- coding: utf-8 -*-
import scrapy

from area.items import AreaItem

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['aqistudy.cn']
    base_url = 'http://www.aqistudy.cn/historydata/'
    start_urls = [base_url]
    def parse(self, response):
        #城市信息
        url_list = response.xpath('//div[@class="bottom"]/ul/div[2]/li/a/@href').extract()[:10]
        city_list = response.xpath('//div[@class="bottom"]/ul/div[2]/li/a/text()').extract()[:10]
        for Url,city in zip(url_list,city_list):
            url = self.base_url + Url
            yield scrapy.Request(url=url,meta={'city':city},callback=self.parse_month)
    def parse_month(self,response):
        #爬取月份信息
        url_list = response.xpath('//tbody/tr/td/a/@href').extract()[-4:]
        for Url in url_list:
            url = self.base_url + Url
            yield scrapy.Request(url=url,meta={"city": response.meta['city']},callback=self.parse_day)
    def parse_day(self,response):
        #最终数据
        item = AreaItem()
        node_list = response.xpath('//tr')
        node_list.pop(0)
        for node in node_list:
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['city'] = response.meta['city']
            item['AQI'] = node.xpath('./td[2]/text()').extract_first()
            item['level'] = node.xpath('./td[3]/span/text()').extract_first()
            item['PM2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['PM10'] = node.xpath('./td[5]/text()').extract_first()
            item['SO2'] = node.xpath('./td[6]/text()').extract_first()
            item['CO'] = node.xpath('./td[7]/text()').extract_first()
            item['NO2'] = node.xpath('./td[8]/text()').extract_first()
            item['O3'] = node.xpath('./td[9]/text()').extract_first()
            yield item











