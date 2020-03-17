from flask_restful import Resource, reqparse
from flask import request
from TestB.tools.api_result import apiResult

# from TestB.adapter.house_repository import search_house
class House_Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('region_name', type=str, default='', required=False, location=['args', 'json'])
        self.reqparse.add_argument('sex_requirement', default=0, type=int, required=False, location=['args'])
        self.reqparse.add_argument('phone', type=str, default='', required=False, location=['args'])
        self.reqparse.add_argument('is_owner', type=bool, required=False, location=['args'])
        self.reqparse.add_argument('landlord_first_name', default='', type=str, required=False, location=['args'])
        self.reqparse.add_argument('owner_sex', type=int, default=0, required=False, location=['args'])
    def get(self):
        # - 【男生可承租】且【位於新北】的租屋物件
        # - 以【聯絡電話】查詢租屋物件
        # - 所有【非屋主自行刊登】的租屋物件
        # - 【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件

        try:
            arg = self.reqparse.parse_args()
            request
            # data = search_house(arg)
            data = {"rent_list":[[
       {
        "landlord_name": "吳小姐",
"landlord_status":"屋主",
"phone":"02-22223333",
"building_type":"公寓",
"house_type": "獨立套房",
"sex_requirement": 1,
"own_sex": 2,
"landlord_first_name": "吳",
"region_name": "台北市",
"is_own": True
      }
  ]]}
            return apiResult(200, data, 'Get rent house success')
        except Exception as e:
            return apiResult(500, str(e), 'something wrong: ' + str(e))

