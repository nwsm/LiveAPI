import sys
from live_api import LiveAPI
print(sys.path)
api = LiveAPI.LiveAPI()

api.createAPI(3)