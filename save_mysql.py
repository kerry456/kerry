#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql
import configparser
import ProxyIP

class MysqlOper:
    def __init__(self,relult_list):
        config = configparser.ConfigParser()
        config.read('db.conf')
        self.host = config['mysql']['HOST']
        self.port = int(config['mysql']['PORT'])
        self.user = config['mysql']['USER']
        self.passwd =config['mysql']['PASSWD']
        self.db = config['mysql']['DB']
        self.table = config['mysql']['TABLE']
        self.charset = config['mysql']['CHARSET']
        self.result_list = relult_list


    def mysql_save(self):
        try:
            DB = pymysql.connect(self.host,self.user,self.passwd,self.db,self.port,charset=self.charset)
            cursor = DB.cursor()
        except Exception as e:
            print("链接失败，请检查配置")
            print(e)
            exit(1)
        cursor.execute('show tables in ljj;')
        tables = cursor.fetchall()
        # print(tables)
        flag = True
        for tab in tables:
            if self.table in tab:
                flag = False
                print("%s表已存在，无需创建！"%self.table)
        # print(flag)
        if flag:
            sql ='''create table pytab (id int unsigned not null primary key auto_increment,protocol varchar(10),content varchar(50))'''
            cursor.execute(sql)
            DB.commit()
        else:
            return 0
        for values in self.result_list:
            for port,cont in values.items():
                try:
                    cursor.execute("insert into pytab(protocol,content) value (%s,%s);",[prot,cont])
                except Exception as e:
                    print("插入失败")

if __name__ == '__main__':
    proxyhelper=ProxyIP.GetProxyIP(50)
    res_pool=proxyhelper.get_ip()
    proxy_ip=proxyhelper.right_proxies(res_pool)
    print(proxy_ip)
    DBopener = MysqlOper(proxy_ip)
    DBopener.mysql_save()


