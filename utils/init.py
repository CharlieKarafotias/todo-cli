"""
Functions needed to initialize the YAML file when the CLI is first ran
"""

import os
from datetime import datetime

# TODO: fix error when trying to run python3 ./main.py
try:
    import errors
    import jsonHandler
    import schema.default
except:
    from .errors import *
    from .jsonHandler import *
    from .environment import *
    from schema.default import *

# from utils.errors import print_err
# from utils.jsonHandler import create_new_json_file, py_dict_to_json_str
# from schema.default import new_todo_list
# from utils.environment import add_new_list_to_env



def new_json_file(destination, name=f'todo_list_{datetime.now().strftime("%Y_%m_%d")}'):
    """
    Creates a new json file for storing the list
    :param destination: the directory where the file should be saved
    :param name: the name of the file (the list name); defaults to todo_list_%Y_%m_%d
    :return: no return, a new file will be created
    """
    if os.path.isdir(destination):
        name = format_file_name(name)
        # create new json file
        create_new_json_file(
            f'{destination}{name}',
            py_dict_to_json_str(new_todo_list(name))
        )

        #  update env to remember where list is stored
        add_new_list_to_env(name, destination)
    else:
        errors.print_err(f'ERR: no such directory - {destination}')


def format_file_name(name):
    # format name
    return name.strip().replace(' ', '_')

