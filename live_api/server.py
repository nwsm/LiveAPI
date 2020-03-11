from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

data = {

}

class Data(Resource):
    def post(self, resource):
        json_data = request.get_json(force=True)
        data[resource] = json_data['data']
        print(data)
        return 200
    def get(self, resource):
        return data[resource], 200

api.add_resource(Data, '/<resource>')

if __name__ == '__main__':
    app.run(debug=True, port=3000)