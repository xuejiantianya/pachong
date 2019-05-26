# -*- coding: utf-8 -*-

# Scrapy settings for zhihuuser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihuuser'

SPIDER_MODULES = ['zhihuuser.spiders']
NEWSPIDER_MODULE = 'zhihuuser.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihuuser (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    # 'cookie':'_zap=6637de17-ad2b-4516-8e52-06bac50eca1b; d_c0="AHCh2gBpwg6PTqi8QdQCbSffRkdo1b2wekg=|1546344814"; __guid=74140564.4418409432180674600.1546344801561.385; __gads=ID=d7620f1e811503bf:T=1553521480:S=ALNI_MbLa8CK0y1x_PuO1FB2Zlsq8zW2AQ; UM_distinctid=16a10f3d84a378-0414eefa28ffa1-3c604504-1fa400-16a10f3d84b880; _ga=GA1.2.912074659.1551000576; q_c1=ddd4b2095e87456e90a80910c7c67dad|1556186525000|1550834144000; tst=h; _xsrf=cXQsGtm2DbsAz4xJoFuDxtuQr8rL72ns; CNZZDATA1272960301=234264353-1555059137-%7C1558784486; capsion_ticket="2|1:0|10:1558784906|14:capsion_ticket|44:NGMyZDEzYWIyZmMyNDE4YTlmNTM4NmFhMmY2YWRkMWQ=|7ed0e0d60271b004c8dae37cf3578fd28fbb20f1e378619589ea78103405c168"; z_c0="2|1:0|10:1558784919|4:z_c0|92:Mi4xUTBzYkR3QUFBQUFBY0tIYUFHbkNEaVlBQUFCZ0FsVk5sM25XWFFDd3VSUVk2VEpPRFhIOWNSQUcyVkFsdF9WOC1R|c30b51a1c41da9951405f6f8f95a53f18a3d247ea992c24059b0b013434d92f5"; __utma=51854390.912074659.1551000576.1558527979.1558784900.74; __utmb=51854390.0.10.1558784900; __utmc=51854390; __utmz=51854390.1558784900.74.73.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/hot; __utmv=51854390.100-1|2=registration_date=20190405=1^3=entry_date=20190222=1; tgw_l7_route=7c109f36fa4ce25acb5a9cf43b0b6415; monitor_count=31',

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihuuser.middlewares.ZhihuuserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'zhihuuser.pipelines.MongoPipeline': 300,
  # 'zhihuuser.pipelines.MoonBlogPipeline': 300,
  'zhihuuser.pipelines.WangyinPipeline_a': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MONGO_URI = 'localhost'
MONGO_DATABASE = 'zhihu'
