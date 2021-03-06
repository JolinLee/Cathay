ROOT_URL = "https://rent.591.com.tw"
API_URL = "https://rent.591.com.tw/home/search/rsList"

HEADERS = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36",
}

CONDITIONS = {
    'is_new_list': '1',
    'type': '1',
    'kind': '0',  # 1
    'searchtype': '1',
    'regionid': '3'  # 1 台北市   3 新北市
    # 'rentprice': '0,26000',
    # 'patternMore': '2',
    # 'option': 'cold',
    # 'hasimg': '1',
    # 'not_cover': '1',
}

region_key = {
    '台北市': 1,
    '新北市': 3
}

WEB_URL_FORMAT_STR = "https://rent.591.com.tw/rent-detail-{}.html"

PARSE_INTERVAL_IN_SECONDS = 1800