#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sneaker Notify
# author - Yu Lin
# https://github.com/yulin12345
# admin@yulin12345.site

import logging
import re
import time

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
FootDistrictURL = "https://footdistrict.com/en/sneakers/latest.html?limit=12&p=1"
SizeURL = "https://www.size.co.uk/mens/footwear/brand/nike,adidas-originals,adidas,nike-sb,jordan/latest/?from=0"
YCMCURL = "http://www.ycmc.com/men/shoes/sneakers.html?dir=desc&order=new_arrivals&p=1"
CityURL = "http://www.citygear.com/catalog/shoes/brand/nike-adidas-jordan/sort-by/news_from_date/sort-direction/desc.html"
FootLockerURL = "http://m.footlocker.com/?uri=search&Nao=0&Rpp=20&N=991+76"
FootActionURL = "http://m.footaction.com/?uri=search&Nao=0&Rpp=20&N=991+76"
ChampsURL = "http://m.champssports.com/?uri=search&Nao=0&Rpp=20&N=991+76"
EastBayURL = "http://m.eastbay.com/?uri=search&Nao=0&Rpp=20&N=61+842"
FinishLineURL = "http://www.finishline.com/store/men/shoes/nike/jordan/adidas/_/N-1737dkjZhtjl46Zvnhst2?mnid=men_shoes#/store/men/shoes/nike/jordan/adidas/_/N-1737dkjZhtjl46Zvnhst2Zh51uar?mnid=men_shoes_nike_jordan_adidas&No=0"
AdidasUSURL = "http://www.adidas.com/us/men-athletic_sneakers-shoes?srule=newest-to-oldest&sz=48&start=0"
AdidasEUURL = "http://www.adidas.co.uk/men-shoes?srule=newest-to-oldest&sz=48&start=0"
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
UndefeatedURL = "https://shop.undefeated.com/collections/footwear"
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
ConceptsURL = "http://cncpts.com/collections/footwear#"
SocialStatusURL = "https://www.socialstatuspgh.com/collections/sneakers?page=1&sort_by=created-descending"
ExtraButterURL = URL = "https://shop.extrabutterny.com/collections/footwear?page=1&sort_by=created-descending"
BodegaURL = "https://shop.bdgastore.com/collections/footwear?sort_by=created-descending&page=1"
SaintAlfredURL = "https://www.saintalfred.com/collections/footwear?page=1&sort_by=created-descending"
LapstoneNHammerURL = "https://www.lapstoneandhammer.com/collections/foortwear?page=1"
ShelfLifeURL = "https://www.shelflife.co.za/Online-store/sneakers/?&page=1"
AsphaltGoldURL = "https://asphaltgold.de/en/sneaker?p=1"
HanonURL = "http://www.hanon-shop.com/c/q/department/footwear"
SoleBoxURL = "https://www.solebox.com/en/Footwear/"
ConsortiumURL = "http://www.consortium.co.uk/footwear.html?brand=adidas,nike&p=1"
HavenURL = "https://shop.havenshop.ca/collections/footwear?page=1&sort_by=created-descending"
NeedSupplyURL = "http://needsupply.com/mens/shoes/sneakers?p=1"
LoadedURL = "http://www.loadednz.com/products/footwear,1"
WellGoshURL = "https://wellgosh.com/footwear?dir=desc&order=created_at&p=1"
CapsuleURL = "http://www.capsuletoronto.com/collections/footwear?page=1"
YMEURL = "https://ymeuniverse.com/en/sneakers?brand=Adidas+Consortium,Adidas,Nike,Nike+SP,NIKELAB+ACG&dir=asc&order=created_at&p=1"
HypeDCURL = "https://www.hypedc.com/mens/footwear?dir=desc&manufacturer=28,55,478&order=news_from_date&p=1"
BSTNURL = "https://www.bstnstore.com/en/footwear/filter/__brand_adidas.jordan.nike/page/1/sort/date_new"
TrophyRoomURL = "https://www.trophyroomstore.com/collections/all/footwear?page=1&sort_by=created-descending"
OfficeURL = "http://www.office.co.uk/view/search?page=1&pageSize=30&search=his&sort=releaseDate&BRAND=Adidas"
ALLikeURL = "https://www.allikestore.com/default/sneakers.html?dir=desc&limit=16&manufacturer=27_639_494_641_628_28_650&order=created_at&p=1"
UrbanJungleURL = "http://www.urbanjunglestore.com/en/sneakers/shopby/nike-jordan-adidas.html#"
SSenseURL = "https://www.ssense.com/en-us/men/sneakers?page=1"
BackDoorURL = "https://www.back-door.it/product-category/sneakers/page/1/?orderby=date"
BasketURL = "http://www.baskets-store.com/sneakers/-/adidas-originals_nike/?dir=desc&ignore=true&limit=20&order=news_from_date&p=1"
DopeFactoryURL = "http://www.dope-factory.com/categories/shoes.html?dir=desc&limit=20&order=product_date&p=1"
NextDoorURL = "http://www.thenextdoor.fr/fr/34-chaussures?p=1"
SummerURL = "http://www.summer-store.com/en/11-shoes"
MrPorterURL = "https://www.mrporter.com/en-us/mens/shoes/sneakers?pn=1"
StormFashionURL = "http://stormfashion.dk/category/men/shoes"
TresBienURL = "http://tres-bien.com/footwear?p=1"
PackerURL = "https://packershoes.com/collections/footwear?page=1"
AddictURL = "https://www.addictmiami.com/collections/men?page=1"
AphroditeURL = "http://www.aphrodite1994.com/footwear#dir=asc&manufacturer=adidas,adidas-x-raf-simons,nike&order=entity_id&gan_data=true"
BaitURL = "http://www.baitme.com/footwear?dir=desc&order=stock_date&p=1"
BlendsURL = "https://www.blendsus.com/collections/mens-footwear?page=1"
NiceKicksURL = "https://shopnicekicks.com/collections/shoes?page=1&sort_by=created-descending"
FeatureURL = "https://www.featuresneakerboutique.com/collections/footwear?page=1&sort_by=created-descending"
HypeBeastURL = "https://hbx.com/categories/shoes/page/1"
DeadStockURL = "https://www.deadstock.ca/collections/footwear?page=1&sort_by=created-descending"
NotreURL = "https://www.notre-shop.com/collections/sneakers?page=1&sort_by=created-descending"
NrmlURL = "https://nrml.ca/collections/nrml-footwear?page=1&sort_by=created-descending"
OnenessURL = "https://www.oneness287.com/collections/men?page=1&sort_by=created-descending"
PufferRedsURL = "http://www.pufferreds.com/shop/men/footwear.html?dir=desc&order=news_to_date&p=1"
RenartsURL = "https://renarts.com/collections/mens-7/footwear?page=1&sort_by=newest-to-oldest"
ProperURL = "https://properlbc.com/collections/footwear?page=1&sort_by=created-descending"
SoleStopURL = "https://www.solestop.com/collections/men-footwear?sort_by=created-descending"
TitoloURL = "https://en.titolo.ch/sneakers?limit=36"
UptownURL = "https://www.uptownmia.com/collections/new-arrivals?page=1"
WestNYCURL = "https://www.westnyc.com/collections/footwear?page=1&sort_by=created-descending"
XileClothingURL = "https://www.xileclothing.com/browse/c-Footwear-24/b-Adidas-8/?page=1&sortby=new-additions"
SoleflyURL = "https://www.solefly.com/collections/mens-1?page=1"
SVDURL = "https://www.sivasdescalzo.com/en/lifestyle/sneakers?limit=36&p=1"
DSMNYURL = "http://shop.doverstreetmarket.com/us/what-s-new"
HubbastilleURL = "http://hubbastille.com/13-le-rez-de-chaussee?orderby=date_add&orderway=desc&orderway=desc&p=1"
ShoesAddictorURL = "http://shoesaddictor.com/"


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
		while True:
			try:
				products = Selector(response).xpath('//div[@class="grid-uniform grid--center wide--grid--middle"]//div[contains(@class,"grid__item")]')
				
				for product in products:
					item = KithItem()
					item['name'] = product.xpath('div/div/a[1]/img/@alt').extract()[0]
					item['link'] = "https://kith.com" + product.xpath('div/div/a[1]/@href').extract()[0]
					# item['image'] = "https:" + product.xpath('div/div/a[1]/img/@src').extract()[0]
					item['size'] = "https://kith.com/cart/add.js?id=" + product.xpath('div/div/a[2]/div/*/div[1]/@data-value').extract()[0] + "&quantity=1"
					yield item
					
				yield Request(KithURL, callback=self.parse, dont_filter=True, priority=0)	
			
			except:
				pass
				
				
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
            item['name'] = product.xpath('h3/text()').extract()[0]
            item['link'] = product.xpath('@href').extract()[0]
            # item['image'] = product.xpath('figure/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(RuvillaURL, callback=self.parse, dont_filter=True, priority=1)
		
		
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
            # item['image'] = product.xpath('a/div/img/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(FootShopURL, callback=self.parse, dont_filter=True, priority=2)
		
		
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
            # item['image'] = product.xpath('.//div[1]/@base_img').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(AfewURL, callback=self.parse, dont_filter=True, priority=3)
		
		
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
            # item['image'] = product.xpath('.//a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(CalirootsURL, callback=self.parse, dont_filter=True, priority=4)
		
		
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
            # item['image'] = product.xpath('.//a/div/img[1]/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(EinhalbURL, callback=self.parse, dont_filter=True, priority=5)
		
		
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
            # item['image'] = product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(EndURL, callback=self.parse, dont_filter=True, priority=6)
		
		
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
            # item['image'] = "http://www.sneakersnstuff.com" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SNSURL, callback=self.parse, dont_filter=True, priority=7)
		
		
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
            # item['image'] = product.xpath('div/div/div[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(TintURL, callback=self.parse, dont_filter=True, priority=8)
		
		
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
            # item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(OverkillURL, callback=self.parse, dont_filter=True, priority=9)
		
		
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
            item['name'] = product.xpath('.//a[2]/@title').extract()[0]
            item['link'] = product.xpath('.//a[2]/@href').extract()[0]
            # item['image'] = product.xpath('.//a[2]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(FootDistrictURL, callback=self.parse, dont_filter=True, priority=10)
		
		
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
            # item['image'] = product.xpath('.//span/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SizeURL, callback=self.parse, dont_filter=True, priority=11)
		
		
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
            # item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(YCMCURL, callback=self.parse, dont_filter=True, priority=12)
		
		
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
            # item['image'] = product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(CityURL, callback=self.parse, dont_filter=True, priority=13)
		
		
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
            item['name'] = product.xpath('.//div/a/@title').extract()[0].replace(" - Men's", "")
            item['link'] = product.xpath('.//div/a/@href').extract()[0].replace("&cm=GLOBAL SEARCH: KEYWORD SEARCH", "")
            # item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(FootLockerURL, callback=self.parse, dont_filter=True, priority=14)
		
		
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
            item['name'] = product.xpath('.//div/a/@title').extract()[0].replace(" - Men's", "")
            item['link'] = product.xpath('.//div/a/@href').extract()[0].replace("&cm=GLOBAL SEARCH: KEYWORD SEARCH", "")
            # item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(FootActionURL, callback=self.parse, dont_filter=True, priority=15)
		
		
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
            item['name'] = product.xpath('.//div/a/@title').extract()[0].replace(" - Men's", "")
            item['link'] = product.xpath('.//div/a/@href').extract()[0].replace("&cm=GLOBAL SEARCH: KEYWORD SEARCH", "")
            # item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(ChampsURL, callback=self.parse, dont_filter=True, priority=16)
		
		
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
            item['name'] = product.xpath('.//div/a/@title').extract()[0].replace(" - Men's", "")
            item['link'] = product.xpath('.//div/a/@href').extract()[0].replace("&cm=GLOBAL SEARCH: KEYWORD SEARCH", "")
            # item['image'] = product.xpath('.//div/a/div/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(EastBayURL, callback=self.parse, dont_filter=True, priority=17)
		
		
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
            item['name'] = product.xpath('.//div/a[2]/div/p/text()').extract()[0].strip().replace("Men's ", "")
            item['link'] = "http://www.finishline.com" + product.xpath('.//div/a[1]/@href').extract()[0]
            # item['image'] = product.xpath('.//div/a[1]/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(FinishLineURL, callback=self.parse, dont_filter=True, priority=18)
		
		
class AdidasUSSpider(Spider):
    
    name = "AdidasUSSpider"
    allowded_domains = ["adidas.com"]
    start_urls = [AdidasUSURL]

    def __init__(self):
        logging.critical("AdidasUSSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="hoverable clearfix"]//div[@class="product-tile"]//div[contains(@class,"hockeycard")]')
        
        for product in products:
            item = AdidasItem()
            item['name'] = product.xpath('div[3]/div[3]/a/@data-productname').extract()[0]
            item['link'] = product.xpath('div[3]/div[3]/a/@href').extract()[0]
            # item['image'] = product.xpath('div[3]/div[3]/a/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(AdidasUSURL, callback=self.parse, dont_filter=True, priority=19)
		
		
class AdidasEUSpider(Spider):
    
    name = "AdidasEUSpider"
    allowded_domains = ["adidas.co.uk"]
    start_urls = [AdidasEUURL]

    def __init__(self):
        logging.critical("AdidasEUSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="hoverable clearfix"]//div[@class="product-tile"]//div[contains(@class,"hockeycard")]')
        
        for product in products:
            item = AdidasItem()
            item['name'] = product.xpath('div[3]/div[3]/a/@data-productname').extract()[0]
            item['link'] = product.xpath('div[3]/div[3]/a/@href').extract()[0]
            # item['image'] = product.xpath('div[3]/div[3]/a/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(AdidasEUURL, callback=self.parse, dont_filter=True, priority=20)
		
		
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
            # item['image'] = product.xpath('.//div/div/div[1]/div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(NikeURL, callback=self.parse, dont_filter=True, priority=21)
		
		
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
            item['name'] = product.xpath('.//a/img/@alt').extract()[0].replace(" (Men)", "")
            item['link'] = "http://shop.nordstrom.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(NordstromURL, callback=self.parse, dont_filter=True, priority=22)
		
		
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
            # item['image'] = product.xpath('.//div/div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(BarneysURL, callback=self.parse, dont_filter=True, priority=23)
		
		
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
            # item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(JimmyJazzURL, callback=self.parse, dont_filter=True, priority=24)
		
		
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
            # item['image'] = product.xpath('.//span/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(JDSportsURL, callback=self.parse, dont_filter=True, priority=25)
		
		
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
            # item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(FootPatrolURL, callback=self.parse, dont_filter=True, priority=26)
		
		
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
            # item['image'] = "http:" + product.xpath('.//a/div/img/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SneakerPoliticsURL, callback=self.parse, dont_filter=True, priority=27)
		
		
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
            # item['image'] = "http:" + product.xpath('div[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(UrbanIndustryURL, callback=self.parse, dont_filter=True, priority=28)
		
		
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
            # item['image'] = product.xpath('.//a/img/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SneakerBaasURL, callback=self.parse, dont_filter=True, priority=29)
		
		
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
            # item['image'] = "http:" + product.xpath('div/p[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(UrbanOutfittersURL, callback=self.parse, dont_filter=True, priority=30)
		
		
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
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(LuisaURL, callback=self.parse, dont_filter=True, priority=31)
		
		
class SlamJamSpider(Spider):
    
    name = "SlamJamSpider"
    allowded_domains = ["slamjamsocialism.com"]
    start_urls = [SlamJamURL]
    custom_settings = {'ROBOTSTXT_OBEY': False}
    
    def __init__(self):
        logging.critical("SlamJamSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product_list grid row packery"]//li[contains(@class,"tooltip")]//div[@class="product-container"]//div[@class="left-block"]//div[@class="product-image-container"]')
        
        for product in products:
            item = SlamJamItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SlamJamURL, callback=self.parse, dont_filter=True, priority=32)
		
		
class Rise45Spider(Spider):

    name = "Rise45Spider"
    allowded_domains = ["rise45.com"]
    start_urls = [Rise45URL]
	
    def __init__(self):
        logging.critical("Rise45Spider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@id="content"]//div[@class="collection-matrix"]//div[contains(@class,"col")]/div')
		
        for product in products:
            item = Rise45Item()
            item['name'] = product.xpath('a[2]/h4/text()').extract()[0]
            item['link'] = "https://rise45.com" + product.xpath('a[1]/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(Rise45URL, callback=self.parse, dont_filter=True, priority=33)
		
		
class UndefeatedSpider(Spider):
    
    name = "UndefeatedSpider"
    allowded_domains = ["undefeated.com"]
    start_urls = [UndefeatedURL]
    
    def __init__(self):
        logging.critical("UndefeatedSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="collection-listing cf"]//div[@class="product-list"]//div[contains(@class,"product-block")]')
		
        for product in products:
            item = UndefeatedItem()
            item['name'] = product.xpath('.//a/div[1]/div/div/text()').extract()[0]
            item['link'] = "https://shop.undefeated.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "http:" + product.xpath('.//div/div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(UndefeatedURL, callback=self.parse, dont_filter=True, priority=34)
		
		
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
            item['name'] = product.xpath('span[@class="productImgContainer"]/img/@alt').extract()[0]
            item['link'] = "http://www.zappos.com" + product.xpath('@href').extract()[0]
            # item['image'] = product.xpath('span[@class="productImgContainer"]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(ZapposURL, callback=self.parse, dont_filter=True, priority=35)
		
		
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
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(PointzURL, callback=self.parse, dont_filter=True, priority=36)
		
		
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
            # item['image'] = product.xpath('a/img/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(StickABushURL, callback=self.parse, dont_filter=True, priority=37)
		
		
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
            # item['image'] = "http://www.shoepalace.com" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(ShoesPalaceURL, callback=self.parse, dont_filter=True, priority=38)
		
		
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
            # item['image'] = "http:" + product.xpath('a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(KongURL, callback=self.parse, dont_filter=True, priority=39)
		
		
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
            # item['image'] = product.xpath('a/span/span/img/@srcset').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SaveOurSoleURL, callback=self.parse, dont_filter=True, priority=40)
		
		
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
            # item['image'] = "http://www.inflammable.com/" + product.xpath('div[1]/div[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(InflammableURL, callback=self.parse, dont_filter=True, priority=41)
		
		
class DefShopSpider(Spider):

    name = "DefShopSpider"
    allowded_domains = ["def-shop.com"]
    start_urls = [DefShopURL]
	
    def __init__(self):
        logging.critical("DefShopSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row def-v-offset3"]//div[contains(@class,"def-col-listing")]//article[@class="prod-article"]//div[@class="bx-wrapper"]')
        
        for product in products:
            item = DefShopItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/div/img/@content').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(DefShopURL, callback=self.parse, dont_filter=True, priority=42)
		
		
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
            item['name'] = product.xpath('div[2]/div[1]/a//text()[3]').extract()[0].strip()
            item['link'] = "http://www.offspring.co.uk/view" + product.xpath('div[1]/a/@href').extract()[0]
            # item['image'] = product.xpath('div[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(OffspringURL, callback=self.parse, dont_filter=True, priority=43)
		
		
class SoleKitchenSpider(Spider):

    name = "SoleKitchenSpider"
    allowded_domains = ["solekitchen.de"]
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
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(SoleKitchenURL, callback=self.parse, dont_filter=True, priority=44)
		
		
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
            # item['image'] = "http://www.drome.co.uk" + product.xpath('div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(DromeURL, callback=self.parse, dont_filter=True, priority=45)
		
		
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
            # item['image'] = "https://www.footasylum.com" + product.xpath('div/span[2]/img/@data-original').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(FootAsylumURL, callback=self.parse, dont_filter=True, priority=46)
		
		
class ConceptsSpider(Spider):
    
    name = "ConceptsSpider"
    allowded_domains = ["cncpts.com"]
    start_urls = [ConceptsURL]
    
    def __init__(self):
        logging.critical("ConceptsSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="prod-flex-list"]//div[contains(@class,"product")]')

        for product in products:
            item = ConceptsItem()
            item['name'] = product.xpath('div/h4/a/text()').extract()[0]
            item['link'] = "http://cncpts.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "http:" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(ConceptsURL, callback=self.parse, dont_filter=True, priority=47)
		
		
class SocialStatusSpider(Spider):
    
    name = "SocialStatusSpider"
    allowded_domains = ["socialstatuspgh.com"]
    start_urls = [SocialStatusURL]
    
    def __init__(self):
        logging.critical("SocialStatusSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="desktop-12 tablet-6 mobile-3"]//div[contains(@class,"product-index")]//div[@class="product-index-inner"]')
		
        for product in products:
            item = SocialStatusItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "https://www.socialstatuspgh.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img[1]/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SocialStatusURL, callback=self.parse, dont_filter=True, priority=48)
		
		
class ExtraButterSpider(Spider):

    name = "ExtraButterSpider"
    allowded_domains = ["extrabutterny.com"]
    start_urls = [ExtraButterURL]
	
    def __init__(self):
        logging.critical("ExtraButterSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row"]//div[contains(@class,"col-xs-12")]//div[@class="product-thumbnail"]')
		
        for product in products:
            item = ExtraButterItem()
            item['name'] = product.xpath('div/article/div[2]/h3/a/@data-full-title').extract()[0]
            item['link'] = "https://shop.extrabutterny.com" + product.xpath('div/article/div[2]/h3/a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(ExtraButterURL, callback=self.parse, dont_filter=True, priority=49)
		
		
class BodegaSpider(Spider):
    
    name = "BodegaSpider"
    allowded_domains = ["bdgastore.com"]
    start_urls = [BodegaURL]
    
    def __init__(self):
        logging.critical("BodegaSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[contains(@class,"clear-xs-only clear-sm-only col-md-9")]//ul//li[contains(@class,"product-item")]')
		
        for product in products:
            item = BodegaItem()
            item['name'] = product.xpath('div/div/h3/a/text()').extract()[0].strip()
            item['link'] = "https://shop.bdgastore.com" + product.xpath('div/a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/a/div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(BodegaURL, callback=self.parse, dont_filter=True, priority=50)
		
		
class SaintAlfredSpider(Spider):
    
    name = "SaintAlfredSpider"
    allowded_domains = ["saintalfred.com"]
    start_urls = [SaintAlfredURL]
    
    def __init__(self):
        logging.critical("SaintAlfredSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[contains(@class,"collection-products")]//div[contains(@class,"product-list-item")]//figure[@class="product-list-item-thumbnail"]')
		
        for product in products:
            item = SaintAlfredItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = "https://www.saintalfred.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img//@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(SaintAlfredURL, callback=self.parse, dont_filter=True, priority=51)	
		
		
class LapstoneNHammerSpider(Spider):
    
    name = "LapstoneNHammerSpider"
    allowded_domains = ["lapstoneandhammer.com"]
    start_urls = [LapstoneNHammerURL]
    
    def __init__(self):
        logging.critical("LapstoneNHammerSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-grid clearfix"]//div[contains(@class,"product-item columns")]//div[@class="image-wrapper"]')

        for product in products:
            item = LapstoneNHammerItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = "https://www.lapstoneandhammer.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img//@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(LapstoneNHammerURL, callback=self.parse, dont_filter=True, priority=52)
		
		
class ShelfLifeSpider(Spider):
    
    name = "ShelfLifeSpider"
    allowded_domains = ["shelflife.co.za"]
    start_urls = [ShelfLifeURL]
    
    def __init__(self):
        logging.critical("ShelfLifeSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row push_both push_top push_bottom light_row"]//div[contains(@class,"col-xs-6")]')
		
        for product in products:
            item = ShelfLifeItem()
            item['name'] = product.xpath('.//a/div/img/@alt').extract()[0]
            item['link'] = "https://www.shelflife.co.za/" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https://www.shelflife.co.za/" + product.xpath('.//a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(ShelfLifeURL, callback=self.parse, dont_filter=True, priority=53)
		
		
class AsphaltGoldSpider(Spider):
    
    name = "AsphaltGoldSpider"
    allowded_domains = ["asphaltgold.de"]
    start_urls = [AsphaltGoldURL]
    
    def __init__(self):
        logging.critical("AsphaltGoldSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-grid"]//section[contains(@class,"item")]')

        for product in products:
            item = AsphaltGoldItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img//@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(AsphaltGoldURL, callback=self.parse, dont_filter=True, priority=54)
		
		
class HanonSpider(Spider):
    
    name = "HanonSpider"
    allowded_domains = ["hanon-shop.com"]
    start_urls = [HanonURL]
    
    def __init__(self):
        logging.critical("HanonSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@id="ks-products-wrapper"]//div[contains(@class,"product")]')

        for product in products:
            item = HanonItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "http://www.hanon-shop.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(HanonURL, callback=self.parse, dont_filter=True, priority=55)
		
		
class SoleBoxSpider(Spider):
    
    name = "SoleBoxSpider"
    allowded_domains = ["solebox.com"]
    start_urls = [SoleBoxURL]
    
    def __init__(self):
        logging.critical("SoleBoxSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="gridView clear"]//li[contains(@class,"productData")]')
		
        for product in products:
            item = SoleBoxItem()
            item['name'] = product.xpath('a/@title').extract()[0].strip()
            temp = product.xpath('a/@href').extract()[0]
            item['link'] = re.sub(r'(\?(.*))', '', temp)
            # item['image'] = product.xpath('a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SoleBoxURL, callback=self.parse, dont_filter=True, priority=56)
		
		
class ConsortiumSpider(Spider):
    
    name = "ConsortiumSpider"
    allowded_domains = ["consortium.co.uk"]
    start_urls = [ConsortiumURL]
    
    def __init__(self):
        logging.critical("ConsortiumSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//li[@class="item text-center"]')
		
        for product in products:
            item = ConsortiumItem()
            item['name'] = product.xpath('div/h2/a/@title').extract()[0]
            item['link'] = product.xpath('div/h2/a/@href').extract()[0]
            # item['image'] = product.xpath('img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(ConsortiumURL, callback=self.parse, dont_filter=True, priority=57)
		
		
class HavenSpider(Spider):
    
    name = "HavenSpider"
    allowded_domains = ["havenshop.ca"]
    start_urls = [HavenURL]
    
    def __init__(self):
        logging.critical("HavenSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//main[@class="main shop-category"]//section[@class="shop-products"]//a[contains(@class,"product-card")]')

        for product in products:
            item = HavenItem()
            item['name'] = product.xpath('div[2]/p[2]/text()').extract()[0]
            item['link'] = product.xpath('@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div[1]/img[1]/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(HavenURL, callback=self.parse, dont_filter=True, priority=58)
		
		
class NeedSupplySpider(Spider):
    
    name = "NeedSupplySpider"
    allowded_domains = ["needsupply.com"]
    start_urls = [NeedSupplyURL]
    
    def __init__(self):
        logging.critical("NeedSupplySpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-list-grid"]//article[contains(@class,"grid-item")]')

        for product in products:
            item = NeedSupplyItem()
            item['name'] = product.xpath('.//div/a/@title').extract()[0]
            item['link'] = product.xpath('.//div/a/@href').extract()[0]
            # item['image'] = product.xpath('.//div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(NeedSupplyURL, callback=self.parse, dont_filter=True, priority=59)
		
		
class LoadedSpider(Spider):
    
    name = "LoadedSpider"
    allowded_domains = ["loadednz.com"]
    start_urls = [LoadedURL]
    
    def __init__(self):
        logging.critical("LoadedSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row image-grid"]//div[contains(@class,"image")]')

        for product in products:
            item = LoadedItem()
            item['name'] = product.xpath('.//div[2]/text()').extract()[0]
            item['link'] = "http://www.loadednz.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(LoadedURL, callback=self.parse, dont_filter=True, priority=60)
		
		
class WellGoshSpider(Spider):
    
    name = "WellGoshSpider"
    allowded_domains = ["wellgosh.com"]
    start_urls = [WellGoshURL]
    
    def __init__(self):
        logging.critical("WellGoshSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products row grid-mode"]//article[contains(@class,"small-6")]')

        for product in products:
            item = WellGoshItem()
            item['name'] = product.xpath('.//figure/a/@title').extract()[0]
            item['link'] = product.xpath('.//figure/a/@href').extract()[0]
            # item['image'] = product.xpath('.//figure/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(WellGoshURL, callback=self.parse, dont_filter=True, priority=61)
		
		
class CapsuleSpider(Spider):
    
    name = "CapsuleSpider"
    allowded_domains = ["capsuletoronto.com"]
    start_urls = [CapsuleURL]
    
    def __init__(self):
        logging.critical("CapsuleSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-list"]//div[contains(@class,"product-block")]//div[@class="block-inner"]//div[@class="image-cont"]')
		
        for product in products:
            item = CapsuleItem()
            item['name'] = product.xpath('a[1]/div/img/@alt').extract()[0]
            item['link'] = "http://www.capsuletoronto.com" + product.xpath('a[1]/@href').extract()[0]
            # item['image'] = "http:" + product.xpath('a[1]/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(CapsuleURL, callback=self.parse, dont_filter=True, priority=62)
		
		
class YMESpider(Spider):

    name = "YMESpider"
    allowded_domains = ["ymeuniverse.com"]
    start_urls = [YMEURL]
	
    def __init__(self):
        logging.critical("YMESpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//ul[contains(@class,"small-block-grid-2")]//li[@class="item"]//div[@class="item-wrapper"]')
		
        for product in products:
            item = YMEItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/span/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(YMEURL, callback=self.parse, dont_filter=True, priority=63)
		
		
class HypeDCSpider(Spider):
    
    name = "HypeDCSpider"
    allowded_domains = ["hypedc.com"]
    start_urls = [HypeDCURL]
    
    def __init__(self):
        logging.critical("HypeDCSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products row"]//div[contains(@class,"item")]')

        for product in products:
            item = HypeDCItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = product.xpath('.//a/@href').extract()[0]
            # item['image'] = product.xpath('.//a/div/img/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(HypeDCURL, callback=self.parse, dont_filter=True, priority=64)
		
		
class BSTNSpider(Spider):
    
    name = "BSTNSpider"
    allowded_domains = ["bstnstore.com"]
    start_urls = [BSTNURL]
	
    def __init__(self):
        logging.critical("BSTNSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="block-grid four-up mobile-two-up productlist"]//li[contains(@class,"item")]//div[@class="itemWrapper pOverlay"]//div[@class="pImageContainer"]//a[@class="plink image"]')

        for product in products:
            item = BSTNItem()
            item['name'] = product.xpath('div/@data-alt').extract()[0]
            item['link'] = "https://www.bstnstore.com" + product.xpath('@href').extract()[0]
            # item['image'] = "https://www.bstnstore.com" + product.xpath('div/div[2]/@data-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
	yield Request(BSTNURL, callback=self.parse, dont_filter=True, priority=65)
	
	
class TrophyRoomSpider(Spider):
    
    name = "TrophyRoomSpider"
    allowded_domains = ["trophyroomstore.com"]
    start_urls = [TrophyRoomURL]
	
    def __init__(self):
        logging.critical("TrophyRoomSpider STARTED.")
		
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="grid-uniform"]//div[contains(@class,"grid__item")]//div[@class="product-card"]')
		
        for product in products:
            item = TrophyRoomItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = "https://www.trophyroomstore.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(TrophyRoomURL, callback=self.parse, dont_filter=True, priority=66)
		
		
class OfficeSpider(Spider):
    
    name = "OfficeSpider"
    allowded_domains = ["office.co.uk"]
    start_urls = [OfficeURL]
    
    def __init__(self):
        logging.critical("OfficeSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="productList row"]//li[contains(@class,"col-xs-6")]//div[@class="productList_item"]')

        for product in products:
            item = OfficeItem()
            item['name'] = product.xpath('div[2]/div/a/text()[2]').extract()[0].strip()
            item['link'] = "http://www.office.co.uk" + product.xpath('div[1]/a/@href').extract()[0]
            # item['image'] = "http:" + product.xpath('div[1]/a/img/@data-transition').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(OfficeURL, callback=self.parse, dont_filter=True, priority=67)
		
		
class ALLikeSpider(Spider):
    
    name = "ALLikeSpider"
    allowded_domains = ["allikestore.com"]
    start_urls = [ALLikeURL]
    
    def __init__(self):
        logging.critical("ALLikeSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="products-grid"]//li[contains(@class,"item")]//div[@class="item-wrap"]')

        for product in products:
            item = ALLikeItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(ALLikeURL, callback=self.parse, dont_filter=True, priority=68)
		
		
class UrbanJungleSpider(Spider):
    
    name = "UrbanJungleSpider"
    allowded_domains = ["urbanjunglestore.com"]
    start_urls = [UrbanJungleURL]
    custom_settings = {'ROBOTSTXT_OBEY': False}
    
    def __init__(self):
        logging.critical("UrbanJungleSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="products-grid category-products-grid itemgrid itemgrid-adaptive itemgrid-3col single-line-name centered equal-height"]//li[contains(@class,"item")]//div[@class="product-image-wrapper"]')

        for product in products:
            item = UrbanJungleItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(UrbanJungleURL, callback=self.parse, dont_filter=True, priority=69)
		
		
class SSenseSpider(Spider):
    
    name = "SSenseSpider"
    allowded_domains = ["ssense.com"]
    start_urls = [SSenseURL]
    
    def __init__(self):
        logging.critical("SSenseSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="browsing-product-list"]//figure[contains(@class,"browsing-product-item")]')

        for product in products:
            item = SSenseItem()
            item['name'] = product.xpath('.//a/figcaption/p[2]/text()').extract()[0]
            item['link'] = product.xpath('.//meta[3]/@content').extract()[0]
            # item['image'] = product.xpath('.//meta[2]/@content').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SSenseURL, callback=self.parse, dont_filter=True, priority=70)
		
		
class BackDoorSpider(Spider):
    
    name = "BackDoorSpider"
    allowded_domains = ["back-door.it"]
    start_urls = [BackDoorURL]
    
    def __init__(self):
        logging.critical("BackDoorSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="products clearfix"]//li')

        for product in products:
            item = BackDoorItem()
            item['name'] = product.xpath('a[1]/h6/text()').extract()[0]
            item['link'] = product.xpath('a[1]/@href').extract()[0]
            # item['image'] = product.xpath('div/a[2]/span/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(BackDoorURL, callback=self.parse, dont_filter=True, priority=71)
		
		
class BasketSpider(Spider):
    
    name = "BasketSpider"
    allowded_domains = ["baskets-store.com"]
    start_urls = [BasketURL]
    
    def __init__(self):
        logging.critical("BasketSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="products-grid"]//div[contains(@class,"item")]')

        for product in products:
            item = BasketItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(BasketURL, callback=self.parse, dont_filter=True, priority=72)
		
		
class DopeFactorySpider(Spider):
    
    name = "DopeFactorySpider"
    allowded_domains = ["dope-factory.com"]
    start_urls = [DopeFactoryURL]
    
    def __init__(self):
        logging.critical("DopeFactorySpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//div[contains(@class,"products-grid")]//div[@class="item span3"]')

        for product in products:
            item = DopeFactoryItem()
            item['name'] = product.xpath('div/a/@title').extract()[0]
            item['link'] = product.xpath('div/a/@href').extract()[0]
            # item['image'] = product.xpath('div/a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(DopeFactoryURL, callback=self.parse, dont_filter=True, priority=73)
		
		
class NextDoorSpider(Spider):
    
    name = "NextDoorSpider"
    allowded_domains = ["thenextdoor.fr"]
    start_urls = [NextDoorURL]
    
    def __init__(self):
        logging.critical("NextDoorSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="product_list grid row"]//li[contains(@class,"ajax_block_product")]//div[@class="product-container"]//div[@class="pro_outer_box"]')

        for product in products:
            item = NextDoorItem()
            item['name'] = product.xpath('div/a/@title').extract()[0]
            item['link'] = product.xpath('div/a/@href').extract()[0]
            # item['image'] = product.xpath('div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(NextDoorURL, callback=self.parse, dont_filter=True, priority=74)
		
		
class SummerSpider(Spider):
    
    name = "SummerSpider"
    allowded_domains = ["summer-store.com"]
    start_urls = [SummerURL]
    
    def __init__(self):
        logging.critical("SummerSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//section[@class="product_list row"]//article[contains(@class,"cl-8-r1")]')

        for product in products:
            item = SummerItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/div/img[1]/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SummerURL, callback=self.parse, dont_filter=True, priority=75)
		
		
class MrPorterSpider(Spider):
    
    name = "MrPorterSpider"
    allowded_domains = ["mrporter.com"]
    start_urls = [MrPorterURL]
    
    def __init__(self):
        logging.critical("MrPorterSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="pl-grid__column pl-grid__column--main"]//ul[@class="pl-products"]//li[contains(@class,"pl-products-item")]')

        for product in products:
            item = MrPorterItem()
            item['name'] = product.xpath('a/div[2]/div/span[2]/text()').extract()[0].replace(" Sneakers", "")
            item['link'] = "https://www.mrporter.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(MrPorterURL, callback=self.parse, dont_filter=True, priority=76)
		
		
class StormFashionSpider(Spider):
    
    name = "StormFashionSpider"
    allowded_domains = ["stormfashion.dk"]
    start_urls = [StormFashionURL]
    
    def __init__(self):
        logging.critical("StormFashionSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product_list"]//li[contains(@class,"storm-item")]//div[@class="pro_img"]')

        for product in products:
            item = StormFashionItem()
            item['name'] = product.xpath('ul/li/a/img/@alt').extract()[0].strip()
            item['link'] = "http://stormfashion.dk" + product.xpath('ul/li/a/@href').extract()[0]
            # item['image'] = product.xpath('ul/li/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(StormFashionURL, callback=self.parse, dont_filter=True, priority=77)
		
		
class TresBienSpider(Spider):
    
    name = "TresBienSpider"
    allowded_domains = ["tres-bien.com"]
    start_urls = [TresBienURL]
    
    def __init__(self):
        logging.critical("TresBienSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products category-3col layout-"]//ul[contains(@class,"products-grid")]//li[@class="grid-1 rect first"]')

        for product in products:
            item = TresBienItem()
            item['name'] = product.xpath('a/div[2]/h2/text()').extract()[0].strip()
            item['link'] = "http://tres-bien.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/div[1]/picture/@data-default-src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(TresBienURL, callback=self.parse, dont_filter=True, priority=78)
		
		
class PackerSpider(Spider):
    
    name = "PackerSpider"
    allowded_domains = ["packershoes.com"]
    start_urls = [PackerURL]
    
    def __init__(self):
        logging.critical("PackerSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row"]//div//div[contains(@class,"product-class")]')

        for product in products:
            item = PackerItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "https://packershoes.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(PackerURL, callback=self.parse, dont_filter=True, priority=79)
		
		
class ShoesAddictorSpider(Spider):
    
    name = "ShoesAddictorSpider"
    allowded_domains = ["shoesaddictor.com"]
    start_urls = [ShoesAddictorURL]
    
    def __init__(self):
        logging.critical("ShoesAddictorSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row multi-columns-row"]//div[contains(@class,"col-sm-6")]//div[@class="shop-item"]')

        for product in products:
            item = ShoesAddictorItem()
            item['name'] = product.xpath('h4/a/text()').extract()[0]
            item['link'] = product.xpath('h4/a/@href').extract()[0]
            # item['image'] = product.xpath('div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(ShoesAddictorURL, callback=self.parse, dont_filter=True, priority=80)
		
		
class AddictSpider(Spider):
    
    name = "AddictSpider"
    allowded_domains = ["addictmiami.com"]
    start_urls = [AddictURL]
    
    def __init__(self):
        logging.critical("AddictSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="grid grid--no-gutters grid--uniform"]//div[contains(@class,"grid__item small--one-half")]')

        for product in products:
            item = AddictItem()
            item['name'] = product.xpath('a/div[2]/div[1]/text()').extract()[0]
            item['link'] = "https://www.addictmiami.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(AddictURL, callback=self.parse, dont_filter=True, priority=81)
		
		
class AphroditeSpider(Spider):
    
    name = "AphroditeSpider"
    allowded_domains = ["aphrodite1994.com"]
    start_urls = [AphroditeURL]
    
    def __init__(self):
        logging.critical("AphroditeSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="products-list--grid-mode"]//ul[contains(@class,"products-grid")]//li[contains(@class,"item")]')

        for product in products:
            item = AphroditeItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(AphroditeURL, callback=self.parse, dont_filter=True, priority=82)
		
		
class BaitSpider(Spider):
    
    name = "BaitSpider"
    allowded_domains = ["baitme.com"]
    start_urls = [BaitURL]
    
    def __init__(self):
        logging.critical("BaitSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[@class="item last"]')

        for product in products:
            item = BaitItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(BaitURL, callback=self.parse, dont_filter=True, priority=83)
		
		
class BlendsSpider(Spider):
    
    name = "BlendsSpider"
    allowded_domains = ["blendsus.com"]
    start_urls = [BlendsURL]
    
    def __init__(self):
        logging.critical("BlendsSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row"]//div[contains(@class,"product-index desktop-3 mobile-3")]')

        for product in products:
            item = BlendsItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = "https://www.blendsus.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(BlendsURL, callback=self.parse, dont_filter=True, priority=84)
		
		
class NiceKicksSpider(Spider):
    
    name = "NiceKicksSpider"
    allowded_domains = ["shopnicekicks.com"]
    start_urls = [NiceKicksURL]
    
    def __init__(self):
        logging.critical("NiceKicksSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="sixteen columns"]//div[contains(@class,"four")]')

        for product in products:
            item = NiceKicksItem()
            item['name'] = product.xpath('div/figure/img/@alt').extract()[0]
            item['link'] = "https://shopnicekicks.com" + product.xpath('div/figure/a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/figure/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(NiceKicksURL, callback=self.parse, dont_filter=True, priority=85)
		
		
class FeatureSpider(Spider):
    
    name = "FeatureSpider"
    allowded_domains = ["featuresneakerboutique.com"]
    start_urls = [FeatureURL]
    
    def __init__(self):
        logging.critical("FeatureSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="products-list clearfix"]//a[contains(@class,"entry")]')

        for product in products:
            item = FeatureItem()
            item['name'] = product.xpath('.//article/img/@alt').extract()[0]
            item['link'] = "https://www.featuresneakerboutique.com" + product.xpath('.//@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//article/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(FeatureURL, callback=self.parse, dont_filter=True, priority=86)
		
		
class HypeBeastSpider(Spider):
    
    name = "HypeBeastSpider"
    allowded_domains = ["hbx.com"]
    start_urls = [HypeBeastURL]
    
    def __init__(self):
        logging.critical("HypeBeastSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row product-row"]//div[contains(@class,"product-wrapper")]//div[@class="product-box catalog product"]')

        for product in products:
            item = HypeBeastItem()
            item['name'] = product.xpath('a[2]/h3/text()').extract()[0]
            item['link'] = "https://hbx.com" + product.xpath('div/a/@href').extract()[0]
            # item['image'] = product.xpath('div/a/img[1]/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(HypeBeastURL, callback=self.parse, dont_filter=True, priority=87)
		
		
class DeadStockSpider(Spider):
    
    name = "DeadStockSpider"
    allowded_domains = ["deadstock.ca"]
    start_urls = [DeadStockURL]
    
    def __init__(self):
        logging.critical("DeadStockSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="sixteen columns products"]//div[contains(@class,"four")]')

        for product in products:
            item = DeadStockItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = "https://www.deadstock.ca" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(DeadStockURL, callback=self.parse, dont_filter=True, priority=88)
		
		
class NotreSpider(Spider):
    
    name = "NotreSpider"
    allowded_domains = ["notre-shop.com"]
    start_urls = [NotreURL]
    
    def __init__(self):
        logging.critical("NotreSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row"]//div[contains(@class,"col-lg-4")]/div/div[1]')

        for product in products:
            item = NotreItem()
            item['name'] = product.xpath('a[1]/img/@alt').extract()[0]
            item['link'] = "https://www.notre-shop.com" + product.xpath('a[1]/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(NotreURL, callback=self.parse, dont_filter=True, priority=89)
		
		
class NrmlSpider(Spider):
    
    name = "NrmlSpider"
    allowded_domains = ["Nrml-shop.com"]
    start_urls = [NrmlURL]
    
    def __init__(self):
        logging.critical("NrmlSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="grid-uniform"]//div[contains(@class,"grid__item")]')

        for product in products:
            item = NrmlItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = "https://nrml.ca" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(NrmlURL, callback=self.parse, dont_filter=True, priority=90)
		
		
class OnenessSpider(Spider):
    
    name = "OnenessSpider"
    allowded_domains = ["oneness287.com"]
    start_urls = [OnenessURL]
    
    def __init__(self):
        logging.critical("OnenessSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-list collection-matrix clearfix"]//div[contains(@class,"four")]//div[@class="product-wrap"]')

        for product in products:
            item = OnenessItem()
            item['name'] = product.xpath('div/div[1]/a/text()').extract()[0]
            item['link'] = "https://www.oneness287.com" + product.xpath('div/a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/a/div/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(OnenessURL, callback=self.parse, dont_filter=True, priority=91)
		
		
class PufferRedsSpider(Spider):
    
    name = "PufferRedsSpider"
    allowded_domains = ["pufferreds.com"]
    start_urls = [PufferRedsURL]
    
    def __init__(self):
        logging.critical("PufferRedsSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="category-products"]//li[contains(@class,"item")]')

        for product in products:
            item = PufferRedsItem()
            item['name'] = product.xpath('.//a/@title').extract()[0]
            item['link'] = product.xpath('.//a/@href').extract()[0]
            # item['image'] = product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(PufferRedsURL, callback=self.parse, dont_filter=True, priority=92)
		
		
class RenartsSpider(Spider):
    
    name = "RenartsSpider"
    allowded_domains = ["renarts.com"]
    start_urls = [RenartsURL]
    
    def __init__(self):
        logging.critical("RenartsSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="row"]//div[contains(@class,"col-xs-12")]//div[@class="product-thumbnail"]')

        for product in products:
            item = RenartsItem()
            item['name'] = product.xpath('a/h4/text()').extract()[0]
            item['link'] = "https://renarts.com" + product.xpath('div/a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(RenartsURL, callback=self.parse, dont_filter=True, priority=93)
		
		
class ProperSpider(Spider):
    
    name = "ProperSpider"
    allowded_domains = ["properlbc.com"]
    start_urls = [ProperURL]
    
    def __init__(self):
        logging.critical("ProperSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="products"]//div[contains(@class,"four")]')

        for product in products:
            item = ProperItem()
            item['name'] = product.xpath('.//a/div[1]/img/@alt').extract()[0]
            item['link'] = "https://properlbc.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/div[1]/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(ProperURL, callback=self.parse, dont_filter=True, priority=94)
		
		
class SoleStopSpider(Spider):
    
    name = "SoleStopSpider"
    allowded_domains = ["solestop.com"]
    start_urls = [SoleStopURL]
    
    def __init__(self):
        logging.critical("SoleStopSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="cata-product cp-grid cp-5 clearfix"]//div[contains(@class,"product-grid-item")]//div[@class="product-wrapper"]//div[@class="product-head"]//div[@class="product-image"]//div[@class="featured-img switch"]')

        for product in products:
            item = SoleStopItem()
            item['name'] = product.xpath('.//a/img/@alt').extract()[0]
            item['link'] = "https://www.solestop.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SoleStopURL, callback=self.parse, dont_filter=True, priority=95)
		
		
class TitoloSpider(Spider):
    
    name = "TitoloSpider"
    allowded_domains = ["titolo.ch"]
    start_urls = [TitoloURL]
    
    def __init__(self):
        logging.critical("TitoloSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="small-block-grid-2 medium-block-grid-3 large-block-grid-4 no-bullet"]//li[contains(@class,"item")]//div[@class="list-inner-wrapper"]')

        for product in products:
            item = TitoloItem()
            item['name'] = product.xpath('a/@title').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = product.xpath('div[1]/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(TitoloURL, callback=self.parse, dont_filter=True, priority=96)
		
		
class UptownSpider(Spider):
    
    name = "UptownSpider"
    allowded_domains = ["uptownmia.com"]
    start_urls = [UptownURL]
    
    def __init__(self):
        logging.critical("UptownSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="product-list"]//div[contains(@class,"product-block")]//div[@class="block-inner"]//div[@class="image-cont"]')

        for product in products:
            item = UptownItem()
            item['name'] = product.xpath('.//a/img/@alt').extract()[0]
            item['link'] = "https://www.uptownmia.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(UptownURL, callback=self.parse, dont_filter=True, priority=97)
		
		
class WestNYCSpider(Spider):
    
    name = "WestNYCSpider"
    allowded_domains = ["westnyc.com"]
    start_urls = [WestNYCURL]
    
    def __init__(self):
        logging.critical("WestNYCSpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="grid grid--uniform grid--view-items"]//div[contains(@class,"grid__item")]//div[@class="grid-view-item"]')

        for product in products:
            item = WestNYCItem()
            item['name'] = product.xpath('.//a/img/@alt').extract()[0]
            item['link'] = "https://www.westnyc.com" + product.xpath('.//a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('.//a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(WestNYCURL, callback=self.parse, dont_filter=True, priority=98)
		
		
class XileClothingSpider(Spider):
    
    name = "XileClothingSpider"
    allowded_domains = ["xileclothing.com"]
    start_urls = [XileClothingURL]
    
    def __init__(self):
        logging.critical("XileClothingSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="itemsList"]/li/div[1]')

        for product in products:
            item = XileClothingItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = product.xpath('a/@href').extract()[0]
            # item['image'] = "https://www.xileclothing.com" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(XileClothingURL, callback=self.parse, dont_filter=True, priority=99)
		
		
class SoleflySpider(Spider):
    
    name = "SoleflySpider"
    allowded_domains = ["solefly.com"]
    start_urls = [SoleflyURL]
    
    def __init__(self):
        logging.critical("SoleflySpider STARTED.")

    def parse(self, response):
        products = Selector(response).xpath('//div[@class="grid grid--uniform grid--view-items"]//div[contains(@class,"grid__item")]//div[@class="grid-view-item text-center"]')

        for product in products:
            item = SoleflyItem()
            item['name'] = product.xpath('a/img/@alt').extract()[0]
            item['link'] = "https://www.solefly.com" + product.xpath('a/@href').extract()[0]
            # item['image'] = "https:" + product.xpath('a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SoleflyURL, callback=self.parse, dont_filter=True, priority=100)
		
		
class SVDSpider(Spider):
    
    name = "SVDSpider"
    allowded_domains = ["SVD.com"]
    start_urls = [SVDURL]
    
    def __init__(self):
        logging.critical("SVDSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//ul[@class="products-list medium-block-grid-3 large-block-grid-4"]//li')

        for product in products:
            item = SVDItem()
            item['name'] = product.xpath('div/a/img/@alt').extract()[0]
            item['link'] = product.xpath('div/a/@href').extract()[0]
            item['image'] = product.xpath('div/a/img/@src').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item

        yield Request(SVDURL, callback=self.parse, dont_filter=True, priority=101)
		
		
class DSMNYSpider(Spider):
    
    name = "DSMNYSpider"
    allowded_domains = ["doverstreetmarket.com"]
    start_urls = [DSMNYURL]
    
    def __init__(self):
        logging.critical("DSMNYSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@id="home-content"]//a')
        
        for product in products:
            item = DSMNYItem()
            item['link'] = product.xpath('@href').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
            
        yield Request(DSMNYURL, callback=self.parse, dont_filter=True, priority=102)
		
		
class HubbastilleSpider(Spider):
    
    name = "HubbastilleSpider"
    allowded_domains = ["hubbastille.com"]
    start_urls = [HubbastilleURL]
    
    def __init__(self):
        logging.critical("HubbastilleSpider STARTED.")
        
    def parse(self, response):
        products = Selector(response).xpath('//div[@class="mix cs-item"]')
		
        for product in products:
            item = HubbastilleItem()
            item['name'] = product.xpath('section/div/div/a/img[1]/@title').extract()[0]
            item['link'] = product.xpath('section/div/div/a/@href').extract()[0]
            item['size'] = '**NOT SUPPORTED YET**'
            yield item
			
        yield Request(HubbastilleURL, callback=self.parse, dont_filter=True, priority=103)
		
		
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
process.crawl(AdidasUSSpider)
process.crawl(AdidasEUSpider)
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
process.crawl(ConceptsSpider)
process.crawl(SocialStatusSpider)
process.crawl(ExtraButterSpider)
process.crawl(BodegaSpider)
process.crawl(SaintAlfredSpider)
process.crawl(LapstoneNHammerSpider)
process.crawl(ShelfLifeSpider)
process.crawl(AsphaltGoldSpider)
process.crawl(HanonSpider)
process.crawl(SoleBoxSpider)
process.crawl(ConsortiumSpider)
process.crawl(HavenSpider)
process.crawl(NeedSupplySpider)
process.crawl(LoadedSpider)
process.crawl(WellGoshSpider)
process.crawl(CapsuleSpider)
process.crawl(YMESpider)
process.crawl(HypeDCSpider)
process.crawl(BSTNSpider)
process.crawl(TrophyRoomSpider)
process.crawl(OfficeSpider)
process.crawl(ALLikeSpider)
process.crawl(UrbanJungleSpider)

process.crawl(SSenseSpider)
process.crawl(BackDoorSpider)
process.crawl(BasketSpider)
process.crawl(DopeFactorySpider)
process.crawl(NextDoorSpider)
process.crawl(SummerSpider)
process.crawl(MrPorterSpider)
process.crawl(StormFashionSpider)
process.crawl(TresBienSpider)
process.crawl(PackerSpider)
process.crawl(AddictSpider)
process.crawl(AphroditeSpider)
process.crawl(BaitSpider)
process.crawl(BlendsSpider)
process.crawl(NiceKicksSpider)
process.crawl(FeatureSpider)
process.crawl(HypeBeastSpider)
process.crawl(DeadStockSpider)
process.crawl(NotreSpider)
process.crawl(NrmlSpider)
process.crawl(OnenessSpider)
process.crawl(PufferRedsSpider)
process.crawl(RenartsSpider)
process.crawl(ProperSpider)
process.crawl(SoleStopSpider)
process.crawl(TitoloSpider)
process.crawl(UptownSpider)
process.crawl(WestNYCSpider)
process.crawl(XileClothingSpider)
process.crawl(SoleflySpider)
process.crawl(SVDSpider)
process.crawl(HubbastilleSpider)

# process.crawl(ShoesAddictorSpider)
# process.crawl(DSMNYSpider)
# process.crawl(EndSpider)		#Captcha if crawl too much.
# process.crawl(SNSSpider)		#ASN blocked on Vultr via CloudFlare.
# process.crawl(FinishLineSpider)	#Banned on Vultr.
# process.crawl(BarneysSpider)		#Ban if crawl too much.
# process.crawl(JimmyJazzSpider)	#ASN blocked on Vultr via CloudFlare.
# process.crawl(ShoesPalaceSpider)      #Need to disobey robots.txt, if you want to crawl.

process.start()
