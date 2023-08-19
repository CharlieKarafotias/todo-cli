"""
Functions needed to initialize the YAML file when the CLI is first ran
"""

import os
import errors
import jsonHandler
from datetime import datetime


def new_json_file(destination, name=f'todo_list_{datetime.now().strftime("%Y_%m_%d")}'):
    """
    Creates a new json file for storing the list
    :param destination: the directory where the file should be saved
    :param name: the name of the file (the list name); defaults to todo_list_%Y_%m_%d
    :return: no return, a new file will be created
    """
    if os.path.isdir(destination):
        name = format_file_name(name)
        # TODO: change this to a new format from a separate file once I figure out the format
        jsonHandler.create_new_json_file(f'{destination}{name}', jsonHandler.py_dict_to_json_str({}))
        # create new json file at destination with name
    else:
        errors.print_err(f'ERR: no such directory - {destination}')


def format_file_name(name):
    # format name
    return name.strip().replace(' ', '_')

