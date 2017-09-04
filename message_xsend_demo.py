#-*- coding: utf-8 -*-
from message_xsend import MESSAGEXsend
from app_configs import MESSAGE_CONFIGS
from flask import Flask, request
from flask.ext import restful
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
api = restful.Api(app)

class sendMessage(restful.Resource):
    def get(self):
        return "xxxxxxxxxx"
    def post(self):
        cellPhone = request.form['tos']
        content = request.form['content']
        submail = MESSAGEXsend(MESSAGE_CONFIGS)
        submail.add_to(cellPhone)
        submail.add_var("txt", content)
        #content = '【liang.chen】{0}'.format(test.decode('utf8'))
        submail.set_project(content)
        return submail.xsend()
api.add_resource(sendMessage, '/api/v2/send')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)