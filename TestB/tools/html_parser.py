from bs4 import BeautifulSoup

from TestB.constants import CONDITIONS, region_key


def html_parser(html):
    # 以 Beautiful Soup 解析 HTML 程式碼
    soup = BeautifulSoup(html, 'html.parser')
    print(soup)
    page = soup.find("a", {"class": "pageNum-form"})

    return int(page.get('data-total'))


def get_url_parameter(region, row=None, totalRows=None):
    result = CONDITIONS
    if region is not None:
        result['regionid'] = region_key[region]

    if (row is not None) & (totalRows is not None):
        result['firstRow'] = row
        result['totalRows'] = totalRows

    return result

if __name__ == '__main__':
    html_doc = '<a class=\"pagePrev first\"><span>上一頁</span></a><span class=\"pageCurrent\">1</span><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"30\" data-total=\"12409\" >2</a><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"60\" data-total=\"12409\" >3</a><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"90\" data-total=\"12409\" >4</a><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"120\" data-total=\"12409\" >5</a><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"150\" data-total=\"12409\" >6</a><span class=\"pageBreak\">...</span><a class=\"pageNum-form\" href=\"javascript:;\"  data-first=\"12390\" data-total=\"12409\" >414</a><a href=\"javascript:;\" data-first=\"30\" data-total=\"12409\"  class=\"pageNext\"><span>下一頁</span></a><span class=\"TotalRecord\">&nbsp;&nbsp;共 <span class=\"R\">12409 </span>筆</span>'

    data_total = html_parser(html_doc)
    print(data_total)
