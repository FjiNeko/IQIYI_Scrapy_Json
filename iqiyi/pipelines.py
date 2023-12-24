# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from .settings import FEED_EXPORT_FIELDS as title
import pandas as pd
from scrapy import cmdline
# from scrapy.pipelines.files import
import csv

import pandas as pd
class IqiyiPipeline:
    global IqiyiPipeline
    def open_spider(self,spider):
        self.v_name = "爱奇艺电视剧_高分榜"
        self.f = open('tv1.csv'.format(self.v_name), 'w',newline='',encoding='utf-8')
        self.writer = csv.writer(self.f)
        header = ['排行','标题','封面','描述','发行年份','类型','主演','评分','评价人数']
        self.writer.writerow(header)
    def process_item(self, item, spider):
        self.v_name = "爱奇艺电视剧_高分榜"
        print("======================================================")
        print(f"     正在爬取 {self.v_name:^3} 排名为{item['rank']}的信息")
        print("======================主要信息========================")
        print(f"    标题: {item['title']:^3}     ")
        print(f"    类型: {item['genre']:^3}     ")
        print(f"    主演: {item['actor']:^3}     ")
        print(f"    描述: {item['desc'][:18]+(item['desc'][18:] and '...'):^6}     ")
        # [1]
        # [2]
        # print(item)
        # return item
        # data = pd.DataFrame(
        # #     {
        # #         "排名": item['rank'],
        # #         "标题": item['title'],
        # #         "封面": item['cover'],
        # #         "发行年份": item['year'],
        # #         "类型": item['genre'],
        # #         "主演": item['actor'],
        # #         "评分": item['rating'],
        # #         "评价人数": item['rater']
        # #     }
        # # )
        # data.to_csv('shuibian.csv')
        self.writer.writerow([item['title'],item['genre'],item['cover'],item['actor'],item['desc']])
    def close_spider(self, spider):
        self.f.close()




