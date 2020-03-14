class house_object(object):
    def __init__(self):
        self.landlord_name = ''
        self.landlord_status = ''
        self.phone = ''
        self.building_type = ''
        self.house_type = ''
        self.sex_requirement = ''

        self.landlord_first_name = ''
        self.region_name = ''

        # Save requment
        #   出租者(陳先生)   'linkman'
        # - 出租者身份(屋主)  'nick_name'
        # - 聯絡電話(02 - 25569419)
        # - 型態(電梯大樓)
        # - 現況(獨立套房) kind_name_img
        # - 性別要求(男女生皆可)

        # Get Parameter
        # - 【男生可承租】且【位於新北】的租屋物件
        # - 以【聯絡電話】查詢租屋物件
        # - 所有【非屋主自行刊登】的租屋物件
        # - 【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件
