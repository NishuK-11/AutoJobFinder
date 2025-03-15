import scrapy

class IndeedSpider(scrapy.Spider):
    name = "indeed"
    start_urls =["https://in.indeed.com/jobs?q=full+time&l=&radius=100&from=searchOnDesktopSerp&cf-turnstile-response=0.PY2mpaDTq65w4hAySn4oN3HP8IN4Maa2eEXkQFSc8rnRf34s4pBMfn08ElLYTzz3eKg7h7vc7XHlWmsDNjGiJH9eWjfJUiAthf_cXfmbvru7zouUEeohv08M7WUTlpBCrFRje4if5HhVuZ5mSQ6Sl-uin4IAtkA7rZQ3vAJVzFFkGB1-ZHcWRlzGML7yOfsWTNHj9krHL3gtgT2MI3s5p_E5rMKby1Xunp3MUTBOZOjn7wQsZa17cYi27DmrnbjQxIcPqdUZD3LYi4j1NaJDB9ydfHcHyRSQlmmPvrTmqQ8B-g3YtNg3eJ4-1tRb3QEfY1PWCY1gOCWWJtxdr3BXml3xriWIeFC7yVuIK4jKn5G1_gDSDYg3c9UIUPgAjUxeTdbdqlDUbDkZspuCInD4C0T9W4o06DOSHh_zgsl4DFztTDkgsVfdFloo0x_S88fwmSmyYK7svCrBl1PyDTElCuVhUsLtOYEcYKsDjjjC-kaLARyES7VlsvKj5sB8WpCIXsNmY-28vaB6jaMKfeecc-kwcLJJ7egpvQom6jQBPnDcE2EypYCjc6IfBt2T5b3PXcLUyxtWhH9tdRT0l0HMIrRlMeaYZvjBopZcKg8Pcu06GY9kdjZ9uuREAS42KW-2HpCqoCJmw1GjUc8srpt3HLh7TRs2XGmvQt1Rg84esVBZfP-K-Yf522qhWe_HvEp9hpo5v2ioXfaVOlZsNfR43BLod8IoXfm_RC0MHXHRomuDgW7sB7iuvUjziHfgsMlRuJMfL5ny-2fEycH126OGSZpOugktgfw7S_j5N-8KY7ci4-e0xJgI7Z2ROaJ0vcyx964r8RF-m5uGV7jXbOIxmpTa2T4xLnBQtOz1i1CVzMvUKKhAnjuB1nHGjZMVlmh9.7Jb0H3NPoiw_LFb9unv7mA.f82917353ca1359871fc5f8725468512404d323aefb395dd94c6bf63172fc288&vjk=3478195419240c9c"]

    def parse(self, response):
        print("hello!")
        try:

            company_name = response.xpath('').extract()
        except Exception as e:
            print("error is : ",e)

