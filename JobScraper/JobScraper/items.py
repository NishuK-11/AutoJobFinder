# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    role = scrapy.Field()
    location = scrapy.Field()
    stipned = scrapy.Field()
    salary = scrapy.Field()
    duartion = scrapy.Field()
    post_link = scrapy.Field()
    posted_date = scrapy.Field()
    start_date = scrapy.Field()
    apply_by = scrapy.Field()
    total_applicants = scrapy.Field()
    skills = scrapy.Field()
    openings = scrapy.Field()
    website_link = scrapy.Field()
    job_type = scrapy.Field()
    responsibilities = scrapy.Field()
    about_company = scrapy.Field()
    activities = scrapy.Field()