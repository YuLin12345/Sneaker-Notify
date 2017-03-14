Sneaker/Restock Notify via Twitter coded in Python using Scrapy.
#
Status: **Under Development. If Interested feel free to follow W_Notify on Twitter**

Description: Crawl a list of sneaker websites. Once new product goes live or restocks and contains certain keywords, alert the user via tweet, Twitter with date, time, item name, and link.

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
 - SlamJam
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