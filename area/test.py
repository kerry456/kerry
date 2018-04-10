
import pymysql
import time


class AreaMysqlPipeline(object):
    def open_spider(self):
        self.con=pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ljj',
                             use_unicode=True, charset='utf8')
        self.cursor=self.con.cursor()

#
    def process_item(self,):
#         # if isinstance(item, AreaItem):
#             # insert_sql='''INSERT INTO area(TITLE, AREA, PRICE, RENT_METHOD, ADDRESS, URL) VALUES ('{}', '{}', '{}', '{}', '{}', '{}','{}','{}','{}','{}')'''.format(
#             #     item['date'], item['city'], item['AQI'], item['level'], item['PM2_5'], item['PM10'],item['SO2'],item['CO'],item['NO2'],item['O3'])
#             # else:
#         insert_sql='''INSERT INTO AREA VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') ''' % (
        try:
            insert_sql = '''INSERT INTO area(date,city,AQI,level,PM2_5,PM10,SO2,CO,NO2,O3) VALUES('df', 'df', 'AQI', 'level', 'PM2_5','PM10','SO2','CO','NO2','O3')'''
            self.cursor.execute(insert_sql)  # 执行sql语句
            self.con.commit()  # 提交到数据库，insert和updata语句必须执行这句
        except Exception as error:
            print(error)

    def close_spider(self,):
        self.con.close()
if __name__ == '__main__':
    a = AreaMysqlPipeline()
    a.open_spider()
    a.process_item()
    time.sleep(.3)
    a.close_spider()


# 2.插入操作
db=pymysql.connect(host="127.0.0.1", user="root",password="123456", db="ljj", port=3306,use_unicode=True,charset='utf8')

# 使用cursor()方法获取操作游标
# cur=db.cursor()
#
# sql_insert="""INSERT INTO area(date,city,AQI,level,PM2_5,PM10,SO2,CO,NO2,O3) VALUES('df', 'df', 'AQI', 'level', 'PM2_5','PM10','SO2','CO','NO2','O3')"""
#
# try:
#     cur.execute(sql_insert)
#     # 提交
#     db.commit()
# except Exception as e:
#     # 错误回滚
#     db.rollback()
# finally:
#     db.close()

# SELECT * FROM ljj.area;
#
# INSERT INTO area(date,city,AQI,level,PM2_5,PM10,SO2,CO,NO2,O3) VALUES('df', 'df', 'AQI', 'level', 'PM2_5','PM10','SO2','CO','NO2','O3')
#
# truncate table area;
#
# INSERT INTO area(date,city,AQI,level,PM2_5,PM10,SO2,CO,NO2,O3) VALUES('df', 'df', 'AQI', 'level', 'PM2_5','PM10','SO2','CO','NO2','O3')