# Scrapy settings for iqiyi project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "iqiyi"

SPIDER_MODULES = ["iqiyi.spiders"]
NEWSPIDER_MODULE = "iqiyi.spiders"
FEED_EXPORT_FIELDS = ['排行','标题','封面','描述','发行年份','类型','主演','评分','评价人数']


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8
# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'application/json, text/plain, */*',
	# 'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
	'origin': 'https://www.iqiyi.com',
	'referer': 'https://www.iqiyi.com/',
	'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"`',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
	'cookie':'RK=dt88cd0MOT; ptcz=7a597f6e0c1de68af26bdba301568b5d3e7daf4e9a34235065a54914e0c6feab; tab_experiment_str=100000; video_guid=adfffb53111e4479; qq_domain_video_guid_verify=adfffb53111e4479; _qimei_uuid42=17b12172e08100580f606a5227a8c931566dcb0c99; _qimei_fingerprint=f85deceea7f0f4901886bebd1a815027; pgv_info=ssid=s6244175190; ts_refer=www.baidu.com/link; pgv_pvid=3833364556; ts_uid=7257316950; bucket_id=0; video_platform=2; _qimei_q36=; _qimei_h38=52f7c5d40f606a5227a8c9310200000b117b12; player_spts=40|0|false|false|true|true|false; ts_last=v.qq.com/biu/ranks/; ptag=www_baidu_com'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "iqiyi.middlewares.IqiyiSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "iqiyi.middlewares.IqiyiDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "iqiyi.pipelines.IqiyiPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "gbk"
LOG_LEVEL = "WARNING"
