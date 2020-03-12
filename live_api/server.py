from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

data = {

}

class Data(Resource):
    def delete(self, resource):
        try:
            del data[resource]
        except KeyError:
            pass
    def post(self, resource):
        json_data = request.get_json(force=True)
        print(json_data)
        if resource in data:
            data[resource] = data[resource] + json_data['data']
        else:
            data[resource] = json_data['data']
        return 200
    def get(self, resource):
        return data[resource], 200

api.add_resource(Data, '/<resource>')

if __name__ == '__main__':
    app.run(debug=True, port=3000)