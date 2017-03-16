Sneaker/Restock Notify via Twitter coded in Python using Scrapy.
#
Status: **Under Development. If Interested feel free to follow W_Notify on Twitter.**

Description: Crawl a list of sneaker websites. Once the new product is found or is restocked. It will check for certain keywords in the item's name. If found, it will alert the user via Twitter using tweet, with date, time, item name, and link.

#
**Supported Sites List:**
 - 43einhalb
 - 5 Pointz
 - AFewStore
 - Adidas
 - Barneys - Ban if crawl too much.
 - Caliroots
 - ChampsSports
 - City Gear
 - EastBay
 - End - Captcha if crawl too much.
 - FinishLine - Banned on Vultr.
 - FootAction
 - FootDistrict
 - FootLocker
 - FootPatrol
 - FootShop
 - JDSports
 - JimmyJazz - ASN blocked on Vultr via CloudFlare.
 - Kith
 - Kong
 - Luisa Via Roma
 - Nike
 - Nordstrom
 - OverKill
 - Rise45
 - Ruvilla
 - SaveOurSole
 - ShoesPalace - Need to disobey robots.txt, if you want to crawl.
 - Size
 - Slam Jam Socialism
 - SneakerBaas
 - SneakerNStuff - ASN blocked on Vultr via CloudFlare.
 - SneakerPolitics
 - StickABush
 - Tint Footware
 - Undefeated
 - Urban Industry
 - Urban Outfitters
 - YCMC
 - Zappos
 
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
- Make sure you have Python installed: https://www.python.org/
- Open CMD (Windows) or Terminal (Mac) pip install the requirements above.

- For Mac, to install MySQL-python. Open terminal:
 - /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
 - brew install mysql-connector-c
 - pip install MySQL-python

- Install the MySQL database -> .sql provided in the folder.
- Go into mysql_pipeline.py edit MySQL connection info and edit Twitter CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, and ACCESS_TOKEN_SECRET to your Twitter account.

- To run:
- For Windows:
 - Click on main.py
- For Mac:
 - Open terminal on the folder type python main.py