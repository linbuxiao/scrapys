import scrapy
import scrapy_splash


class VideoSpider(scrapy.Spider):
    name = "video"
    allowed_domains = ["www.yhdmp.cc"]

    def __init__(self, id=None, name=None, **kwargs):
        self.id = id
        super().__init__(name, **kwargs)

    def start_requests(self):
        url = f"https://www.yhdmp.cc/showp/{self.id}.html"
        yield scrapy_splash.SplashRequest(url, self.parse, args={"wait": 1.0})

    def parse(self, response):
        block = response.xpath("//div[@class='movurl'][@style='display:block']")[0]
        all_hrefs = block.xpath("./ul/li/a/@href").extract()
        for href in all_hrefs:
            yield scrapy_splash.SplashRequest(
                f"https://www.yhdmp.cc{href}", self.parse_episode, args={"wait": 1.5}
            )

    def parse_episode(self, response):
        pass
