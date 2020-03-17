import numpy as np
from bs4 import BeautifulSoup

from TestB.tools.html_parser import html_parser, get_url_parameter
from TestB.model.house_model import house_object

class Rent_House_591(object):
    def __init__(self, param, session):
        self.source_name = 'rent_house_591'
        self.source_ch_name = '591租屋網'
        self.source_url = "https://rent.591.com.tw/home/search/rsList"
        self.source_site_url = 'https://rent.591.com.tw'

        self.header = {
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "en-US,en;q=0.9",
            'connection': "keep-alive",
            'dnt': "1",
            'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
        }

        self.param = param
        self.session = session
        self.cache = set()

    def content_download(self):
        # 1.訪問 token
        self._set_csrf_token()
        return 1

    def search_house(self, region):
        page_list, total_rows = self._get_pages(region, self.session)
        all_region_house = []

        for row in page_list[0:3]:
            url_filter = get_url_parameter(region, row, total_rows)
            temp_region_house = self._search_houses_process(url_filter)
            all_region_house = all_region_house + temp_region_house

        return all_region_house

    def _set_csrf_token(self):
        r = self.session.get(self.source_site_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for tag in soup.select('meta'):
            if tag.get('name', None) == 'csrf-token':
                csrf_token = tag.get('content')
                self.session.headers = self.header
                self.session.headers['X-CSRF-TOKEN'] = csrf_token
        else:
            print('No csrf-token found')

    def _get_pages(self, region, session):
        parameter = get_url_parameter(region)
        response = session.get(self.source_url, params=parameter)

        try:
            data = response.json()['data']
        except Exception:
            raise
        else:
            page_html = data.get('page', [])

            page_total = html_parser(page_html)
            pages_counts = (page_total / 30) + 1
            page_row = np.arange(pages_counts)

            page_row = page_row * 30
            page_row = [int(i) for i in page_row]
            return page_row, page_total

    def _search_houses_process(self, url_filter):
        houses = self._get_houses(url_filter)
        house_array = []
        for house in houses:
            if house['post_id'] in self.cache:
                continue

            # 回傳 house dict物件
            house_array.append(self._log_house_info(house))
            self.cache.update([house['post_id']])

        return house_array

    def _get_houses(self, url_filter):
        # logger.info('requests 591 API...')
        response = self.session.get(self.source_url, params=url_filter)

        try:
            data = response.json()['data']
        except Exception:
            raise
        else:
            houses = data.get('data', [])

            for house in houses:
                yield house

    def _log_house_info(self, house):
        name = (
            "名稱：{}-{}-{}".format(
                house['region_name'],
                house['section_name'],
                house['fulladdress'],
            )
        )
        # weburl = ("網址：{}".format(WEB_URL_FORMAT_STR.format(house['post_id'])))
        rent_price = ("租金：{} {}".format(house['price'], house['unit']))
        space = ("坪數：{} 坪".format(house['area']))
        layout = ("格局：{}".format(house['layout']))

        # refresh_time = ("更新時間：{}".format(time.ctime(house['refreshtime'])))

        house_obj = house_object()
        # 刊登者姓名
        house_obj.landlord_name = house['linkman']
        # 刊登者身分
        nick_array = house['nick_name'].split(' ')
        house_obj.landlord_status = nick_array[0] if len(nick_array) > 0 else ''
        # 聯繫電話
        house_obj.phone = 0
        # 建築型態
        house_obj.building_type = ''
        # 房屋格局
        house_obj.house_type = house['kind_name_img']
        # 性別要求
        house_obj.sex_requirement = 0

        linkman = house['linkman'][0]
        # 屋主性別
        house_obj.owner_sex = 1 if '先生' in linkman else 2

        # 租屋者姓氏
        linkman = (linkman.replace('先生', '')).replace('小姐', '')
        house_obj.landlord_first_name = linkman

        # 地區
        house_obj.region_name = house['region_name']

        # 屋主親自刊登
        house_obj.is_owner = True if house_obj.landlord_status == '屋主' else False

        house_dict = house_obj.__dict__
        return house_dict


