import requests

if __name__ == '__main__':
    from TestB.crawl.collect_base import CollectBase
    # 爬取 591租屋網，台北、新北的資料.
    collect = CollectBase('house_591')
    collect.search('新北市')
    collect.search('台北市')

    response = requests.get('http://httpbin.org/get', params={'region_name': '台北市'})
    print(response)



