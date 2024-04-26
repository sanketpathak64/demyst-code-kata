import os
from dotenv import load_dotenv
import pytest
from app import get_todos
from integrations.api import get_todo


load_dotenv()

@pytest.fixture(autouse=True)
def override_env_variables():
    os.environ['TODO_LIMIT'] = '1'
    yield
    del os.environ['TODO_LIMIT']


def test_get_todos(mocker):
    todo = {
        "userId": 1,
        "id": 2,
        "title": "delectus aut autem",
        "completed": False
    }
    mock_get_todo = mocker.patch('app.get_todo')
    mock_get_todo.return_value = todo

    res = get_todos()

    assert res == [todo]
