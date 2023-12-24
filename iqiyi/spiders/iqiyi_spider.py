import scrapy
from ..items import IqiyiItem
from scrapy import Request
from scrapy.http import HtmlResponse, TextResponse


class IqiyiSpiderSpider(scrapy.Spider):
    name = "iqiyi_spider"
    allowed_domains = ["mesh.if.iqiyi.com"]
    start_urls = ["https://mesh.if.iqiyi.com/"]
    #定义开始请求数据:
    def start_requests(self):
        self.order = 1
        self.tags_list = []
        for page in range(1, 5):
            url = 'https://mesh.if.iqiyi.com/portal/pcw/rankList/comSecRankList?&server=false&page_st=0&tag=-4&category_id=2&date=&pg_num={}'.format(page)
            yield Request(url=url,dont_filter=True)


    def parse(self, response:TextResponse):
        json_data = response.json()
        content_list = json_data['data']['items'][0]['contents']
        # print(content_list)
        #取内容
        for content in content_list:
            iqiyi_list = []
            # print(content)
            iqiyi_item = IqiyiItem()
            #取排名
            iqiyi_item['rank'] = self.order
            #标题
            iqiyi_item['title'] = content['title']
            #取封面
            iqiyi_item['cover'] = content['img']
            #取详描述信息
            iqiyi_item['desc'] = content['desc']
            #获取电视剧标签
            tag_list = content['tags'].strip().split('/')
            #分别获取标签中的发行年份、类型、主演名
            iqiyi_item['year'] = tag_list[-1]
            iqiyi_item['genre'] = tag_list[-2]
            iqiyi_item['actor'] = tag_list[-3]
            #获取该电视剧评分
            iqiyi_item['rating'] = content['mainIndex']
            #获取评分人数
            iqiyi_item['rater'] = content['bulletIndex']
            self.order +=1
            yield iqiyi_item







