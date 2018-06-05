import scrapy
import json
from spiderMan.items import DmozItem

class StockingsSpider(scrapy.Spider):
	name="stocking"
	allowed_domains=["www.gq.com.cn"]
	start_urls=["http://www.gq.com.cn/tag/14428/t2.html"]

	
	def parse(self,response):
		print response.body
		for sel in response.xpath('//ul/li'):
			item=DmozItem()
			title=sel.xpath('a/text()').extract()
			link=sel.xpath('a/@href').extract()
			desc=sel.xpath('text()').extract()
			item['title'] =title
			item['link'] = link
			item['desc'] = desc
			#print json.dumps(item['title']), json.dumps(item['link']), json.dumps(item['desc'])
			yield item
		
			