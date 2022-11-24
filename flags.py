import argparse

from commands import GetCommand, ListCommands, DeleteCommand, InsertCommand
from fs_utils import deserialize_config_file, serialize_config_file

import logging

available_commands = [InsertCommand(), GetCommand(), ListCommands(), DeleteCommand()]


def _get_version():
    # todo
    return '0'


def parse_args():
    return parser.parse_args()


# init parser
parser = argparse.ArgumentParser(description='Manages and stores your most used shell commands')

# version subcommand command
parser.add_argument('--version', action='version', version=_get_version())

# debugger flag
# todo currently does not work if --debug flag is placed after subcommand i.e. 'python main.py list-commands --debug'
parser.add_argument('--debug', action=argparse.BooleanOptionalAction)

subparsers = parser.add_subparsers(dest='cmd')

# add subcommands
[cmd.setup_parser(subparsers.add_parser(cmd.get_command_name())) for cmd in available_commands]

args = parser.parse_args()

# todo refactor some logic to main.py

logger = logging.getLogger(__name__)
if args.debug:
    logger.setLevel(logging.DEBUG)

if args.cmd is None:
    parser.print_help()
else:
    user_config = deserialize_config_file()
    args.func(args, user_config)
    serialize_config_file(user_config)
