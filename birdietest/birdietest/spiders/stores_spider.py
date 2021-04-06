from scrapy import Request
from scrapy import Spider
# from .. import items

# scrapy crawl storespider -a filename=minioffers.csv -o items.json -t json
# scrapy crawl storespider -a filename=minioffers.csv -O minioutput.json
# pip freeze > requirements.txt


class StoreSpider(Spider):
    name = 'storespider'
    start_urls = []

#    handle_httpstatus_list = [301, 302]

    def __init__(self, filename=None, **kwargs):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = [url.rstrip('\n') for url in f.readlines()]

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.90 Safari/537.36 '
        }
        for url in self.start_urls:
            yield Request(url, headers=headers)

    def parse(self, response, **kwargs):
        """
        web scrapping without items library
        """
        if "mercadolivre.com.br" in response.url:
            if response.css('h1.ui-pdp-title::text').get():
                if response.css('span.price-tag-fraction::text').get():
                    yield {
                        'product': response.css('h1.ui-pdp-title::text').get().strip(),
                        'price': response.css('span.price-tag-fraction::text').get().strip(),
                        'product-status': 'Available',
                        'store': 'Mercado Livre',
                        'request-status': response.status,
                        'link': response.url,
                    }

            #     else:
            #         yield {
            #             'product': response.css('h1.ui-pdp-title::text').get().strip(),
            #             'price': 'None',
            #             'product-status': 'Sold Out',
            #             'store': 'Mercado Livre',
            #             'request-status': response.status,
            #             'link': response.url,
            #         }
            #
            # else:
            #     yield {
            #         'product': 'None',
            #         'price': 'None',
            #         'product-status': 'Not Available',
            #         'store': 'Mercado Livre',
            #         'request-status': response.status,
            #         'link': response.url,
            #     }

        elif "casasbahia.com.br" in response.url:
            pass
            # if response.css('h1.css-rfo7gs.eym5xli0::text').get():
            #     if response.css('span.product-price-value::text').get():
            #         yield {
            #             'product': response.css('h1.css-rfo7gs.eym5xli0::text').get().strip(),
            #             'price': response.css('span.product-price-value::text').get().replace("R$&nbsp;", "").strip(),
            #             'product-status': 'Available',
            #             'store': 'Casas Bahia',
            #             'request-status': response.status,
            #             'link': response.url,
            #         }
            #     else:
            #         yield {
            #             'product': response.css('h1.css-rfo7gs eym5xli0::text').get().strip(),
            #             'price': 'None',
            #             'product-status': 'Sold Out',
            #             'store': 'Casas Bahia',
            #             'request-status': response.status,
            #             'link': response.url,
            #         }
            # else:
            #     yield {
            #         'product': 'None',
            #         'price': 'None',
            #         'product-status': 'Not Available',
            #        'store': 'Casas Bahia',
            #         'request-status': response.status,
            #         'link': response.url,
            #     }

        elif "magazineluiza.com.br" in response.url:
            if response.css('h1.header-product__title::text').get():
                if response.css('span.price-template__text::text').get():
                    yield {
                        'product': response.css('h1.header-product__title::text').get().strip(),
                        'price': response.css('span.price-template__text::text').get().strip(),
                        'product-status': 'Available',
                        'store': 'Magazine Luiza',
                        'request-status': response.status,
                        'link': response.url,
                    }
            #     else:
            #         yield {
            #             'product': response.css('h1.header-product__title::text').get().strip(),
            #             'price': 'None',
            #             'product-status': 'Sold Out',
            #             'store': 'Magazine Luiza',
            #             'request-status': response.status,
            #             'link': response.url,
            #         }
            #
            # elif response.css('h1.header-product__title--unavailable::text').get():
            #     yield {
            #         'product': response.css('h1.header-product__title--unavailable::text').get().strip(),
            #         'price': 'None',
            #         'product-status': 'Not Available',
            #         'store': 'Magazine Luiza',
            #         'request-status': response.status,
            #         'link': response.url,
            #     }
            #
            # else:
            #     yield {
            #         'product': 'None',
            #         'price': 'None',
            #         'product-status': 'Not Available',
            #         'store': 'Magazine Luiza',
            #         'request-status': response.status,
            #         'link': response.url,
            #     }

        """
        webscrapping using items library
        """

        # if "mercadolivre.com.br" in response.url:
        #     if response.css('h1.ui-pdp-title::text').get():
        #         if response.css('span.price-tag-fraction::text').get():
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.ui-pdp-title::text').get().strip()
        #             item['price'] = response.css('span.price-tag-fraction::text').get().strip()
        #             item['product-status'] = 'Available'
        #             item['store'] = 'Mercado Livre'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #
        #         else:
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.ui-pdp-title::text').get().strip()
        #             item['price'] = 'None'
        #             item['product-status'] = 'Sold Out'
        #             item['store'] = 'Mercado Livre'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #
        #     else:
        #         item = items.StoresItem()
        #         item['product'] = 'None'
        #         item['price'] = 'None'
        #         item['product-status'] = 'Not Available'
        #         item['store'] = 'Mercado Livre'
        #         item['request-status'] = response.status
        #         item['link'] = response.url
        #         yield item
        #
        # elif "casasbahia.com.br" in response.url:
        #     if response.css('h1.css-rfo7gs.eym5xli0::text').get():
        #         if response.css('span.product-price-value::text').get():
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.css-rfo7gs.eym5xli0::text').get().strip()
        #             item['price'] = response.css('span.product-price-value::text').get().replace("R$&nbsp;", "").strip()
        #             item['product-status'] = 'Available'
        #             item['store'] = 'Casas Bahia'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #
        #         else:
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.css-rfo7gs eym5xli0::text').get().strip()
        #             item['price'] = 'None'
        #             item['product-status'] = 'Sold Out'
        #             item['store'] = 'Casas Bahia'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #     else:
        #         item = items.StoresItem()
        #         item['product'] = 'None'
        #         item['price'] = 'None'
        #         item['product-status'] = 'Not Available'
        #         item['store'] = 'Casas Bahia'
        #         item['request-status'] = response.status
        #         item['link'] = response.url
        #         yield item
        #
        # elif "magazineluiza.com.br" in response.url:
        #     if response.css('h1.header-product__title::text').get():
        #         if response.css('span.price-template__text::text').get():
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.header-product__title::text').get().strip()
        #             item['price'] = response.css('span.price-template__text::text').get().strip()
        #             item['product-status'] = 'Available'
        #             item['store'] = 'Magazine Luiza'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #         else:
        #             item = items.StoresItem()
        #             item['product'] = response.css('h1.header-product__title::text').get().strip()
        #             item['price'] = 'None'
        #             item['product-status'] = 'Sold Out'
        #             item['store'] = 'Magazine Luiza'
        #             item['request-status'] = response.status
        #             item['link'] = response.url
        #             yield item
        #
        #     elif response.css('h1.header-product__title--unavailable::text').get():
        #         item = items.StoresItem()
        #         item['product'] = response.css('h1.header-product__title--unavailable::text').get().strip()
        #         item['price'] = 'None'
        #         item['product-status'] = 'Not Available'
        #         item['store'] = 'Magazine Luiza'
        #         item['request-status'] = response.status
        #         item['link'] = response.url
        #         yield item
        #
        #     else:
        #         item = items.StoresItem()
        #         item['product'] = 'None'
        #         item['price'] = 'None'
        #         item['product-status'] = 'Not Available'
        #         item['store'] = 'Magazine Luiza'
        #         item['request-status'] = response.status
        #         item['link'] = response.url
        #         yield item