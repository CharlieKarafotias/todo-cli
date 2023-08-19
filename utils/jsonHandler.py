import json
import os
import errors


def empty_json():
    data = {}
    resp = json.dumps(data)
    return resp


def py_dict_to_json_str(data: dict):
    return json.dumps(data)


def write_json_to_file(destination: str, json_str: str):
    if os.path.isfile(destination):
        with open(destination, "w") as f:
            # Writing data to file
            f.write(json_str)
    else:
        errors.print_err(f'ERR: no such file - {destination}')


def create_new_json_file(destination: str, json_str: str):
    if not ('.' in destination and destination.split('.')[-1] == 'json'):
        destination += '.json'

    with open(destination, "w") as f:
        # Writing data to file
        f.write(json_str)


