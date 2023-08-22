import os
from dotenv import load_dotenv

load_dotenv()


def change_scope():
    """
    Changes the current list in scope
    :return:
    """
    #TODO: write and add this functionality to change scopes
    pass


def add_new_list_to_env(key: str, value: str):
    env_file_path = './.env'
    if os.path.isfile(env_file_path):
        with open(env_file_path, "a") as f:
            f.write(f"{key.upper()}={value}\n")
    else:
        with open(env_file_path, "w") as f:
            f.write(f'SCOPE={key.upper()}\n')
            f.write(f"{key.upper()}={value}\n")
