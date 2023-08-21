from datetime import datetime


def new_todo_list(name: str) -> dict:
    resp = {
        'name': name,
        'created_on': f'{datetime.now():%Y-%m-%d %H:%M:%S%z}',
        'todos': []
    }

    return resp
