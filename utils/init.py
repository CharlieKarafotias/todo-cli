"""
Functions needed to initialize the YAML file when the CLI is first ran
"""

import os
import errors
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
        # create new json file at destination with name
    else:
        errors.print_err(f'ERR: no such directory - {destination}')


def format_file_name(name):
    # format name
    return name.strip().replace(' ', '_')


new_json_file('../')
