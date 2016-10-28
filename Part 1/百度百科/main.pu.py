# -*-coding:utf-8-*-
import url_manager
import html_downloader
import html_output
import html_parser


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.output = html_output.HtmlOutput()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d: %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.output.collect_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print 'craw failed'
        self.output.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/link?url=X4gv-acrN5Lc6HS9SRYyEGfTXb-n-WUUYfNGak1O1m5OI7E2fO2F2k2az_nsj_0R25pw2w5CouAXmOohUnS4Ya"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)













