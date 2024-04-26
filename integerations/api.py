import os
from dotenv import load_dotenv
import requests

load_dotenv()

def get_todo(id):
    path = "/todos"
    url = os.environ.get("URL")
    request_url = url + path + "/" + str(id)
    data = requests.get(request_url)
    return data.json()    
