# -*- coding: utf-8 -*-
import scrapy
import time
import json
from ..items import TencentjobItem


class TencentjobSpider(scrapy.Spider):
    name = 'tencentJob'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1558510109687&countryId=&cityId='
                  '&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10'
                  '&language=zh-cn&area=cn']
    timestamp = round(time.time() * 1000)
    pg_size = 10

    def parse(self, response):
        res = json.loads(response.text)
        job_num = res["Data"]["Count"] # 获取职位总数
        all_pg_num = int(job_num)//10 + 1 # 页面数
        for pg_num in range(1, all_pg_num + 1):
            list_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={0}&countryId=&cityId=' \
                       '&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={1}' \
                       '&pageSize={2}&language=zh-cn&area=cn'.format(self.timestamp, pg_num, self.pg_size)
            yield scrapy.Request(list_url, callback=self.parse_list_html)

    # 解析每页列表
    def parse_list_html(self, response):
        infos = json.loads(response.text)["Data"]["Posts"]
        for info in infos:
            PostID = info["PostId"]
            job_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp={0}&postId={1}&' \
                      'language=zh-cn'.format(self.timestamp, PostID)
            yield scrapy.Request(job_url, callback=self.parse_jog_html)

    # 抓取职位信息
    def parse_jog_html(self, response):
        item = TencentjobItem()
        job_info = json.loads(response.text)["Data"]
        item["RecruitPostName"] = job_info["RecruitPostName"]
        item["BGName"] = job_info["BGName"]
        item["LocationName"] = job_info["LocationName"]
        item["CategoryName"] = job_info["CategoryName"]
        item["LastUpdateTime"] = job_info["LastUpdateTime"]
        item["Responsibility"] = job_info["Responsibility"]
        item["Requirement"] = job_info["Requirement"]
        yield item        
        
        
    
        













