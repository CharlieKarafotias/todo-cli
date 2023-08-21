from datetime import datetime


def new_todo_list(name: str) -> dict:
    resp = {
        'name': name,
        'created_on': datetime.now(),
        'todos': []
    }

    return resp
