import json
import datetime
from bson import ObjectId


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return json.JSONEncoder.default(self, obj)


# http code status
status = {
    200: 'OK',
    400: 'Bad Request',
    404: 'Not Found',
    405: 'Method Not Allowed',
    500: 'Internal Server Error'
}

# http code description (default)
default_description = {
    200: 'Successful response',
    400: 'Please check paras or query valid.',
    404: 'Please read the document to check API.',
    405: 'Please read the document to check API.',
    500: 'Please contact api server manager.'
}


# cdumpsommon return model
def apiResult(code, data, description="", project_id=0, model_id=0):
    data = json.loads(json.dumps(data, cls=DateEncoder))
    description = default_description.get(code) if description == "" else description
    response = {
        "code": code,
        "status": status.get(code),
        "data": data,
        "description": description
    }

    return response
