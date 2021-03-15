# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class GetproxyPipeline:
    def open_spider(self, spider):
        self.dict_init = {}

    def process_item(self, item, spider):
        if item['category'] != '透明':
            with open('./proxy/匿名.json', 'ab') as f:
                schema = str(item['scheme']).lower()
                proxy = schema+"://"+item['ip']+":"+item['port']

                self.dict_init['proxy'] = proxy
                self.dict_init['scheme'] = schema
                f.write((str(json.dumps(self.dict_init))+"\n").encode('utf-8'))
        return item
