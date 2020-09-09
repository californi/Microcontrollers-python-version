from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import pika

app = Flask(__name__)
api = Api(app)

class SendingData(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #If i am here, then status_code == 200
        id = str(postedData["id"])
        description = str(postedData["description"])
        messageBody = 'Id: ' + id + ' - Description: ' + description

        parameters = pika.URLParameters('amqp://guest:guest@172.17.0.3:5672/%2f')
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue='monitoring-queue')
        channel.basic_publish('',
                            'monitoring-queue',
                            messageBody,
                            pika.BasicProperties(content_type='text/plain',
                                                    delivery_mode = 1))
        connection.close()   


        #Step 2: Add the posted data

        retMap = {
            'Message': messageBody,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(SendingData, "/proactive-monitoring/sendingdata")

@app.route('/')
def hello_world():
    return "Hello World! - amqp://guest:guest@172.17.0.3:5672"


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)