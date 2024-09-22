import scrapy
from pathlib import Path
import json
from utils import timestamp


class PeoplePerHourSpider(scrapy.Spider):
    name = "people_per_hour"
    allowed_domains = ["www.peopleperhour.com"]
    # start_urls = ["https://www.peopleperhour.com/freelance-jobs"]
    def start_requests(self):
        for page in range(1, 78):
            yield scrapy.Request(f"https://www.peopleperhour.com/freelance-jobs?page={page}", self.parse)

    def parse(self, response):
        self.log(f"@@@ Url {response.url}")
        page = response.url.split("=")[-1]
        filename = f"../output/page-{page}-{timestamp()}.json"
        data = []
        containers = response.xpath(
            '//li[contains(@class, "list__item⤍List")]')
        for container in containers:
            data_item = {
                'username': container.xpath('.//span[contains(@class, "card__username")]/text()').getall()[1].strip(),
                'profile_url': container.xpath('.//a[contains(@class, "card__user-link")]/@href').get(),
                'price': container.xpath('.//div[contains(@class, "card__price")]//span/text()').get().strip(),
                'job_type': container.xpath('.//span[contains(@class, "etiquettes")]/text()').get(),
                'job_title': container.xpath('.//h6[contains(@class, "item__title")]/a/text()').get(),
                'job_url': container.xpath('.//h6[contains(@class, "item__title")]/a/@href').get(),
                'description': container.xpath('.//p[contains(@class, "item__desc")]/text()').get().strip(),
                'posted_time': container.xpath('.//div[contains(@class, "card__footer-left")]/span[1]/text()').get(),
                'num_proposals': container.xpath('.//div[contains(@class, "card__footer-left")]/span[2]/text()').get(),
                'location': container.xpath('.//div[contains(@class, "card__footer-left")]/span/span/text()').get()
            }

            data.append(data_item)

        with open(filename, 'w') as fp:
            json.dump(data, fp)
        self.log(f"@@@ Saved file {filename}")
