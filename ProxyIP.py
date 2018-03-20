#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
import requests
from lxml import etree
import time
from bs4 import BeautifulSoup


class GetProxyIP:
    def __init__(self,page=10):
        self.page =page
        self.base_url = 'http://www.xicidaili.com/wt/'
    def get_ip(self):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
        #建立代理IP池，方便之后获取到的ip存储
        res_pool = []
        for pagenum in range(1,self.page):
            url = self.base_url + str(pagenum)
            response = requests.get(url,headers=headers,timeout=3)
            html = response.text
            print(html)
        #     soup = BeautifulSoup(html,'lxml')
        #     soup_tr = soup.find_all('tr')
        #     for item in soup_tr:
        #         try:
        #             soup_td = item.find_all('td')
        #             # print(soup_td[2].text)
        #             res_pool.append(soup_td[5].text.lower() + '://' + soup_td[1].text + ':' + soup_td[2].text)
        #             # q = res_pool.append(soup_td[1].text.lower() + '://' + soup_td[2])
        #             # print(q)
        #         except IndexError:
        #             pass
        # return res_pool
        # print(res_pool)
            # print(soup_tr)
            # print(html)
            # selectot = etree.HTML(html)
            # ipaddr = selectot.xpath('//*[@id="ip_list"]/tbody/tr/td[2]/text()')
    def right_proxies(self,res_pool):
        right_pool = []
        for ip in res_pool:
            if 'https' in ip:
                proxies = {'http':ip}
            else:
                proxies = {'http':ip}
            check_urllist = ['http://www.baidu.com', 'http://www.taobao.com', 'https://cloud.tencent.com/']
            try:
                respon = requests.get(random.choices(check_urllist),proxies=proxies,timeout=1)
                if respon.status_code == 200:
                    right_pool.append(proxies)
                    print('Add: %s'% proxies)
            except Exception as e:
                continue
        # print(res_pool)
        return res_pool

if __name__ == '__main__':
    Proxy = GetProxyIP(10)
    res_pool = Proxy.get_ip()
    # proxy_ip = Proxy.right_proxies(res_pool)
    # print(proxy_ip)
    time.sleep(0.5)


# http://blog.51cto.com/kaliarch/2083997?cid=700494#700494
