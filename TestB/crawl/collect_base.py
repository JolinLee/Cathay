import requests

from TestB.crawl.rent_house_591 import Rent_House_591
from TestB.adapter.house_repository import save_house

class CollectBase():
    def __init__(self, use_module):
        self.crawl_hash = {
            'house_591': Rent_House_591
        }
        session = requests.Session()
        self.crawl_module = self.crawl_hash[use_module]('', session)

    def search(self, region):

        self.crawl_module.content_download()
        collect_region_house = self.crawl_module.search_house(region)
        print(collect_region_house)
        save_house(collect_region_house)
