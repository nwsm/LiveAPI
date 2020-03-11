import os
import requests
import json

class LiveAPI:
    def createAPI(self):
        os.system('python server.py')
    def updateData(self, resource):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        requests.post('http://localhost:3000/'+resource.name, data=json.dumps({"data": resource.value}), headers=headers)
    def getData(self, resource):
        return requests.get('http://localhost:3000/'+resource)

class Resource:
    def __init__(self, api, name, value):
        self.name=name
        self.value=value
        self.api=api
        if value != None:
            self.api.updateData(self)
    def set_value(self, value):
        self.value=value
        self.api.updateData(self)

    