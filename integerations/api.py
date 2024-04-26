import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def get_todo(id):
    path = "/todos"
    url = os.environ.get("URL")
    print(url)
    request_url = url + path + "/" + str(id)
    data = requests.get(request_url)
    return json.loads(data.content)    
