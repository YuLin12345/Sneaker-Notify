# -*- coding: utf-8 -*-

# Sneaker Notify
# author - Yu Lin
# https://github.com/yulin12345
# admin@yulin12345.site

import logging

from colorama import Fore, Style, init
from scrapy import Spider
from scrapy.crawler import CrawlerProcess
from scrapy.exceptions import CloseSpider, DropItem
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.settings import Settings
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings

from items import *
import settings as settings


# Crawling URLs.
KithURL = "https://kith.com/collections/footwear/sneaker?page=1&sort_by=created-descending"
RuvillaURL = "https://www.ruvilla.com/men/footwear.html?dir=desc&limit=15&order=news_from_date&p=1"
FootShopURL = "https://www.footshop.com/en/5-mens-shoes/brand-adidas_originals-adidas_running-jordan-nike/page-1"
AfewURL = "https://www.afew-store.com/en/sneaker/nike_air-jordan_adidas/?limit=24&p=1"
CalirootsURL = "https://caliroots.com/mens-sneakers/s/19/1?p=94509&p=222765&p=100518&p=98890&orderBy=Published"
EinhalbURL = "http://www.43einhalb.com/en/sneaker/filter/__brand_nike.adidas/page/1/sort/date_new/perpage/24"
EndURL = "https://www.endclothing.com/us/footwear?p=1&brand=767-769-387963-485046-266802-393359-158-47923-48457-339915-494498-526966-560129-266506&dir=desc&order=position"
SNSURL = "http://www.sneakersnstuff.com/en/2/sneakers/1?p=813&p=5954&p=1046&orderBy=Published"
TintURL = "http://www.tint-footwear.com/shoes?dir=desc&limit=16&order=news_from_date&p=1"
OverkillURL = "https://www.overkillshop.com/en/sneaker/filter/manufacturer-nike-adidas-jordan.html?dir=desc&limit=36&order=category_sorting&p=1"
FootDistrictURL = "https://footdistrict.com/en/sneakers/latest/where/marca/adidas_jordan_nike/p/1/order/position/dir/desc/limit/12.html"
SizeURL = "https://www.size.co.uk/mens/footwear/brand/nike,adidas-originals,adidas,nike-sb,jordan/latest/?from=0"
YCMCURL = "http://www.ycmc.com/men/shoes/sneakers.html?dir=desc&order=new_arrivals&p=1&warm=1"
CityURL = "http://www.citygear.com/catalog/shoes/brand/nike-adidas-jordan/sort-by/news_from_date/sort-direction/desc.html"
FootLockerURL = "http://m.footlocker.com/?uri=search&Nao=0&Rpp=20&N=991+76"
FootActionURL = "http://m.footaction.com/?uri=search&Nao=0&Rpp=20&N=991+76"
ChampsURL = "http://m.champssports.com/?uri=search&Nao=0&Rpp=20&N=991+76"
EastBayURL = "http://m.eastbay.com/?uri=search&Nao=0&Rpp=20&N=61+842"
FinishLineURL = "http://www.finishline.com/store/men/shoes/nike/jordan/adidas/_/N-1737dkjZhtjl46Zvnhst2?mnid=men_shoes#/store/men/shoes/nike/jordan/adidas/_/N-1737dkjZhtjl46Zvnhst2Zh51uar?mnid=men_shoes_nike_jordan_adidas&No=0"
AdidasURL = "http://www.adidas.com/us/men-shoes1-shoes?srule=newest-to-oldest&sz=48&start=0"
NikeURL = "http://store.nike.com/us/en_us/pw/mens-jordan-shoes/7puZonnZoi3?sortOrder=publishdate|desc"
NordstromURL = "http://shop.nordstrom.com/c/mens-sneakers?top=12&sort=Newest&page=1"
BarneysURL = "http://www.barneys.com/category/men/shoes/adidas/N-13x4l33Z11mt8ibZ1ltz1sdZ7i1mmyZ15aqac?page=1&recordsPerPage=48"
JimmyJazzURL = "http://www.jimmyjazz.com/mens/footwear?sort=most-recent&ppg=52&page=1"
JDSportsURL = "https://www.jdsports.co.uk/men/mens-footwear/brand/adidas-originals,nike,adidas,nike-sb,jordan/latest/?from=0"
FootPatrolURL = "http://www.footpatrol.co.uk/footwear/br:adidas,adidas-consortium,adidas-originals,adidas-raf-simons,adidas-spezial,jordan,nike,nikelab/?order_by=1"
SneakerPoliticsURL = "http://sneakerpolitics.com/collections/sneakers?page=1"
UrbanIndustryURL = "https://www.urbanindustry.co.uk/collections/shoes?page=1&sort_by=created-descending"
SneakerBaasURL = "http://www.sneakerbaas.com/uk/mens.html?brands=adidas,jordan,nike,nike-skate-boarding&p=1"
UrbanOutfittersURL = "http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=M_SHOES_SNEAKERS&cm_sp=MENS-_-L3-_-MENS_SHOES:M_SHOES_SNEAKERS&brand=adidas&sortBy=--newexpirationdate#/"
LuisaURL = "https://www.luisaviaroma.com/men/catalog/shoes/sneakers/lang_EN/lineid_4/catid_97?FilterDes=4R8,140,210,DNR,VL1,DMS,W8H,3HU,VW5&Page=1&SortType=NewIn"
SlamJamURL = "https://www.slamjamsocialism.com/footwear/#/manufacturer-adidas_by_raf_simons-adidas_consortium-adidas_originals-nike-nike_gyakusou-nike_special_project/page-1"
Rise45URL = "https://rise45.com/collections/mens-footwear"
UndefeatedURL = "http://undefeated.com/footwear"
ZapposURL = "http://www.zappos.com/men-shoes/CK_XAcABAuICAgEY.zso?s=isNew/desc/goLiveDate/desc/recentSalesStyle/desc/"
PointzURL = "https://www.5pointz.co.uk/footwear?brand=510_486_493&dir=desc&order=release_date"
StickABushURL = "https://www.stickabush.com/sneaker.html?limit=18&p=1"
ShoesPalaceURL = "http://www.shoepalace.com/men/footwear/shoes/?limit=24&order=created_at&p=1"
KongURL = "http://www.kongonline.co.uk/collections/footwear?page=1&sort_by=created-descending"
SaveOurSoleURL = "https://www.saveoursole.de/en/sneaker/?p=1&o=1&n=12"
InflammableURL = "http://www.inflammable.com/en/sneaker/?&perPage=30&page=1"
DefShopURL = "https://en.def-shop.com/men/sneakers/?page=1&rf=1"
OffspringURL = "http://www.offspring.co.uk/view/category/offspring_catalog/1?page=1&pageSize=24&sort=releaseDate"
SoleKitchenURL = "http://www.solekitchen.de/en/sneaker/?p=1&o=1"
DromeURL = "http://www.drome.co.uk/footwear/?old_expand=2&brand=BR_AA&brand=BR_NN&brand=BR_JORD&display=grid4&order=NEW+PRODUCTS&expand=1"
FootAsylumURL = "https://www.footasylum.com/mens-footwear/?brand=BR_AA&brand=BR_NN&brand=BR_JORD&order=NEW+PRODUCTS&page=1"


init()


configure_logging(install_root_handler=False)
logging.basicConfig(filename='log.txt', format='%(levelname)s: %(message)s', level=logging.INFO)
logging.disable(logging.INFO)


class KithSpider(Spider):
    
    name = "KithSpider"
    allowded_domains = ["kith.com"]
    start_urls = [KithURL]

    def __init__(self):
        logging.critical("KithSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class=" grid__item large-up--one-third medium--one-half "]')
        
        for product in products:
            item = KithItem()
            item['name'] = product.xpath('div/a[1]/img/@alt').extract()[0]
            item['link'] = "https://kith.com" + product.xpath('div/a[1]/@href').extract()[0]
            item['image'] = "https:" + product.xpath('div/a[1]/img/@src').extract()[0]
            yield item
            
        yield Request(KithURL, callback=self.parse, dont_filter=True)

        
class RuvillaSpider(Spider):
    
    name = "RuvillaSpider"
    allowded_domains = ["ruvilla.com"]
    start_urls = [RuvillaURL]

    def __init__(self):
        logging.critical("RuvillaSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//ul//li[contains(@class," item")]')
        
        for product in products:
            item = RuvillaItem()
            item['name'] = product.xpath('div/div[1]/a/@title').extract()[0]
            item['link'] = product.xpath('div/div[1]/a/@href').extract()[0]
            # item['image'] = product.xpath('div/div[1]/a/img/@src').extract()[0]
            yield item
            
        yield Request(RuvillaURL, callback=self.parse, dont_filter=True)

        
class FootShopSpider(Spider):
    
    name = "FootShopSpider"
    allowded_domains = ["footshop.com"]
    start_urls = [FootShopURL]

    def __init__(self):
        logging.critical("FootShopSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="col-xs-6 col-md-4 col-lg-3"]')
        
        for product in products:
            item = FootShopItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/div/img/@data-src').extract()[0]
            yield item
            
        yield Request(FootShopURL, callback=self.parse, dont_filter=True)

        
class AfewSpider(Spider):
    
    name = "AfewSpider"
    allowded_domains = ["afew-store.com"]
    start_urls = [AfewURL]

    def __init__(self):
        logging.critical("AfewSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="amshopby-page-container"]//li[contains(@class,"item")]')
        
        for product in products:
            item = AfewItem()
            item['name'] = product.xpath('./h2/a/@title').extract()[0]
            item['link'] = product.xpath('.//h2/a/@href').extract()[0]
            item['image'] = product.xpath('.//div[1]/@base_img').extract()[0]
            yield item
            
        yield Request(AfewURL, callback=self.parse, dont_filter=True)

        
class CalirootsSpider(Spider):
    
    name = "CalirootsSpider"
    allowded_domains = ["caliroots.com"]
    start_urls = [CalirootsURL]

    def __init__(self):
        logging.critical("CalirootsSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product-list row"]//li[contains(@class,"product")]')
        
        for product in products:
            item = CalirootsItem()
            item['name'] = product.xpath('.//a/p[2]/text()').extract()[0]
            item['link'] = "https://caliroots.com" + product.xpath('.//a/@href').extract()[0]
            item['image'] = product.xpath('.//a/div/img/@src').extract()[0]
            yield item
            
        yield Request(CalirootsURL, callback=self.parse, dont_filter=True)

        
class EinhalbSpider(Spider):
    
    name = "EinhalbSpider"
    allowded_domains = ["43einhalb.com"]
    start_urls = [EinhalbURL]

    def __init__(self):
        logging.critical("EinhalbSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="block-grid three-up mobile-two-up productListing"]//li[contains(@class,"item")]')
        
        for product in products:
            item = EinhalbItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = "http://www.43einhalb.com" + product.xpath('.//a/@href').extract()[0]
            item['image'] = product.xpath('.//a/div/img[1]/@data-src').extract()[0]
            yield item
            
        yield Request(EinhalbURL, callback=self.parse, dont_filter=True)

        
class EndSpider(Spider):
    
    name = "EndSpider"
    allowded_domains = ["endclothing.com"]
    start_urls = [EndURL]

    def __init__(self):
        logging.critical("EndSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products listing-type-list catalog-listing"]//div[contains(@class,"thumbnail")]')
        
        for product in products:
            item = EndItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = product.xpath('.//a/@href').extract()[0]
            item['image'] = product.xpath('.//a/img/@src').extract()[0]
            yield item
            
        yield Request(EndURL, callback=self.parse, dont_filter=True)

        
class SNSSpider(Spider):
    
    name = "SNSSpider"
    allowded_domains = ["sneakersnstuff.com"]
    start_urls = [SNSURL]

    def __init__(self):
        logging.critical("SNSSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product-listing"]//li[contains(@class,"product")]')
        
        for product in products:
            item = SNSItem()
            item['name'] = product.xpath('.//div/h4/a/text()').extract()[0]
            item['link'] = "http://www.sneakersnstuff.com" + product.xpath('.//div/h4/a/@href').extract()[0]
            item['image'] = "http://www.sneakersnstuff.com" + product.xpath('.//a/img/@src').extract()[0]
            yield item
            
        yield Request(SNSURL, callback=self.parse, dont_filter=True)

        
class TintSpider(Spider):
    
    name = "TintSpider"
    allowded_domains = ["tint-footwear.com"]
    start_urls = [TintURL]

    def __init__(self):
        logging.critical("TintSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="products-grid arw-4-col arw-row"]//li[contains(@class,"arw-col")]')
        
        for product in products:
            item = TintItem()
            item['name'] = product.xpath('div/div/div[1]/a/@title').extract()[0]
            item['link'] = product.xpath('div/div/div[1]/a/@href').extract()[0]
            item['image'] = product.xpath('div/div/div[1]/a/img/@src').extract()[0]
            yield item
            
        yield Request(TintURL, callback=self.parse, dont_filter=True)

        
class OverkillSpider(Spider):
    
    name = "OverkillSpider"
    allowded_domains = ["overkillshop.com"]
    start_urls = [OverkillURL]

    def __init__(self):
        logging.critical("OverkillSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[contains(@class,"item")]')
        
        for product in products:
            item = OverkillItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            yield item
            
        yield Request(OverkillURL, callback=self.parse, dont_filter=True)

        
class FootDistrictSpider(Spider):
    
    name = "FootDistrictSpider"
    allowded_domains = ["footdistrict.com"]
    start_urls = [FootDistrictURL]

    def __init__(self):
        logging.critical("FootDistrictSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//ul[contains(@class,"products")]')
        
        for product in products:
            item = FootDistrictItem()
            item['name'] = product.xpath('.//li[1]/a[2]/@title').extract()[0]
            item['link'] = product.xpath('.//li[1]/a[2]/@href').extract()[0]
            item['image'] = product.xpath('.//li[1]/a[2]/img/@src').extract()[0]
            yield item
            
        yield Request(FootDistrictURL, callback=self.parse, dont_filter=True)

        
class SizeSpider(Spider):
    
    name = "SizeSpider"
    allowded_domains = ["size.co.uk"]
    start_urls = [SizeURL]

    def __init__(self):
        logging.critical("SizeSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="listProducts productList"]//li[contains(@class,"productListItem")]')
        
        for product in products:
            item = SizeItem()
            item['name'] = product.xpath('.//span/span/span/a/text()').extract()[0]
            item['link'] = "https://www.size.co.uk" + product.xpath('.//span/span/span/a/@href').extract()[0]
            item['image'] = product.xpath('.//span/a/img/@src').extract()[0]
            yield item
            
        yield Request(SizeURL, callback=self.parse, dont_filter=True)

        
class YCMCSpider(Spider):
    
    name = "YCMCSpider"
    allowded_domains = ["ycmc.com"]
    start_urls = [YCMCURL]

    def __init__(self):
        logging.critical("YCMCSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[contains(@class,"item")]')
        
        for product in products:
            item = YCMCItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            yield item
            
        yield Request(YCMCURL, callback=self.parse, dont_filter=True)

        
class CitySpider(Spider):
    
    name = "CitySpider"
    allowded_domains = ["citygear.com"]
    start_urls = [CityURL]

    def __init__(self):
        logging.critical("CitySpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[contains(@class,"item")]')
        
        for product in products:
            item = CityItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = product.xpath('.//a/@href').extract()[0]
            item['image'] = product.xpath('.//a/img/@src').extract()[0]
            yield item
            
        yield Request(CityURL, callback=self.parse, dont_filter=True)

        
class FootLockerSpider(Spider):
    
    name = "FootLockerSpider"
    allowded_domains = ["footlocker.com"]
    start_urls = [FootLockerURL]

    def __init__(self):
        logging.critical("FootLockerSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="merge"]//li[contains(@class,"content_entry")]')
        
        for product in products:
            item = FootLockerItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            yield item
            
        yield Request(FootLockerURL, callback=self.parse, dont_filter=True)

        
class FootActionSpider(Spider):
    
    name = "FootActionSpider"
    allowded_domains = ["footaction.com"]
    start_urls = [FootActionURL]

    def __init__(self):
        logging.critical("FootActionSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="merge"]//li[contains(@class,"content_entry")]')
        
        for product in products:
            item = FootActionItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            yield item
            
        yield Request(FootActionURL, callback=self.parse, dont_filter=True)

        
class ChampsSpider(Spider):
    
    name = "ChampsSpider"
    allowded_domains = ["champssports.com"]
    start_urls = [ChampsURL]

    def __init__(self):
        logging.critical("ChampsSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="merge"]//li[contains(@class,"content_entry")]')
        
        for product in products:
            item = ChampsItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            yield item
            
        yield Request(ChampsURL, callback=self.parse, dont_filter=True)

        
class EastBaySpider(Spider):
    
    name = "EastBaySpider"
    allowded_domains = ["eastbay.com"]
    start_urls = [EastBayURL]

    def __init__(self):
        logging.critical("EastBaySpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="merge"]//li[contains(@class,"content_entry")]')
        
        for product in products:
            item = EastBayItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            yield item
            
        yield Request(EastBayURL, callback=self.parse, dont_filter=True)

        
class FinishLineSpider(Spider):
    
    name = "FinishLineSpider"
    allowded_domains = ["finishline.com"]
    start_urls = [FinishLineURL]

    def __init__(self):
        logging.critical("FinishLineSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="small-block-grid-2 medium-block-grid-3 large-block-grid-4 xlarge-block-grid-5 productGrid "]//li[contains(@class,"noOnModelImage")]')
        
        for product in products:
            item = FinishLineItem()
            item['name'] = product.xpath('.//div/a[2]/div/p/text()').extract()[0]
            item['link'] = "http://www.finishline.com" + product.xpath('.//div/a[1]/@href').extract()[0]
            item['image'] = product.xpath('.//div/a[1]/div/img/@src').extract()[0]
            yield item
            
        yield Request(FinishLineURL, callback=self.parse, dont_filter=True)

        
class AdidasSpider(Spider):
    
    name = "AdidasSpider"
    allowded_domains = ["adidas.com"]
    start_urls = [AdidasURL]

    def __init__(self):
        logging.critical("AdidasSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="hoverable clearfix"]//div[@class="product-tile"]//div[contains(@class,"hockeycard")]')
        
        for product in products:
            item = AdidasItem()
            item['name'] = product.xpath('div[3]/div[3]/a/@data-productname').extract()[0]
            item['link'] = product.xpath('div[3]/div[3]/a/@href').extract()[0]
            item['image'] = product.xpath('div[3]/div[3]/a/img/@data-original').extract()[0]
            yield item
            
        yield Request(AdidasURL, callback=self.parse, dont_filter=True)

        
class NikeSpider(Spider):
    
    name = "NikeSpider"
    allowded_domains = ["nike.com"]
    start_urls = [NikeURL]

    def __init__(self):
        logging.critical("NikeSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="exp-product-wall"]//div[contains(@class,"grid-item fullSize")]')
        
        for product in products:
            item = NikeItem()
            item['name'] = product.xpath('.//div/div/div/div/p[1]/text()').extract()[0]
            item['link'] = product.xpath('.//div/div/div[1]/div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/div/div[1]/div/a/img/@src').extract()[0]
            yield item
            
        yield Request(NikeURL, callback=self.parse, dont_filter=True)
        
        
class NordstromSpider(Spider):
    
    name = "NordstromSpider"
    allowded_domains = ["nordstrom.com"]
    start_urls = [NordstromURL]
    
    def __init__(self):
        logging.critical("NordstromSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="npr-2nqsc npr-result-set npr-promo-slots-0"]//div[@class="npr-pBnj7"]//div[@class="npr-2N57q npr-gallery-item"]//article[@class="npr-ahINh npr-product-module large"]')
        
        for product in products:
            item = NordstromItem()
            item['name'] = product.xpath('.//a/img/@alt').extract()[0]
            item['link'] = "http://shop.nordstrom.com" + product.xpath('.//a/@href').extract()[0]
            item['image'] = product.xpath('.//a/img/@src').extract()[0]
            yield item
            
        yield Request(NordstromURL, callback=self.parse, dont_filter=True)
        
        
class BarneysSpider(Spider):
    
    name = "BarneysSpider"
    allowded_domains = ["barneys.com"]
    start_urls = [BarneysURL]

    def __init__(self):
        logging.critical("BarneysSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product-set clearfix"]//li[contains(@class,"col-md-4")]')
        
        for product in products:
            item = BarneysItem()
            item['name'] = product.xpath('.//div/div/a/img/@title').extract()[0]
            item['link'] = "http://www.barneys.com" + product.xpath('.//div/div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/div/a/img/@src').extract()[0]
            yield item
            
        yield Request(BarneysURL, callback=self.parse, dont_filter=True)
        
        
class JimmyJazzSpider(Spider):
    
    name = "JimmyJazzSpider"
    allowded_domains = ["jimmyjazz.com"]
    start_urls = [JimmyJazzURL]

    def __init__(self):
        logging.critical("JimmyJazzSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product_grid "]//div[contains(@class,"product_grid_item")]')
        
        for product in products:
            item = JimmyJazzItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = "http://www.jimmyjazz.com" + product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            yield item
            
        yield Request(JimmyJazzURL, callback=self.parse, dont_filter=True)

        
class JDSportsSpider(Spider):
    
    name = "JDSportsSpider"
    allowded_domains = ["jdsports.co.uk"]
    start_urls = [JDSportsURL]

    def __init__(self):
        logging.critical("JDSportsSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="listProducts productList"]//li[contains(@class,"productListItem")]')
        
        for product in products:
            item = JDSportsItem()
            item['name'] = product.xpath('.//span/a/img/@title').extract()[0]
            item['link'] = "https://www.jdsports.co.uk" + product.xpath('.//span/a/@href').extract()[0]
            item['image'] = product.xpath('.//span/a/img/@src').extract()[0]
            yield item
            
        yield Request(JDSportsURL, callback=self.parse, dont_filter=True)

        
class FootPatrolSpider(Spider):
    
    name = "FootPatrolSpider"
    allowded_domains = ["footpatrol.co.uk"]
    start_urls = [FootPatrolURL]

    def __init__(self):
        logging.critical("FootPatrolSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="fp-product-list"]//li[contains(@class,"fp-column-quarter")]')
        
        for product in products:
            item = FootPatrolItem()
            item['name'] = product.xpath('.//div/a/img/@alt').extract()[0]
            item['link'] = "http://www.footpatrol.co.uk" + product.xpath('.//div/a/@href').extract()[0]
            item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            yield item

        yield Request(FootPatrolURL, callback=self.parse, dont_filter=True)

        
class SneakerPoliticsSpider(Spider):
    
    name = "SneakerPoliticsSpider"
    allowded_domains = ["sneakerpolitics.com"]
    start_urls = [SneakerPoliticsURL]

    def __init__(self):
        logging.critical("SneakerPoliticsSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="twelve columns"]//div[contains(@class,"four")]')
        
        for product in products:
            item = SneakerPoliticsItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = "http://sneakerpolitics.com" + product.xpath('.//a/@href').extract()[0]
            item['image'] = "http:" + product.xpath('.//a/div/img/@data-src').extract()[0]
            yield item
            
        yield Request(SneakerPoliticsURL, callback=self.parse, dont_filter=True)

        
class UrbanIndustrySpider(Spider):
    
    name = "UrbanIndustrySpider"
    allowded_domains = ["urbanindustry.co.uk"]
    start_urls = [UrbanIndustryURL]

    def __init__(self):
        logging.critical("UrbanIndustrySpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="small-12 columns featured-product"]//div[contains(@class,"product-cell")]')
        
        for product in products:
            item = UrbanIndustryItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "https://www.urbanindustry.co.uk" + product.xpath('a/@href').extract()[0]
            item['image'] = "http:" + product.xpath('div[1]/a/img/@src').extract()[0]
            yield item
            
        yield Request(UrbanIndustryURL, callback=self.parse, dont_filter=True)

        
class SneakerBaasSpider(Spider):
    
    name = "SneakerBaasSpider"
    allowded_domains = ["sneakerbaas.com"]
    start_urls = [SneakerBaasURL]
    
    def __init__(self):
        logging.critical("SneakerBaasSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[contains(@class,"item")]')
        
        for product in products:
            item = SneakerBaasItem()
            item['name'] = product.xpath('.//div/h2/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/h2/a/@href').extract()[0]
            item['image'] = product.xpath('.//a/img/@data-src').extract()[0]
            yield item
            
        yield Request(SneakerBaasURL, callback=self.parse, dont_filter=True)

        
class UrbanOutfittersSpider(Spider):
    
    name = "UrbanOutfittersSpider"
    allowded_domains = ["urbanoutfitters.com"]
    start_urls = [UrbanOutfittersURL]

    def __init__(self):
        logging.critical("UrbanOutfittersSpider STARTED.")
    
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products-slide columns"]//ul[@class="category-products  non-inline-slot "]//li[@class="product"]')
        
        for product in products:
            item = UrbanOutfittersItem()
            item['name'] = product.xpath('div/p[1]/a/img/@alt').extract()[0]
            item['link'] = "http://www.urbanoutfitters.com/urban/catalog/" + product.xpath('div/p[2]/a/@href').extract()[0]
            item['image'] = "http:" + product.xpath('div/p[1]/a/img/@src').extract()[0]
            yield item
            
        yield Request(UrbanOutfittersURL, callback=self.parse, dont_filter=True)

        
class LuisaSpider(Spider):
    
    name = "LuisaSpider"
    allowded_domains = ["luisaviaroma.com"]
    start_urls = [LuisaURL]
    
    def __init__(self):
        logging.critical("LuisaSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="catalog"]//div[contains(@class,"article")]')
        
        for product in products:
            item = LuisaItem()
            item['name'] = product.xpath('.//a/span[1]/span[3]/text()').extract()[0]
            item['link'] = "https://www.luisaviaroma.com" + product.xpath('.//@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/span/span/span/img/@src').extract()[0]
            yield item
            
        yield Request(LuisaURL, callback=self.parse, dont_filter=True)

        
class SlamJamSpider(Spider):
    
    name = "SlamJamSpider"
    allowded_domains = ["slamjamsocialism.com"]
    start_urls = [SlamJamURL]
    
    def __init__(self):
        logging.critical("SlamJamSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product_list grid row packery"]//li[contains(@class,"tooltip")]//div[@class="product-container"]//div[@class="left-block"]//div[@class="product-image-container"]')
        
        for product in products:
            item = SlamJamItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/img/@src').extract()[0]
            yield item
            
        yield Request(SlamJamURL, callback=self.parse, dont_filter=True)

        
class Rise45Spider(Spider):
    
    name = "Rise45Spider"
    allowded_domains = ["rise45.com"]
    start_urls = [Rise45URL ]
    
    def __init__(self):
        logging.critical("Rise45Spider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@id="content"]//div[@class="collection-matrix"]//div[contains(@class,"col")]/div')
        
        for product in products:
            item = Rise45Item()
            item['name'] = product.xpath('a[2]/h4/text()').extract()[0]
            item['link'] = "https://rise45.com" + product.xpath('a[1]/@href').extract()[0]
            item['image'] = "https:" + product.xpath('a[1]/img/@src').extract()[0]
            yield item
            
        yield Request(Rise45URL , callback=self.parse, dont_filter=True)

        
class UndefeatedSpider(Spider):
    
    name = "UndefeatedSpider"
    allowded_domains = ["undefeated.com"]
    start_urls = [UndefeatedURL]
    
    def __init__(self):
        logging.critical("UndefeatedSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="view view-solr view-id-solr view-display-id-solr_grid_footwear grid view-dom-id-d656a32e9a8bc23ef35dadd83510be07"]//div[@class="view-content"]//div[contains(@class,"views-row")]')
        
        for product in products:
            item = UndefeatedItem()
            item['name'] = product.xpath('div[2]/a/text()').extract()[0]
            item['link'] = "http://undefeated.com" + product.xpath('div[1]/a/@href').extract()[0]
            item['image'] = product.xpath('div[1]/a/img/@data-src').extract()[0]
            yield item
            
        yield Request(UndefeatedURL, callback=self.parse, dont_filter=True)
		
		
class ZapposSpider(Spider):
    
    name = "ZapposSpider"
    allowded_domains = ["zappos.com"]
    start_urls = [ZapposURL]
    
    def __init__(self):
        logging.critical("ZapposSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@id="resultWrap"]//div[@id="searchResults"]//a')
        
        for product in products:
            item = ZapposItem()
            item['name'] = product.xpath('img/@alt').extract()[0]
            item['link'] = "http://www.zappos.com" + product.xpath('@href').extract()[0]
            item['image'] = product.xpath('img/@src').extract()[0]
            yield item
            
        yield Request(ZapposURL, callback=self.parse, dont_filter=True)
		
		
class PointzSpider(Spider):
    
    name = "PointzSpider"
    allowded_domains = ["5pointz.co.uk"]
    start_urls = [PointzURL]
    
    def __init__(self):
        logging.critical("PointzSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ol[@class="listing listing--grid"]//li[contains(@class,"listing-item")]//article//figure')
        
        for product in products:
            item = PointzItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/img/@src').extract()[0]
            yield item
            
        yield Request(PointzURL, callback=self.parse, dont_filter=True)
		
		
class StickABushSpider(Spider):
    
    name = "StickABushSpider"
    allowded_domains = ["stickabush.com"]
    start_urls = [StickABushURL]
    
    def __init__(self):
        logging.critical("StickABushSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row product-list grid-mode"]//div[contains(@class,"item")]/div')
		
        for product in products:
            item = StickABushItem()
            item['name'] = product.xpath('a/div/p/text()').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/img/@data-src').extract()[0]
            yield item
            
        yield Request(StickABushURL, callback=self.parse, dont_filter=True)

        
class ShoesPalaceSpider(Spider):

    name = "ShoesPalaceSpider"
    allowded_domains = ["shoepalace.com"]
    start_urls = [ShoesPalaceURL]
    
    def __init__(self):
        logging.critical("ShoesPalaceSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="zero center expandable"]//div[contains(@class,"block")]')
		
        for product in products:
            item = ShoesPalaceItem()
            item['name'] = product.xpath('.//div[2]/text()').extract()[0]
            item['link'] = "http://www.shoepalace.com" + product.xpath('.//a/@href').extract()[0]
            item['image'] = "http://www.shoepalace.com" + product.xpath('.//a/img/@src').extract()[0]
            yield item
			
        yield Request(ShoesPalaceURL, callback=self.parse, dont_filter=True)

        
class KongSpider(Spider):
    
    name = "KongSpider"
    allowded_domains = ["kongonline.co.uk"]
    start_urls = [KongURL]
    
    def __init__(self):
        logging.critical("KongSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="desktop-10 tablet-4 mobile-3"]//div[contains(@class,"product-index")]//div[@class="prod-container"]//div[@class="prod-image"]')
        
        for product in products:
            item = KongItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "http://www.kongonline.co.uk" + product.xpath('a/@href').extract()[0]
            item['image'] = "http:" + product.xpath('a/div/img/@src').extract()[0]
            yield item

        yield Request(KongURL, callback=self.parse, dont_filter=True)
		
		
class SaveOurSoleSpider(Spider):
    
    name = "SaveOurSoleSpider"
    allowded_domains = ["saveoursole.de"]
    start_urls = [SaveOurSoleURL]
    
    def __init__(self):
        logging.critical("SaveOurSoleSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="listing"]//div[contains(@class,"product--box box--minimal")]//div[@class="box--content is--rounded"]//div[@class="product--info"]')
        
        for product in products:
            item = SaveOurSoleItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/span/span/img/@srcset').extract()[0]
            yield item
            
        yield Request(SaveOurSoleURL, callback=self.parse, dont_filter=True)
		
		
class InflammableSpider(Spider):

    name = "InflammableSpider"
    allowded_domains = ["inflammable.com"]
    start_urls = [InflammableURL]
	
    def __init__(self):
        logging.critical("InflammableSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="span10 sidebar-products row"]//div[contains(@class,"span25")]')
		
        for product in products:
            item = InflammableItem()
            item['name'] = product.xpath('div[1]/div[1]/a/img/@title').extract()[0]
            item['link'] = product.xpath('div[1]/div[1]/a/@href').extract()[0]
            item['image'] = "http://www.inflammable.com/" + product.xpath('div[1]/div[1]/a/img/@src').extract()[0]
            yield item
			
        yield Request(InflammableURL, callback=self.parse, dont_filter=True)
		
		
class DefShopSpider(Spider):

    name = "DefShopSpider"
    allowded_domains = ["def-shop.com"]
    start_urls = [DefShopURL]
	
    def __init__(self):
        logging.critical("DefShopSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row def-v-offset3 container-fluid"]//div[contains(@class,"def-col-listing")]//article[@class="prod-article"]//div[@class="bx-wrapper"]')
		
        for product in products:
            item = DefShopItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            item['image'] = product.xpath('a/div/img/@content').extract()[0]
            yield item
			
        yield Request(DefShopURL, callback=self.parse, dont_filter=True)
		
		
class OffspringSpider(Spider):
    
    name = "OffspringSpider"
    allowded_domains = ["offspring.co.uk"]
    start_urls = [OffspringURL]
	
    def __init__(self):
        logging.critical("OffspringSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="productList row"]//ul//li[contains(@class,"col-xs-6")]//div[@class="productList_item"]')
		
        for product in products:
            item = OffSpringItem()
            item['name'] = product.xpath('div[2]/div[1]/a//text()[3]').extract()[0]
            item['link'] = "http://www.offspring.co.uk/view" + product.xpath('div[1]/a/@href').extract()[0]
            # item['image'] = product.xpath('div[1]/a/img/@src').extract()[0]
            yield item
			
        yield Request(OffspringURL, callback=self.parse, dont_filter=True)
		
class SoleKitchenSpider(Spider):

    name = "SoleKitchenSpider"
    allowded_domains = ["SoleKitchen.com"]
    start_urls = [SoleKitchenURL]
	
    def __init__(self):
        logging.critical("SoleKitchenSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="listing--container"]//div[@class="listing"]//div[contains(@class,"product--box")]//div[@class="box--content slktn"]')
		
        for product in products:
            item = SoleKitchenItem()
            item['name'] = product.xpath('div/a/@title').extract()[0]
            item['link'] = product.xpath('div/a/@href').extract()[0]
            # tem['image'] = product.xpath('div/span/div/div/div/a[2]/img/@src').extract()[0]
            yield item
			
        yield Request(SoleKitchenURL, callback=self.parse, dont_filter=True)
        
        
class DromeSpider(Spider):
    
    name = "DromeSpider"
    allowded_domains = ["drome.co.uk"]
    start_urls = [DromeURL]
    
    def __init__(self):
        logging.critical("DromeSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="main-list nogaps row"]//div[contains(@class,"prodlistwrap")]//div[@class="prodlist"]')
        
        for product in products:
            item = DromeItem()
            item['name'] = product.xpath('div[1]/img/@alt').extract()[0]
            item['link'] = "http://www.drome.co.uk" + product.xpath('div[2]/div[2]/a/@href').extract()[0]
            item['image'] = "http://www.drome.co.uk" + product.xpath('div[1]/img/@src').extract()[0]
            yield item
            
        yield Request(DromeURL, callback=self.parse, dont_filter=True)
        
        
class FootAsylumSpider(Spider):

    name = "FootAsylumSpider"
    allowded_domains = ["footasylum.com"]
    start_urls = [FootAsylumURL]
	
    def __init__(self):
        logging.critical("FootAsylumSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="productDataOnPage_inner"]//ul[@class="main-list row"]//li[contains(@class,"left")]')
		
        for product in products:
            item = FootAsylumItem()
            item['name'] = product.xpath('div/span[2]/img/@alt').extract()[0]
            item['link'] = product.xpath('div/span[1]/text()').extract()[0]
            item['image'] = "https://www.footasylum.com" + product.xpath('div/span[2]/img/@data-original').extract()[0]
            yield item
			
        yield Request(FootAsylumURL, callback=self.parse, dont_filter=True)
		
		
crawler_settings = Settings()
crawler_settings.setmodule(settings)
process = CrawlerProcess(settings=crawler_settings)

process.crawl(KithSpider)
process.crawl(RuvillaSpider)
process.crawl(FootShopSpider)
process.crawl(AfewSpider)
process.crawl(CalirootsSpider)
process.crawl(EinhalbSpider)
process.crawl(TintSpider)
process.crawl(OverkillSpider)
process.crawl(FootDistrictSpider)
process.crawl(SizeSpider)
process.crawl(YCMCSpider)
process.crawl(CitySpider)
process.crawl(FootLockerSpider)
process.crawl(FootActionSpider)
process.crawl(ChampsSpider)
process.crawl(EastBaySpider)
process.crawl(AdidasSpider)
process.crawl(NikeSpider)
process.crawl(NordstromSpider)
process.crawl(JDSportsSpider)
process.crawl(FootPatrolSpider)
process.crawl(SneakerPoliticsSpider)
process.crawl(UrbanIndustrySpider)
process.crawl(SneakerBaasSpider)
process.crawl(UrbanOutfittersSpider)
process.crawl(LuisaSpider)
process.crawl(SlamJamSpider)
process.crawl(Rise45Spider)
process.crawl(UndefeatedSpider)
process.crawl(ZapposSpider)
process.crawl(PointzSpider)
process.crawl(StickABushSpider)
process.crawl(KongSpider)
process.crawl(SaveOurSoleSpider)
process.crawl(InflammableSpider)
process.crawl(DefShopSpider)
process.crawl(OffspringSpider)
process.crawl(SoleKitchenSpider)
process.crawl(DromeSpider)
process.crawl(FootAsylumSpider)

# process.crawl(EndSpider)		#Captcha if crawl too much.
# process.crawl(SNSSpider)		#ASN blocked on Vultr via CloudFlare.
# process.crawl(FinishLineSpider)	#Banned on Vultr.
# process.crawl(BarneysSpider)		#Ban if crawl too much.
# process.crawl(JimmyJazzSpider)	#ASN blocked on Vultr via CloudFlare.
# process.crawl(ShoesPalaceSpider)      #Need to disobey robots.txt, if you want to crawl.

process.start()
