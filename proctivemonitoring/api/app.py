from flask import Flask, jsonify, request
from flask_restful import Api, Resource

import pika
import requests

app = Flask(__name__)
api = Api(app)


#https://www.nylas.com/blog/use-python-requests-module-rest-apis/#:~:text=How%20to%20Use%20Python%20Requests%20with%20REST%20APIs,-Now%2C%20let's%20take&text=The%20GET%20method%20is%20used,function%20to%20do%20exactly%20this.&text=The%20response%20object%20contains%20all,headers%20and%20the%20data%20payload.

class ARequestingToB(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #If i am here, then status_code == 200
        id = str(postedData["id"])
        message = str(postedData["message"])

        # Requesting self-diagnosis
        query = {
            'id': id, 
            'message':message + ' - Message from ProactiveMonitoring'
        }

        print('executing ARequestingToB')

        response = requests.get('http://microcontrollers.com/selfdiagnosis/breplyingtoa/', params=query)

        print('executing ARequestingToB')

        return response.json()


api.add_resource(ARequestingToB, "/proactive-monitoring/arequestingtob")

@app.route('/')
def hello_world():
    return "Hello World! -- from proactive"


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000)