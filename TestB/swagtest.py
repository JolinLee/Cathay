import random
from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
Swagger(app)

@app.route('/house_search/', methods=['GET'])
def index(language):
    """
        ---
        tags:
          - 591租屋網 查詢系統
        parameters:
          - name: region_name
            in: query
            type: string
            description: 縣市(台北市,新北市)
          - name: sex_requirement
            in: query
            type: int
            description: 性別需求 (1.限男 2.限女 3.男女皆可)
          - name: phone
            in: query
            type: string
            description: 聯繫電話 (02-22223333)
          - name: home_owner
            in: query
            type: string
            description: 刊登者身分
          - name: home_owner
            in: query
            type: string
            description: 屋主姓氏
        """
    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic",
        "simple", "powerful", "amazing",
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )


app.run(debug=True)