import os
from dotenv import load_dotenv
from integrations.api import get_todo
import requests_mock

load_dotenv()

@requests_mock.Mocker(kw="mock")
def test_get_todo_returns_todo(**kwargs):
    json = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    url = f"{os.getenv('URL')}/todos/2"

    kwargs["mock"].get(url, json= json)
    resp = get_todo(2)
    assert resp == json
