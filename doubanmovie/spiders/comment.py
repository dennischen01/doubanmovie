import scrapy

from doubanmovie.items import DoubanmovieItem

import csv

with open('/Users/cxc/PycharmProjects/doubanmovie/doubanmovie/spiders/res.csv', newline='') as f:
    reader = csv.reader(f)
    # data = []
    url = []
    quote = []
    rank = []
    rate = []
    star = []
    title = []
    for row in reader:
        # ata.append(row)
        url.append(row[+0])
        quote.append(row[+1])
        rank.append(row[+2])
        rate.append(row[+3])
        star.append(row[+4])
        title.append(row[+5])
        #print(row)


class DoubanSpider(scrapy.Spider):
    name = 'comment'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/review/1000369/#comments']
    i = 1
    def parse(self, response):


        item = DoubanmovieItem()
        item['rank'] = rank[self.i]
        item['title'] = title[self.i]
        item['star'] = star[self.i]
        item['rate'] = rate[self.i]
        item['quote'] = quote[self.i]
        item['detail'] = response.xpath('//*[@id="link-report"]').extract()[0]
        self.i = self.i + 1
        yield item
        if self.i < 250:
            yield scrapy.Request(url[self.i], self.parse)


