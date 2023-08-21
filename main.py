import argparse
from utils import init


def main():
    parser = argparse.ArgumentParser(
        prog='Todo CLI',
        description='A CLI for handling daily todo tasks and storing them in a JSON format',
        epilog='Developed in 2023 by Charlie Karafotias'
    )
    subparsers = parser.add_subparsers(
        title='Possible commands',
        dest='command')

    # Init parser instantiation
    parser_init = subparsers.add_parser('init', help='Initialize TODO CLI')
    parser_init.add_argument(
        'destination',
        type=str,
        help='The location where the todo list should be saved'
    )
    parser_init.add_argument(
        '-n',
        '--name',
        help='The name of the todo list. Will default to todo_list_YYYY_mm_dd if not specified'
    )

    # add new event parser instantiation
    parser_add = subparsers.add_parser('add', help='Add a new todo')

    # TODO: add function to main.py for changing lists (changes scope)

    args = parser.parse_args()
    print(args)

    # TODO run test again and fix errors with name of json file and .env not adding new lines properly
    # python3 ./main.py init . -n test_list
    match args.command:
        case 'init':
            init.new_json_file(args.destination, args.name)
        case 'add':
            pass


if __name__ == '__main__':
    main()
