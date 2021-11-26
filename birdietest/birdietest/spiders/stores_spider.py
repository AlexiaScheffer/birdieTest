from scrapy import Request
from scrapy import Spider
import hashlib

from .. import items

# scrapy crawl storespider -a filename=minioffers.csv
# scrapy crawl storespider -a filename=minioffers.csv -o items.json
# scrapy crawl storespider -a filename=minioffers.csv -O minioutput.json
# pip freeze > requirements.txt


class StoreSpider(Spider):
    name = "storespider"
    start_urls = []

    #     handle_httpstatus_list = [301, 302]

    def __init__(self, filename=None, **kwargs):
        if filename:
            with open(filename, "r") as f:
                self.start_urls = [url.rstrip("\n") for url in f.readlines()]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/89.0.4389.90 Safari/537.36 "
        }
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response, **kwargs):
        """
        webscrapping using items library
        """

        if "mercadolivre" in response.url and (
            response.css("h1.ui-pdp-title::text").get()
            and response.css("span.price-tag-fraction::text").get()
        ):
            item = items.StoresItem()
            item["url"] = response.url
            item["store"] = "Mercado Livre"
            
            get_product = response.css("h1.ui-pdp-title::text").get()
            item["product"] = get_product.strip() if get_product else None
            
            get_price = response.css("span.price-tag-fraction::text").get()
            item["price"] = get_price.strip() if get_price else None
            

            id_product = str(hashlib.sha1(item["product"].encode("utf-8")).hexdigest())
            item["primary_key"] = id_product
            
            get_description = response.xpath(
                "//p[contains(@class, 'ui-pdp-description__content')]/text()"
            ).getall()
            desc = " ".join(get_description)
            description = " ".join(desc.split())
            item["description"] = description

            breadcrumb = list()
            breadcrumb_list = response.xpath(
                "//ol[contains(@class, 'andes-breadcrumb')]/li/a/text()"
            ).getall()
            for bc in breadcrumb_list:
                bc = bc.strip()
                if bc:
                    breadcrumb.append(bc)
            item["breadcrumb"] = breadcrumb

            get_score = response.xpath(
                "//p[contains(@class, 'ui-pdp-reviews__rating__summary__average')]/text()"
            ).get()
            score = get_score.replace(",", ".") if get_score else None
            item["score"] = float(score) if score else None
            get_score_count = response.xpath(
                "//span[contains(@class, 'ui-pdp-review__amount')]/text()"
            ).get()
            
            score_count = get_score_count.replace(" opiniões", "") if get_score_count else None
            item["score_count"] = int(score_count) if score_count else None

            yield item

        elif "magazineluiza" in response.url and (
            response.css("h1.header-product__title::text").get()
            and response.css("span.price-template__text::text").get()
        ):
            item = items.StoresItem()
            item["url"] = response.url
            item["store"] = "Magazine Luiza"

            get_id = response.xpath(
                "//small[contains(@class, 'header-product__code')]/text()"
            ).get()
            id_product = str(hashlib.sha1(get_id.encode("utf-8")).hexdigest())
            item["primary_key"] = id_product
            
            get_product = response.css("h1.header-product__title::text").get()
            item["product"] = get_product.strip() if get_product else None
            
            get_price = response.css("span.price-template__text::text").get()
            item["price"] = get_price.strip() if get_price else None

            get_description = response.xpath("//div[@itemprop='description']/text()").getall()
            desc = " ".join(get_description)
            description = " ".join(desc.split())
            item["description"] = description

            breadcrumb = list()
            breadcrumb_list = response.xpath("//ul[@class='breadcrumb']//a/text()").getall()
            for bc in breadcrumb_list:
                bc = bc.strip()
                if bc:
                    breadcrumb.append(bc)
            item["breadcrumb"] = breadcrumb

            get_score = response.xpath("//span[@class='js-rating-value']/text()").get()
            score = get_score.replace(",", ".") if get_score else None
            item["score"] = float(score) if score else None
            get_score = response.xpath(
                "//div[contains(@class, 'interaction-client__rating-info')]/span[2]/text()"
            ).get()
            score_count = get_score.replace("(", "").replace(")", "")
            item["score_count"] = int(score_count) if score_count else None
            yield item
