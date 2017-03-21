Sneaker/Restock/Monitor Notify via Twitter coded in Python using Scrapy.

![Example](http://i.imgur.com/cqI2s0x.png)
#
Status: **Under Development. If Interested feel free to follow W_Notify on Twitter.**

Description: Crawl a list of sneaker websites. Once the new product is found or is restocked. It will check for certain keywords in the item's name. If found, it will alert the user via Twitter using tweet, with date, time, item name, and link.
#
**Supported Sites List:**
 - 43einhalb
 - 5 Pointz
 - AFewStore
 - ALLike
 - Adidas
 - AsphaltGold
 - BSTN
 - Back Door
 - Barneys - Ban if crawl too much.
 - Basket Store
 - Bodega
 - Caliroots
 - Capsule
 - ChampsSports
 - City Gear
 - Concepts
 - Consortium
 - DefShop
 - Drome
 - EastBay
 - End - Captcha if crawl too much.
 - Extra Butter NY
 - FinishLine - Banned on Vultr.
 - FootAction
 - FootAsylum
 - FootDistrict
 - FootLocker
 - FootPatrol
 - FootShop
 - Hanon
 - Haven
 - HypeDC
 - Inflammable
 - JDSports
 - JimmyJazz - ASN blocked on Vultr via CloudFlare.
 - Kith
 - Kong
 - Lapstone and Hammer
 - Loaded
 - Luisa Via Roma
 - NeedSupply
 - Nike
 - Nordstrom
 - Office
 - Offspring
 - OverKill
 - Rise45
 - Ruvilla
 - SSense
 - SaintAlfred
 - SaveOurSole
 - Shelf Life
 - ShoesPalace - Need to disobey robots.txt, if you want to crawl.
 - Size
 - Slam Jam Socialism
 - SneakerBaas
 - SneakerNStuff - ASN blocked on Vultr via CloudFlare.
 - SneakerPolitics
 - SocialStatus
 - SoleBox
 - SoleKitchen
 - StickABush
 - Tint Footware
 - TrophyRoom
 - Undefeated
 - Urban Industry
 - Urban Jungle
 - Urban Outfitters
 - WellGosh
 - YCMC
 - YME Universe
 - Zappos
#
**Requirements:**
- pip install scrapy
- pip install scrapy-random-useragent
- pip install TwitterAPI
- pip install MySQL-python
- pip install mysql-connector
- pip install crayons
- pip install datetime
- pip install beautifulsoup4
#
**Setup:**
1. Make sure you have Python installed. (Working on 2.7 not sure about 3) To install go to https://www.python.org/
2. Install the requirements above.
- For Mac, to install MySQL-python. Open terminal:
 - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
 - brew install mysql-connector-c
 - pip install MySQL-python
 
3. Install the MySQL database -> .sql file provided in the folder.
4. Go into mysql_pipeline.py edit MySQL connection info and edit Twitter's CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, and ACCESS_TOKEN_SECRET to your Twitter account's info.

5. To run:
 - For Windows: Click on main.py
 - For Mac: Open terminal on the folder type python main.py