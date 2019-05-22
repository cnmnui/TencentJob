# -*- coding: utf-8 -*-
import csv


# 保存数据到csv
class TencentjobPipeline(object):
    def process_item(self, item, spider):
        with open('ooo.csv', "a", newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            content = [item['RecruitPostName'], item["BGName"], item["LocationName"], 
                       item["CategoryName"], item["LastUpdateTime"], item["Responsibility"],
                       item["Requirement"]]
            writer.writerow(content)
