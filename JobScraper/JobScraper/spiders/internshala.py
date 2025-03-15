
import scrapy
from properties.p import Property


class InternshalaSpider(scrapy.Spider):
    name = "internshala"
    prop = Property()
    p = prop.load_property('properties/internshala.properties')
    url1 = p.get('START_URL1')
    url2 = p.get('START_URL2')
    print("url =",url1)


    start_urls = [
        url1,
        url2
    ]



    def parse(self, response):

        print("here.")