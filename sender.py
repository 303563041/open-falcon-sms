#-*- coding: utf-8 -*-
from message_xsend import MESSAGEXsend
from app_configs import MESSAGE_CONFIGS
from flask import Flask, request
from flask.ext import restful
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
api = restful.Api(app)

class sendMessage(restful.Resource):
    def get(self):
        return "message"
    def post(self):
        cellPhone = request.form['tos']
        content = request.form['content']
        submail = MESSAGEXsend(MESSAGE_CONFIGS)
        submail.add_to(cellPhone)
        submail.set_project("RIEdd4")
        submail.add_var('txt', content)
        return submail.xsend()

class sendCall(restful.Resource):
    def get(self):
        return "call"

    def post(self):
        _to = request.form['tos']
        _message = request.form['content']
        message_url = "http://sms-api.xxxxxxxx/api/v2/send"

        header = {
            'Token': 'xxxxxx'
        }
    
        body = {
            "type": "call",
            "tel": _to,
            "csc": "86",
            "message": "有报警," + str(_message) + "详情请查看邮件或者打开Duty页面; 有报警," + str(_message) + "详情请查看邮件或者打开Duty页面"
        }
    
        response = requests.post(message_url, data=json.dumps(body), headers=header)
        ret = json.loads(response.text)
        if ret.get('status', 0):
            return True
        else:
            return False


api.add_resource(sendMessage, '/api/v2/message')
api.add_resource(sendCall, '/api/v2/call')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
