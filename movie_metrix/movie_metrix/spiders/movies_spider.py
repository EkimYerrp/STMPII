import scrapy
import json

class QuotesSpider(scrapy.Spider):
	name = "movie_metrix"

	def start_requests(self):
		urls = [
		'http://movierepo.spencercodes.com/index.php'
		]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		ids_page = []
		ids_list = response.xpath('//a[contains(@href, "id")]/@href').extract()
		for id_lis in ids_list:
			ids_page.append(id_lis.split("=")[1])		
		json_file = json.dumps(ids_page)
		with open('ids_list.json', 'w', encoding='utf-8') as f:
			json.dump(json_file, f, ensure_ascii=False, indent=4)
	
