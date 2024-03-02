import requests
import urllib3
from lxml import etree


def go():
    keyword = '复古篮球运动鞋'
    url = 'https://search.jd.com/Search?keyword=' + keyword + '&suggest=1.his.0.0&wq=' + keyword + '&page=3'
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }
    # 暂时忽略警告
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.get(url=url, headers=head, verify=False).text
    tree = etree.HTML(response)
    print(response)
    li_list = tree.xpath("//ul[@class='gl-warp clearfix']/li")
    link_list = []  # 商品链接
    commodity_list = []  # 商品名
    price_list = []  # 商品价格
    for li in li_list:
        # 写入商品链接
        link_list.append('https:' + li.xpath(".//div[@class='p-img']/a/@href")[0])
        # 写入商品名
        if (li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[3]")):
            commodity_list.append(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[1]")[0] +
                                  li.xpath(".//div[@class='p-name p-name-type-2']//em/font[1]/text()")[0] +
                                  li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[2]")[0] +
                                  keyword +
                                  li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[3]")[0]
                                  )
        else:
            commodity_list.append(li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[1]")[0] +
                                  li.xpath(".//div[@class='p-name p-name-type-2']//em/font[1]/text()")[0] +
                                  li.xpath(".//div[@class='p-name p-name-type-2']//em/text()[2]")[0] +
                                  keyword
                                  )
            # 写入商品价格
        price_list.append(li.xpath(".//div[@class='p-price']//i/text()")[0])

        print(link_list)
        print('\n')
        print(commodity_list)
        print('\n')
        print(price_list)


if __name__ == '__main__':
    go()
