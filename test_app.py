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


def get_todos_list():
    todo1 = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    todo2 = {
        "userId": 2,
        "id": 2,
        "title": "lorem ipsum",
        "completed": True
    }
    return[todo1, todo2]

def test_get_todos(mocker):
    def mock_get_todo(todo_id):
        if(todo_id == 1): 
            return get_todos_list()[0]
        return get_todos_list()[1]

    mock_get_todo = mocker.patch('app.get_todo', side_effect = mock_get_todo)
    # mock_get_todo.return_value = todo

    res = get_todos()

    assert res == [get_todos_list()[1]]
