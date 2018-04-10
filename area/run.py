'''
auth:hexl
'''
from area.spiders.weather import WeatherSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 获取settings.py模块的设置
settings = get_project_settings()
process = CrawlerProcess(settings=settings)

#添加spider
process.crawl(WeatherSpider)
#启动spider
process.start()