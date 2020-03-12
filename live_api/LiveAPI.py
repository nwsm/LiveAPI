import os
import requests
import json

class LiveAPI:
    def createAPI(self):
        os.system('python server.py')

    def deleteData(self, name):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        requests.delete('http://localhost:3000/'+name, headers=headers)

    def addData(self, name, data):
        headers = {'Content-Type': 'application/json', 'Accept':'application/json'}
        requests.post('http://localhost:3000/'+name, data=json.dumps({"data": data}), headers=headers)

    def getData(self, resource):
        return requests.get('http://localhost:3000/'+resource)

def is_iterable(data):
    try:
        iterator = iter(data)
    except TypeError:
        return False
    else:
        return True

class Resource:
    def __init__(self, api, name, data=None):
        self.name=name
        self.api=api
        if data != None:
            if not is_iterable(data):
                data = [data]
            self.data=data
            self.api.addData(self.name)
        else:
            self.data=[]

    def set_data(self, data):
        if not is_iterable(data):
            data = [data]
        self.data=data
        self.api.deleteData(self.name)
        self.api.addData(self.name, data)

    def add_data(self, data):
        if not is_iterable(data):
            data = [data]
        if self.data == None:
            self.data=data
        else:
            self.data=self.data+data
            self.api.addData(self.name, data)
