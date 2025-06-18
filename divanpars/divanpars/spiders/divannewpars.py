import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        divans = response.css('div.LlPhw') # LlPhw NUHc1
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(), # CE4Nr
                'price': divan.css('div.pY3d2 span::text').get(), # sR_jI
                'url': divan.css('a').attrib['href']
            }
