# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exporters import CsvItemExporter

from area.items import AreaItem

import pymysql

class AreaPipeline(object):
    def open_spider(self, spider):
        self.filename = open("area.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.filename.write(content)
        return item

    def close_spider(self, spider):
        self.filename.close()


class AreaMysqlPipeline(object):
    # def process_item(self, item, spider):
    def open_spider(self, spider):
        self.con=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ljj',
                                 use_unicode=True, charset='utf8')
        self.cursor=self.con.cursor()

    def process_item(self, item, spider):
        if isinstance(item, AreaItem):
            # insert_sql='''INSERT INTO area(TITLE, AREA, PRICE, RENT_METHOD, ADDRESS, URL) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}')'''.format(
            #     item['date'], item['city'], item['AQI'], item['level'], item['PM2_5'], item['PM10'],item['SO2'],item['CO'],item['NO2'],item['O3'])
        # else:
            try:
                insert_sql = '''INSERT INTO area(DATE,CITY,AQI,LEVEL,PM2_5,PM10,SO2,CO,NO2,O3) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}')'''.format(item['date'], item['city'], item['AQI'], item['level'], item['PM2_5'], item['PM10'], item['SO2'],item['CO'], item['NO2'], item['O3'])
                self.cursor.execute(insert_sql)  # 执行sql语句
                self.con.commit()  # 提交到数据库，insert和updata语句必须执行这句
            except Exception as e:
                print(e)
            return item

    def close_spider(self, spider):
        self.con.close()




# class AreaPipeline(object):
#     def process_item(self, item, spider):
#          with open("area.json",'w') as f:
#             content = json.dumps(dict(item),ensure_ascii=False) + "\n"
#             f.write(content)
#             return item
#     # def write_json(self,item,spider):
#     #     with open("area.json",'w') as f:
#     #         content = json.dumps(dict(item),ensure_ascii=False) + "\n"
#     #         f.write(content)
#     #         return item
# class AreaCsvPipeline(object):
#     def open_spider(self,spider):
#         self.file = open("aqi.csv", "w")
#         # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
#         self.csv_exporter = CsvItemExporter(self.file)
#         # 表示开始进行数据写入
#         self.csv_exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         self.csv_exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         # 表示结束数据写入
#         self.csv_exporter.finish_exporting()
#         self.file.close()