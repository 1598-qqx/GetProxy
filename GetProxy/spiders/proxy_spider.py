import scrapy
from ..items import GetproxyItem

class ProxySpiderSpider(scrapy.Spider):
    name = 'proxy_spider'
    allowed_domains = ['ip.jiangxianli.com']
    start_urls = ['https://ip.jiangxianli.com']
    start_info_url = 'https://ip.jiangxianli.com/?page=1'
    base_search_url = 'https://ip.jiangxianli.com/?page='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'Host': 'ip.jiangxianli.com',
        'Referer': 'https://ip.jiangxianli.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    cookie_dict = {'UM_distinctid': '177f73d978125-06c2d4a39d474-53e356a-e1000-177f73d9782853', 'CNZZDATA1278691459': '1103320518-1614759066-https%3A%2F%2Fwww.baidu.com%2F|1614759066', 'Hm_lvt_b72418f3b1d81bbcf8f99e6eb5d4e0c3': '1614760745', 'Hm_lpvt_b72418f3b1d81bbcf8f99e6eb5d4e0c3': '1614762373'}

    def parse(self, response):
        if response.status == 200:
            yield scrapy.Request(self.start_info_url, headers=self.headers,callback=self.parse_free_proxy,cookies=self.cookie_dict)
        else:
            yield from super().start_requests()


    def parse_free_proxy(self, response):
        item = GetproxyItem()
        tr_list = response.xpath('//table[@class="layui-table"]/tbody/tr')
        for tr in tr_list:
            td_lists = tr.xpath('./td')[0:4]
            ip = td_lists[0].xpath('./text()')[0].extract()
            port = td_lists[1].xpath('./text()')[0].extract()
            category = td_lists[2].xpath('./text()')[0].extract()
            schema = td_lists[3].xpath('./text()')[0].extract()
            item['ip'] = ip
            item['port'] = port
            item['category'] = category
            item['scheme'] = schema
            yield item
        for page in range(2, 5):
            next_url = self.base_search_url + str(page)
            self.headers['Referer'] = str(response.url)
            yield scrapy.Request(next_url,callback=self.parse_free_proxy,headers=self.headers,cookies=self.cookie_dict)
