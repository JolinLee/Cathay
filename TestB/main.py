import requests

if __name__ == '__main__':
    from TestB.crawl.collect_base import CollectBase
    # 爬取 591租屋網，台北、新北的資料.
    collect = CollectBase('house_591')
    collect.search('新北市')
    collect.search('台北市')

    response = requests.get('http://httpbin.org/get', params={'region_name': '台北市'})
    print(response)

    # requ('https://rent.591.com.tw/home/search/rsList?is_new_list=1&type=1&kind=0&searchtype=1&region=1')
    # GitHub
    # https://github.com/M157q/sgl
    # 完整範例
    # https://heima0809.pixnet.net/blog/post/402619613-180222_parser_%E7%88%AC591

    # 部分範例
    # https://medium.com/@p50305peter/591%E7%A7%9F%E5%B1%8B%E7%B6%B2%E7%88%AC%E8%9F%B2-f70c6ecc5942


