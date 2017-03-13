Sneaker/Restock Notify via Twitter coded in Python using Scrapy.
#
Status: **Under Development**

Description: Crawl a list of sneaker websites. Once new product goes live or restocks, alert the user via tweet, Twitter with date, time, item name, and link.

#
**Supported Sites List:**
 - 43einhalb
 - AFewStore
 - Adidas
 - Barneys - Block if crawl too much.
 - Caliroots
 - ChampsSports
 - City Gear
 - EastBay
 - End - Captcha if crawl too much.
 - FinishLine
 - FootAction
 - FootDistrict
 - FootLocker
 - FootPatrol
 - FootShop
 - JDSports
 - JimmyJazz
 - Kith
 - Luisa Via Roma
 - Nike
 - Nordstrom
 - OverKill
 - Ruvilla
 - Size
 - SneakerBaas
 - SneakerNStuff
 - SneakerPolitics
 - Tint Footware
 - Urban Industry
 - UrbanOutfitters
 - YCMC
	
#
**Requirements:**
- scrapy
- scrapy-random-useragent
- TwitterAPI
- MySQL-python
- mysql-connector
- crayons
- datetime
- beautifulsoup4

#
**Setup:**
- Install the requirements, above.
- Install the MySQL database -> .sql provided in the folder.
- Go into mysql_pipeline.py edit MySQL connection info.
- Edit Twitter CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, and ACCESS_TOKEN_SECRET.
- To run click on main.py.