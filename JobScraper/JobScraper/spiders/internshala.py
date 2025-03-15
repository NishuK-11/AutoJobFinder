
import scrapy
from ..items import JobscraperItem


class InternshalaSpider(scrapy.Spider):
    name = "internshala"
    base_url = 'https://internshala.com'
    url1 = 'https://internshala.com/internships'
    url2 = 'https://internshala.com/jobs'
    start_urls = [
        url1,
        url2
    ]



    def parse(self, response):
        totla_pages = 2
        for i in range(1, totla_pages + 1):
            url = response.url + (f'//page-{i}')
            yield scrapy.Request(url, callback=self.parse_page)

    def parse_page(self, response):
        posts = response.xpath('//div[@class="internship_meta duration_meta"]')
        for post in posts:
            job_item = JobscraperItem()
            try:
                job_item['role'] = post.xpath('.//a/text()').extract_first()
                print("role= ", job_item['role'])
                job_item['company_name'] = post.xpath('.//p[@class="company-name"]//text()').extract_first().strip()
                job_item['location'] = post.xpath('.//div[@class="row-1-item locations"]//span//a//text()').extract_first()
                job_item['stipned'] = post.xpath('.//span[@class="stipend"]//text()').extract_first()
                job_item['duartion'] = post.xpath('.//i[@class="ic-16-calendar"]//following-sibling::span//text()').extract_first()
                job_item['post_link'] = self.base_url + post.xpath('.//a/@href').extract_first()
            except Exception as e:
                print("Error = ", e)
            yield job_item
