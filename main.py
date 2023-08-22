import argparse
from handler import init_handler

# TODO LIST:
# TODO: can parser be initialized as modules? Can it be moved to a python package where every part is separate?
# TODO: flag arg for subtask list?
# TODO: add function to main.py for changing lists (changes scope)
# TODO: add export function with different software for export (should paste to clipboard automatically and notify)

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
    # Properties to include: title, description, due date, priority, tags
    parser_add = subparsers.add_parser('add', help='Add a new todo')
    parser_add.add_argument(
        'title',
        help='The title of the todo event to add to the list.'
    )
    parser_add.add_argument(
        '-d',
        '--description',
        help='The description of the new todo event',
        required=False
    )
    parser_add.add_argument(
        '-p',
        '--priority',
        help='The priority of the new todo event. The default value will be low priority',
        default='low',
        required=False
    )
    parser_add.add_argument(
        '-t',
        '--tags',
        nargs='+',
        help='One or more tags for the new todo event',
        required=False
    )


    args = parser.parse_args()
    print(args)

    match args.command:
        case 'init':
            init_handler.new_json_file(args.destination, args.name)
        case 'add':
            pass


if __name__ == '__main__':
    main()
