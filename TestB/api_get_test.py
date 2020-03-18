import requests

if __name__ == '__main__':
    # jmeter壓力測試工具
    # https: // kennychen - blog.herokuapp.com /

    url = 'http://localhost:8080/house_search'

    # - 【男生可承租】且【位於新北】的租屋物件
    response = requests.get(url, params={'region_name': '新北市', 'sex_requirement': 1})

    # - 以【聯絡電話】查詢租屋物件
    response = requests.get(url, params={'phone': '02-22223333'})

    # - 所有【非屋主自行刊登】的租屋物件
    response = requests.get(url, params={'is_owner': False})

    # - 【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件
    response = requests.get(url, params={'region_name': '台北市', 'owner_sex': 2, 'landlord_first_name': '吳'})