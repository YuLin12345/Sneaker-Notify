#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sneaker Notify
# author - Yu Lin
# https://github.com/yulin12345
# admin@yulin12345.site

from datetime import datetime
import hashlib
import sys

import MySQLdb
from TwitterAPI import TwitterAPI
from colorama import Fore, Style
from pytz import timezone
import requests
from scrapy.exceptions import DropItem
from scrapy.http import Request

from items import *


# Convert time to EST.
DATE_CONVERT = datetime.now(timezone('US/Eastern'))
DATE = DATE_CONVERT.strftime("%m-%d-%Y|%H:%M:%S")

# MYSQL pipleline for storing.
class MYSQL_Pipeline(object):
    
  def __init__(self):
    # Database connection info. (host, user, password, database)
    self.conn = MySQLdb.connect(host='HOST NAME HERE', user='USER NAME HERE', passwd='PASSWORD HERE', db='DATABASE NAME HERE', charset="utf8", use_unicode=True)
    self.conn.ping(True)
    self.cursor = self.conn.cursor()
    
  # Process the item and insert into database.
  def process_item(self, item, spider):
    try:
        # Insert item into kith table.
        if isinstance(item, KithItem):
            self.cursor.execute("INSERT INTO kith (name, link, size, date) VALUES (%s, %s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), item['size'].encode('utf-8'), DATE))
            
        # Insert item into ruvilla table.
        elif isinstance(item, RuvillaItem):
            self.cursor.execute("INSERT INTO ruvilla (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footlocker table.
        elif isinstance(item, FootLockerItem):
            self.cursor.execute("INSERT INTO footlocker (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footaction table.
        elif isinstance(item, FootActionItem):
            self.cursor.execute("INSERT INTO footaction (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into champs table.
        elif isinstance(item, ChampsItem):
            self.cursor.execute("INSERT INTO champs (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into eastbay table.
        elif isinstance(item, EastBayItem):
            self.cursor.execute("INSERT INTO eastbay (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into finishline table.
        elif isinstance(item, FinishLineItem):
            self.cursor.execute("INSERT INTO finishline (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into adidas table.
        elif isinstance(item, AdidasItem):
            self.cursor.execute("INSERT INTO adidas (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into nike table.
        elif isinstance(item, NikeItem):
            self.cursor.execute("INSERT INTO nike (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footshop table.
        elif isinstance(item, FootShopItem):
            self.cursor.execute("INSERT INTO footshop (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into caliroots table.
        elif isinstance(item, CalirootsItem):
            self.cursor.execute("INSERT INTO caliroots (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into afew table.
        elif isinstance(item, AfewItem):
            self.cursor.execute("INSERT INTO afew (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into einhalb table.
        elif isinstance(item, EinhalbItem):
            self.cursor.execute("INSERT INTO einhalb (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into end table.
        elif isinstance(item, EndItem):
            self.cursor.execute("INSERT INTO end (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into sns table.
        elif isinstance(item, SNSItem):
            self.cursor.execute("INSERT INTO sns (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into goodwillout table.
        elif isinstance(item, GoodWillOutItem):
            self.cursor.execute("INSERT INTO goodwillout (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into tint table.
        elif isinstance(item, TintItem):
            self.cursor.execute("INSERT INTO tint (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into overkill table.
        elif isinstance(item, OverkillItem):
            self.cursor.execute("INSERT INTO overkill (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footdistrict table.
        elif isinstance(item, FootDistrictItem):
            self.cursor.execute("INSERT INTO footdistrict (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into size table.
        elif isinstance(item, SizeItem):
            self.cursor.execute("INSERT INTO size (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into ycmc table.
        elif isinstance(item, YCMCItem):
            self.cursor.execute("INSERT INTO ycmc (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into city table.
        elif isinstance(item, CityItem):
            self.cursor.execute("INSERT INTO city (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into nordstrom table.
        elif isinstance(item, NordstromItem):
            self.cursor.execute("INSERT INTO nordstrom (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into barneys table.
        elif isinstance(item, BarneysItem):
            self.cursor.execute("INSERT INTO barneys (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into jimmyjazz table.
        elif isinstance(item, JimmyJazzItem):
            self.cursor.execute("INSERT INTO jimmyjazz (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into jdsports table.
        elif isinstance(item, JDSportsItem):
            self.cursor.execute("INSERT INTO jdsports (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footpatrol table.
        elif isinstance(item, FootPatrolItem):
            self.cursor.execute("INSERT INTO footpatrol (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into sneakerbaas table.
        elif isinstance(item, SneakerBaasItem):
            self.cursor.execute("INSERT INTO sneakerbaas (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into sneakerpolitics table.
        elif isinstance(item, SneakerPoliticsItem):
            self.cursor.execute("INSERT INTO sneakerpolitics (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into urbanindustry table.
        elif isinstance(item, UrbanIndustryItem):
            self.cursor.execute("INSERT INTO urbanindustry (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into urbanoutfitters table.
        elif isinstance(item, UrbanOutfittersItem):
            self.cursor.execute("INSERT INTO urbanoutfitters (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into luisa table.
        elif isinstance(item, LuisaItem):
            self.cursor.execute("INSERT INTO luisa (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into slamjam table.
        elif isinstance(item, SlamJamItem):
            self.cursor.execute("INSERT INTO slamjam (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into rise45 table.
        elif isinstance(item, Rise45Item):
            self.cursor.execute("INSERT INTO rise45 (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into undefeated table.
        elif isinstance(item, UndefeatedItem):
            self.cursor.execute("INSERT INTO undefeated (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into zappos table.
        elif isinstance(item, ZapposItem):
            self.cursor.execute("INSERT INTO zappos (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into ubiq table.
        elif isinstance(item, UbiqItem):
            self.cursor.execute("INSERT INTO ubiq (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into pointz table.
        elif isinstance(item, PointzItem):
            self.cursor.execute("INSERT INTO pointz (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into kicks table.
        elif isinstance(item, KicksItem):
            self.cursor.execute("INSERT INTO kicks (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into shoespalace table.
        elif isinstance(item, ShoesPalaceItem):
            self.cursor.execute("INSERT INTO shoespalace (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into stickabush table.
        elif isinstance(item, StickABushItem):
            self.cursor.execute("INSERT INTO stickabush (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into kong table.
        elif isinstance(item, KongItem):
            self.cursor.execute("INSERT INTO kong (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into saveoursole table.
        elif isinstance(item, SaveOurSoleItem):
            self.cursor.execute("INSERT INTO saveoursole (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into inflammable table.
        elif isinstance(item, InflammableItem):
            self.cursor.execute("INSERT INTO inflammable (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into defshop table.
        elif isinstance(item, DefShopItem):
            self.cursor.execute("INSERT INTO defshop (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into offspring table.
        elif isinstance(item, OffSpringItem):
            self.cursor.execute("INSERT INTO offspring (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into solekitchen table.
        elif isinstance(item, SoleKitchenItem):
            self.cursor.execute("INSERT INTO solekitchen (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into drome table.
        elif isinstance(item, DromeItem):
            self.cursor.execute("INSERT INTO drome (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into footasylum table.
        elif isinstance(item, FootAsylumItem):
            self.cursor.execute("INSERT INTO footasylum (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into hhv table.
        elif isinstance(item, HHVItem):
            self.cursor.execute("INSERT INTO hhv (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into concepts table.
        elif isinstance(item, ConceptsItem):	
            self.cursor.execute("INSERT INTO concepts (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into socialstatus table.
        elif isinstance(item, SocialStatusItem):	
            self.cursor.execute("INSERT INTO socialstatus (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into extrabutter table.
        elif isinstance(item, ExtraButterItem):	
            self.cursor.execute("INSERT INTO extrabutter (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into bodega table.
        elif isinstance(item, BodegaItem):	
            self.cursor.execute("INSERT INTO bodega (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into saintalfred table.
        elif isinstance(item, SaintAlfredItem):	
            self.cursor.execute("INSERT INTO saintalfred (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into lapstonenhammer table.
        elif isinstance(item, LapstoneNHammerItem):	
            self.cursor.execute("INSERT INTO lapstonenhammer (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into shelflife table.
        elif isinstance(item, ShelfLifeItem):	
            self.cursor.execute("INSERT INTO shelflife (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into asphaltgold table.
        elif isinstance(item, AsphaltGoldItem):	
            self.cursor.execute("INSERT INTO asphaltgold (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into hanon table.
        elif isinstance(item, HanonItem):	
            self.cursor.execute("INSERT INTO hanon (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into solebox table.
        elif isinstance(item, SoleBoxItem):	
            self.cursor.execute("INSERT INTO solebox (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
            
        # Insert item into consortium table.
        elif isinstance(item, ConsortiumItem):	
            self.cursor.execute("INSERT INTO consortium (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into haven table.
        elif isinstance(item, HavenItem):	
            self.cursor.execute("INSERT INTO haven (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into needsupply table.
        elif isinstance(item, NeedSupplyItem):	
            self.cursor.execute("INSERT INTO needsupply (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into loaded table.
        elif isinstance(item, LoadedItem):	
            self.cursor.execute("INSERT INTO loaded (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into wellgosh table.
        elif isinstance(item, WellGoshItem):	
            self.cursor.execute("INSERT INTO wellgosh (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into capsule table.
        elif isinstance(item, CapsuleItem):	
            self.cursor.execute("INSERT INTO capsule (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into yme table.
        elif isinstance(item, YMEItem):	
            self.cursor.execute("INSERT INTO yme (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into hypedc table.
        elif isinstance(item, HypeDCItem):	
            self.cursor.execute("INSERT INTO hypedc (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into holypop table.
        elif isinstance(item, HolyPopItem):	
            self.cursor.execute("INSERT INTO holypop (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into bstn table.
        elif isinstance(item, BSTNItem):	
            self.cursor.execute("INSERT INTO bstn (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into trophyroom table.
        elif isinstance(item, TrophyRoomItem):	
            self.cursor.execute("INSERT INTO trophyroom (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into sidestep table.
        elif isinstance(item, SideStepItem):	
            self.cursor.execute("INSERT INTO sidestep (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into shiekh table.
        elif isinstance(item, ShiekhItem):	
            self.cursor.execute("INSERT INTO shiekh (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into rezet table.
        elif isinstance(item, RezetItem):	
            self.cursor.execute("INSERT INTO rezet (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into footlockereu table.
        elif isinstance(item, FootLockerEUItem):	
            self.cursor.execute("INSERT INTO footlockereu (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into office table.
        elif isinstance(item, OfficeItem):	
            self.cursor.execute("INSERT INTO office (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into allike table.
        elif isinstance(item, ALLikeItem):	
            self.cursor.execute("INSERT INTO allike (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into sportshoes table.
        elif isinstance(item, SportsShoesItem):	
            self.cursor.execute("INSERT INTO sportshoes (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into runnerspoint table.
        elif isinstance(item, RunnersPointItem):	
            self.cursor.execute("INSERT INTO runnerspoint (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into graffiti table.
        elif isinstance(item, GraffitiItem):	
            self.cursor.execute("INSERT INTO graffiti (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into urbanjungle table.
        elif isinstance(item, UrbanJungleItem):	
            self.cursor.execute("INSERT INTO urbanjungle (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into ssense table.
        elif isinstance(item, SSenseItem):	
            self.cursor.execute("INSERT INTO ssense (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into backdoor table.
        elif isinstance(item, BackDoorItem):	
            self.cursor.execute("INSERT INTO backdoor (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into basket table.
        elif isinstance(item, BasketItem):	
            self.cursor.execute("INSERT INTO basket (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into oneblockdown table.
        elif isinstance(item, OneBlockDownItem):	
            self.cursor.execute("INSERT INTO oneblockdown (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into dopefactory table.
        elif isinstance(item, DopeFactoryItem):	
            self.cursor.execute("INSERT INTO dopefactory (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into nextdoor table.
        elif isinstance(item, NextDoorItem):	
            self.cursor.execute("INSERT INTO nextdoor (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into summer table.
        elif isinstance(item, SummerItem):	
            self.cursor.execute("INSERT INTO summer (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into mrporter table.
        elif isinstance(item, MrPorterItem):	
            self.cursor.execute("INSERT INTO mrporter (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into stormfashion table.
        elif isinstance(item, StormFashionItem):	
            self.cursor.execute("INSERT INTO stormfashion (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into tresbien table.
        elif isinstance(item, TresBienItem):	
            self.cursor.execute("INSERT INTO tresbien (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into packer table.
        elif isinstance(item, PackerItem):	
            self.cursor.execute("INSERT INTO packer (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into addict table.
        elif isinstance(item, AddictItem):	
            self.cursor.execute("INSERT INTO addict (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into aphrodite table.
        elif isinstance(item, AphroditeItem):	
            self.cursor.execute("INSERT INTO aphrodite (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into bait table.
        elif isinstance(item, BaitItem):	
            self.cursor.execute("INSERT INTO bait (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into blends table.
        elif isinstance(item, BlendsItem):	
            self.cursor.execute("INSERT INTO blends (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into nicekicks table.
        elif isinstance(item, NiceKicksItem):	
            self.cursor.execute("INSERT INTO nicekicks (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into clicks table.
        elif isinstance(item, ClicksItem):	
            self.cursor.execute("INSERT INTO clicks (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into feature table.
        elif isinstance(item, FeatureItem):	
            self.cursor.execute("INSERT INTO feature (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into hypebeast table.
        elif isinstance(item, HypeBeastItem):	
            self.cursor.execute("INSERT INTO hypebeast (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into deadstock table.
        elif isinstance(item, DeadStockItem):	
            self.cursor.execute("INSERT INTO deadstock (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into notre table.
        elif isinstance(item, NotreItem):	
            self.cursor.execute("INSERT INTO notre (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into nrml table.
        elif isinstance(item, NrmlItem):	
            self.cursor.execute("INSERT INTO nrml (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into oneness table.
        elif isinstance(item, OnenessItem):	
            self.cursor.execute("INSERT INTO oneness (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into pufferreds table.
        elif isinstance(item, PufferRedsItem):	
            self.cursor.execute("INSERT INTO pufferreds (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into renarts table.
        elif isinstance(item, RenartsItem):	
            self.cursor.execute("INSERT INTO renarts (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into shoesgallery table.
        elif isinstance(item, ShoesGalleryItem):	
            self.cursor.execute("INSERT INTO shoesgallery (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into proper table.
        elif isinstance(item, ProperItem):	
            self.cursor.execute("INSERT INTO proper (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into solestop table.
        elif isinstance(item, SoleStopItem):	
            self.cursor.execute("INSERT INTO solestop (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into titolo table.
        elif isinstance(item, TitoloItem):	
            self.cursor.execute("INSERT INTO titolo (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into uptown table.
        elif isinstance(item, UptownItem):	
            self.cursor.execute("INSERT INTO uptown (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into westnyc table.
        elif isinstance(item, WestNYCItem):	
            self.cursor.execute("INSERT INTO westnyc (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into wishatl table.
        elif isinstance(item, WishATLItem):	
            self.cursor.execute("INSERT INTO wishatl (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into xileclothing table.
        elif isinstance(item, XileClothingItem):	
            self.cursor.execute("INSERT INTO xileclothing (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))

        # Insert item into solefly table.
        elif isinstance(item, SoleflyItem):	
            self.cursor.execute("INSERT INTO solefly (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into patta table.
        elif isinstance(item, PattaItem):	
            self.cursor.execute("INSERT INTO patta (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into svd table.
        elif isinstance(item, SVDItem):	
            self.cursor.execute("INSERT INTO svd (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into dsmny table.
        elif isinstance(item, DSMNYItem):	
            self.cursor.execute("INSERT INTO dsmny (link, date) VALUES (%s, %s)", (item['link'].encode('utf-8'), DATE))
			
        # Insert item into hubbastille table.
        elif isinstance(item, HubbastilleItem):	
			self.cursor.execute("INSERT INTO hubbastille (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        # Insert item into shoesaddictor table.
        elif isinstance(item, ShoesAddictorItem):	
            self.cursor.execute("INSERT INTO shoesaddictor (name, link, date) VALUES (%s, %s, %s)", (item['name'].encode('utf-8'), item['link'].encode('utf-8'), DATE))
			
        self.conn.commit()
		
        # If item name contain below words. Tweet it.
        keywords = ['ultra boost', 'air jordan', 'jordan retro', 'nmd', 'boost', 'retro', 'flyknit', 'yeezy', 'ronnie', 'fieg', 'pharrel', 'atmos', 'clots', 'mars', 'yard']
		
        if any(keyword in item['name'].encode('utf-8').lower() for keyword in keywords):
		  # Twitter Auth - Tweet the item with date, time, item name, and link.
          # To obtain Twitter CONSUMER and ACCESS keys go to https://apps.twitter.com/
          CONSUMER_KEY = 'PASTE CONSUMER_KEY HERE'
          CONSUMER_SECRET = 'PASTE CONSUMER_SECRET HERE'
          ACCESS_TOKEN_KEY = 'PASTE ACCESS_TOKEN_KEY HERE'
          ACCESS_TOKEN_SECRET = 'PASTE ACCESS_TOKEN_SECRET HERE'
          API = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
          TEXT_TO_SEND = DATE + " EST " + item['name'] + " " + item['link']
          TWEET = API.request('statuses/update', {'status': TEXT_TO_SEND})
          print(Fore.RED + 'TWEET LOG SUCCESS: ' + DATE + ' EST ' + item['name'] + ' ' + item['link'] + Style.RESET_ALL if TWEET.status_code == 200 else Fore.RED + 'TWEET LOG FAILURE: FAILED TO TWEET' + Style.RESET_ALL)
		  
		  # WebHook for Discord. Comment/Uncomment the line below to enable/disable.
          # requests.post('DISCORD WEBHOOK URL', data={'content': "**" + item['name'] + "**" + "\n" + item['link'] + "\n" + "\n" + "[ATC]: " + item['size'] + "\n" + "------------" + "\n"})
		  
		  # WebHook for Slack. Comment/Uncomment the line below to enable/disable.
          # requests.post('SLACK WEBHOOK URL', json={'text': "*" + item['name'] + "*" + "\n" + item['link'] + "\n" + "\n" + "[ATC]: " + item['size'] + "\n" + "------------" + "\n"}, headers={'Content-Type': 'application/json'})
		  
    except MySQLdb.Error, e:
      # print (Fore.RED + "MYSQL ERROR %d: %s" % (e.args[0], e.args[1] + Style.RESET_ALL))
      
      return item
