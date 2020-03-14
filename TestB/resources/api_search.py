from flask_restful import Resource, reqparse

from TestB.tools.api_result import apiResult

from TestB.adapter.house_repository import search_house
class House_Search(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('region_name', type=str, default='', required=False,
                                   location=['args'])
        self.reqparse.add_argument('sex_requirement', type=int, default='', required=False,
                                   location=['args'])
        self.reqparse.add_argument('phone', type=int, default='', required=False,
                                   location=['args'])
        self.reqparse.add_argument('home_owner', type=bool, default='', required=False,
                                   location=['args'])
        self.reqparse.add_argument('landlord_first_name', type=str, default='', required=False,
                                   location=['args'])
    def get(self):
        # - 【男生可承租】且【位於新北】的租屋物件
        # - 以【聯絡電話】查詢租屋物件
        # - 所有【非屋主自行刊登】的租屋物件
        # - 【臺北】【屋主為女性】【姓氏為吳】所刊登的所有租屋物件

        try:
            arg = self.reqparse.parse_args()
            data = search_house(arg)
            return apiResult(200, data, 'Get rent house success')
        except Exception as e:
            return apiResult(500, str(e), 'something wrong: ' + str(e))

