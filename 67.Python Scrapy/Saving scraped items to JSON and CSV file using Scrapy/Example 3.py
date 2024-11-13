BOT_NAME = 'gfg_friendshipquotes'

SPIDER_MODULES = ['gfg_friendshipquotes.spiders']
NEWSPIDER_MODULE = 'gfg_friendshipquotes.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Desired file format
FEED_FORMAT = "json"

# Name of the file where
# data extracted is stored
FEED_URI = "friendshipfeed.json"
