from dotenv import load_dotenv
import os
from integerations.api import get_todo
load_dotenv()

def get_todos():
    even_todo_limit = int(os.environ.get("TODO_LIMIT"))
    todos = [get_todo(i) for i in range(2, 2 * even_todo_limit + 1, 2)]
    return todos

def display_todos(todos):
    for todo in todos:
        print(todo['title'], " ", todo['title'], " ", todo['completed'])

display_todos(get_todos())