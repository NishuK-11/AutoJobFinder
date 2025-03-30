
import scrapy
from ..items import JobscraperItem


class IndeedSpider(scrapy.Spider):
    name = "indeed"
    base_url = 'https://in.indeed.com'
    #all jobs india based on work from home
    url1 = 'https://in.indeed.com/jobs?q=work+from+home&l=India&forceLocation=1&from=searchOnDesktopSerp&cf-turnstile-response=0.LC1C48AE_OplIqwWMBbMDkQwuN3FPaf_FyxoxE1NnnPWsBahry3IPeBARn7dTXq378OMjJKbw3ia2yBI-BKFpRFGnrF4wgCZCNJDuLIuiCpgIXyQDu7JdZE4wdRjzpbeSo_vGEKykKuMIYiEegvfUA4r4NM1za36F-s3iL1OL9am8vNNnz7DJZ2IKsyNh_67Fsf5fd6QbY4t9Q3kciKt_SL00fA29jlTs3l8T7Ryr3umeZe4tRnINo-pQQ4m9aR10PMGuaY9dayeCF4O2-PtSBqtAaH52zQHKHi2PsuyXgrTGDJxCmMv64Tucf0XlnL8xJdr1RxNR3XTUvwyW7lm-IIBCi5aN3zFiGtcArhZuiSN97JmLY5mfZne8O4JdOgI29E6BrBlptKNf_dF3wfiBZzjP8o0ml3S4dwOAM5fvWUYI6RIZpOHfBOO3oXe456PD6CKCJvqwMcq2W3vHk2ON3cqX9HifGIT9_SAev_RLRkWNb0GBPPJLyaKtNtO80jvVwpe_k4-3bHk6ZKqAKorDgRxvfnAvMx6pmzxPL-eg0gOne6P39PIiTPvv3YPgSu0IhHwRIrBC7H_AigYnJzaU3hr72_e5NERRpeZo02OUmkxMdrgbJQtEzHeo-VNnwaxVaUaur-W2SEcNurdmTUruWAX1Wwb5AL4RfgV7HU9iE5mhYWLDjpPalWUJRKOmbr69GzlWNWFR9LEwT6hmRKwpegPikGKeCOipRXL_h3EVGjil5MYWxlXLHgRrBiYkGwjv49thAoKjf9cAd9NH2Nl_rNEarWTdnGLG6z7R-Pht2MyVnlTUbcCkNYB3QQRAgEFj20NcuXHVhX5cu8E3BWEyA.H98wCIfZ4pGzCzWOO8Holg.03c70f75d282316a757014583547bfa67aa4f369d437c85994feb9132118292e&vjk=ff9495b033d18b23'
    start_urls = [
        url1,

    ]

    def parse(self, response):
        print("inside parse.......")
        # totla_pages = 2
        # for i in range(1, totla_pages + 1):
        #     url = response.url + (f'//page-{i}')
        #     yield scrapy.Request(url, callback=self.parse_page)

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
