# -*- encoding:utf-8 -*-
from damai import DamaiSpider
from douban import DoubanSpider
from huodongxing import HuodongxingSpider
from timer import SchedTimer
import thread


def runCrawlers():
    damaiSpider = DamaiSpider()
    doubanSpider = DoubanSpider()
    huodongxingSpider = HuodongxingSpider()
    #crawling with multi-threads
    thread.start_new_thread(damaiSpider.crawl,())
    thread.start_new_thread(doubanSpider.crawl,())
    thread.start_new_thread(huodongxingSpider.crawl,())

if __name__=="__main__":
    t = SchedTimer(24,00,00)
    t.start(runCrawlers)
