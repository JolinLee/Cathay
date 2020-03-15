from flask import Flask, request, jsonify, make_response
from flask.json import JSONEncoder
from flask_restful import Api
from datetime import date, datetime
import traceback
from flasgger import Swagger

from TestB.tools.api_result import apiResult
from TestB.resources.api_search import House_Search

from flask_restful import Resource

class PrintHelloWorld(Resource):
    def get(self):
        return {
                   'message': 'Hello World!'
               }, 200

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.strftime("%Y-%m-%d")
            elif isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')

            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)

app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
api = Api(app)

# swagger_config = Swagger.DEFAULT_CONFIG
Swagger(app)

api.add_resource(PrintHelloWorld, "/print_hello")
api.add_resource(House_Search, '/house_search')

@app.before_request
def before_request():
    print('before_request')
    msg = ('info', "User requests info, path: {0}, method: {1}, ip: {2}, agent: {3}"
           .format(str(request.path), str(request.method), str(request.remote_addr), str(request.user_agent)))
    # write_log(LogMesgLevel.INFO, msg)

    # input parameter
    # request.args [Get]
    # json.loads(request.data)
    log_parm = {
        'API_url': request.path,
        'method': request.method,
        'request_ip': request.remote_addr,
        'request_status': 'before',
        'error_level': 'INFO',
        'system_alarm': '',
        'user_alarm': '',
        'exception_msg': ''
    }


@app.after_request
def after_request(response):
    resp = response.get_json()

    if response.status_code == 400 and 'message' in resp:
        resp = apiResult.result(400, {},
                                resp['message'][list(resp['message'].keys())[0]] if len(resp['message'].keys()) else '')

    print('response content:   ', resp)

    if resp is not None:
        code, status, description, data = resp["code"], resp["status"], resp["description"], resp['data']
        project_id, model_id = 0, 0

        response_info = "Server response info, code: {0}, status: {1}, description: {2}"

        log_parm = {
            'API_url': request.path,
            'method': request.method,
            'request_ip': request.remote_addr,
            'request_status': 'after',
            'error_level': '',
            'system_alarm': '',
            'user_alarm': description,
            'exception_msg': ''
        }

        if code == 500:
            # write_log(LogMesgLevel.WARNING, response_info.format(code, status, description + str(data)))
            log_parm['error_level'] = 'ERROR'
            log_parm['exception_msg'] = str(data)
        else:
            # write_log(LogMesgLevel.INFO, response_info.format(code, status, description))
            log_parm['error_level'] = 'INFO'

    else:
        resp = apiResult.result(200, {})

    json_resp = jsonify(resp)
    json_resp.headers['Access-Control-Allow-Origin'] = '*'
    json_resp.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS, *'
    json_resp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type, Accept, *'
    return make_response(json_resp, resp["code"])


@app.errorhandler(Exception)
def all_exception_handler(e):
    description = str(e)
    return apiResult.result(500,
                            traceback.format_exc(),
                            description)

if __name__ == '__main__':

    app.config['JSON_AS_ASCII'] = False

    # Runing Flask
    # app.run(host="0.0.0.0", port=5010, debug=False)
    app.run(host="0.0.0.0", port=8080, debug=True)


