import requests
import urllib3
from lxml import etree
import random
import time

'''
该工具模块为爬虫模块
'''


# 榜单爬虫
class RankScraper:
    def do_scraper(self):
        url = self.website
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'
            # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
            # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        cookies = {
            '_ga': 'GA1.1.1674762085.1683790199',
            '__bid_n': '18809b8599fcc24f564207',
            'FPTOKEN': 'aVv4v4/6vhQZrw0vn4YtMM0E/1Z97hOObQ8EZZdUTaI14aKlKXIezfAYbvRA0CaXhof9wDM77yvCVluXHvdWVUkSK4WrfBGQdLPYWdTBsLIUgMNfSpzExdUAZhyTm0F+ktzempKsuuKOELvTMHHMHqnGjbp19xFfo0+Rt6GHcUHbwLSEFJi7zAJikLzC3Ag1pO6ks7Jn85BEQ+Je6XVbTiGVC0l58oJ/FExvpqwwCDVDto0AapT0IxVSIGSJlgsg691NWZDfcIPeOYEnYSfp/I/vSmED60X0bN7wIZklKQ5rdp4OreGknq/YmGNr42+acqo8/Nw/AMlFPSvwjmntTOywjpmUG1vN7g5pRWcci1fC+kbTnWH3jOASgOXr2ab+E3JF6oUMB9OXyfEXN6d4eQ==|Pm7CQyINX02ZB77X7OneWuZewqIjKT+pO6GGGhUXCcw=|10|a84c66270f149afc858f731f7ca33611',
            'Hm_lvt_5055f6fc5d5d86dc5b6ad4e29f6c10b1': '1683898171,1683990121,1684037518,1684052025',
            'PHPSESSID': 'tkgtv7b8qarbusqsr588fl3a8m',
            '_history': 'cid:105,cid:1033,cid:7429,cid:9906,cid:109,cid:1034,cid:1040,cid:1038,cid:5606,cid:1020,cid:1035,cid:9914,cid:1032,cid:5853,cid:10106,cid:10304,cid:7705',
            'Hm_ck_vcid': 'BTjXyM0rv0iZ%2FZU1abCyg8ZYz1WQFft9VAanXhyNjRg%3D',
            'Hm_lpvt_5055f6fc5d5d86dc5b6ad4e29f6c10b1': '1684052714',
            '_ga_5CSQSY7EJ0': 'GS1.1.1684052026.12.1.1684052722.0.0.0'
        }
        # 暂时忽略警告
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        delay = random.uniform(2, 5)  # 生成2到5之间的随机延时秒数
        time.sleep(delay)  # 延时等待
        # 忽略ssl认证
        response = requests.get(url=url, headers=head, verify=False, cookies=cookies, timeout=25).text
        final_response = response.encode('utf-8').decode('utf-8')
        tree = etree.HTML(final_response)
        # 品牌排行
        band_list = tree.xpath("//table[@class='rank']/tbody/tr/th[2]/a/span/text()")
        # 对应品牌描述
        band_description_list = tree.xpath("//table[@class='rank']/tbody/tr/th[3]/text()")
        result_dict = {
            'band_list': band_list,
            'band_description_list': band_description_list
        }
        print(result_dict)
        return result_dict

    def __init__(self, website):
        self.website = website


# 商品爬虫
class CommodityScraper:
    def do_scraper(self):
        keyword = self.keyword
        url = 'https://search.jd.com/Search?keyword=' + keyword + '&suggest=1.his.0.0&wq=' + keyword + '&page=1'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
        }
        # 暂时忽略警告
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url=url, headers=head, verify=False).text
        print(response)
        tree = etree.HTML(response)
        li_list = tree.xpath("//ul[@class='gl-warp clearfix']/li")
        print(li_list)
        link_list = []  # 商品链接
        commodity_list = []  # 商品名
        price_list = []  # 商品价格
        for li in li_list:
            # 写入商品链接
            link_list.append('https:' + li.xpath(".//div[@class='p-img']/a/@href")[0])
            # 写入商品名(第二、三个描述可能不存在)
            if (li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[3]")):
                commodity_list.append(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[1]")[0] +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/font[1]/text()")[0] +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[2]")[0] +
                                      keyword +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[3]")[0]
                                      )
            elif (li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[2]")[0]):
                commodity_list.append(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[1]")[0] +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/font[1]/text()")[0] +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[2]")[0] +
                                      keyword
                                      )
            else:
                commodity_list.append(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[1]")[0] +
                                      li.xpath(".//div[@class='p-name p-name-type-2']//em/font[1]/text()")[0] +
                                      keyword
                                      )
            # 写入商品价格
            price_list.append(li.xpath(".//div[@class='p-price']//i/text()")[0])
        return link_list, commodity_list, price_list

    def __init__(self, keyword):
        self.keyword = keyword
