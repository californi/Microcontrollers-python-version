from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BReplyingToA(Resource):
    def post(self):
        #If I am here, then the resouce Add was requested using the method POST

        #Step 1: Get posted data:
        postedData = request.get_json()

        #If i am here, then status_code == 200
        id = str(postedData["id"])
        message = str(postedData["message"])

        # Requesting self-diagnosis
        messageReturn = {
            'id': id, 
            'message': message + ' - Message from Selfdiagnosis'
        }
        print('executing BReplyingToA')

        return jsonify(messageReturn)


api.add_resource(BReplyingToA, "/selfdiagnosis/breplyingtoa")


@app.route('/')
def hello_world():
    return "Hello World! -- from selfdiagnosis"


if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)