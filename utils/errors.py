from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()


def print_err(message):
    print(f'{Fore.RED}{message}{Style.RESET_ALL}')


def print_warn(message):
    print(f'{Fore.YELLOW}{message}{Style.RESET_ALL}')
