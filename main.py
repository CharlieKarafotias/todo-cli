import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='Todo CLI',
        description='A CLI for handling daily todo tasks and storing them in a YAML format',
        epilog='Developed in 2023 by Charlie Karafotias'
    )
    subparsers = parser.add_subparsers(
        title='Possible commands',
        dest='command')

    # Init parser instantiation
    parser_init = subparsers.add_parser('init', help='Initialize TODO CLI')

    # add new event parser instantiation
    parser_add = subparsers.add_parser('add', help='Add a new todo')

    args = parser.parse_args()
    print(args)

    match args.command:
        case 'init':
            pass
        case 'add':
            pass


if __name__ == '__main__':
    main()
