import argparse
from config import UserConfig

from input_utils import ask_for_input, InputException, validate_and_parse_tags

import logging


logger = logging.getLogger(__name__)


class Command:
    def __init__(self):
        raise Exception("This class should not be instantiated")

    def get_command_name(self):
        pass

    def setup_parser(self, parser):
        pass

    def run_command(self, namespace, user_config):
        pass


class ListCommands(Command):
    def __init__(self):
        self._command_name = "list-commands"

    def get_command_name(self):
        return self._command_name

    def setup_parser(self, parser):
        parser.add_argument('--tag', dest='tag', action='store', default=["all"],
                            help='Lists available user commands. Use --tag if you want to list available commands for '
                                 'by tag')
        parser.add_argument('--verbose', '-v', action=argparse.BooleanOptionalAction)
        parser.set_defaults(func=self.run_command)

    def run_command(self, namespace, user_config: UserConfig):
        # if is_verbose is set to true it will display every detail of the available user commands
        is_verbose = True if namespace.verbose else False
        user_config.list_commands(is_verbose)
        pass


class DeleteCommand(Command):
    def __init__(self):
        self._command_name = "delete-command"

    def get_command_name(self):
        return self._command_name

    def setup_parser(self, parser):
        parser.add_argument('--tags', dest='tags', action='store', default=["general"],
                            help='specify the tag associated with the command')
        parser.set_defaults(func=self.run_command)

    def run_command(self, namespace, user_config):
        # todo
        logger.debug(f'running {self._command_name}')
        pass


class InsertCommand(Command):
    def __init__(self):
        self._command_name = "insert-command"

    def get_command_name(self):
        return self._command_name

    def setup_parser(self, parser):
        parser.add_argument('--name', dest='name', action='store',
                            help='specify the name associated with the command')
        parser.add_argument('--command', dest='command', action='store',
                            help='specify the command inside quotes')
        parser.add_argument('--description', dest='description', action='store',
                            help='specify the name associated with the command')
        parser.add_argument('--tags', dest='tags', action='store',
                            help='specify the tag associated with the command')
        parser.set_defaults(func=self.run_command)

    def run_command(self, namespace, user_config):
        try:
            name = namespace.name or ask_for_input("Command name (ex: 'create test folder'): ", is_mandatory=True)
            command = namespace.command or ask_for_input("Command (ex: 'mkdir test'): ", is_mandatory=True)
            description = namespace.description or input("Command description (ex: 'creates a test folder in the "
                                                         "current path'): ") or ''
            tags_as_str = namespace.tags or input("Command tags separated by comma (ex: 'filesystem', 'linux'): ") or 'general'
            tags = validate_and_parse_tags(tags_as_str)
            user_config.add_command(name, command, description, tags)
        except InputException as e:
            logger.error(e)


class GetCommand(Command):
    def __init__(self):
        self._command_name = "get-command"

    def get_command_name(self):
        return self._command_name

    def setup_parser(self, parser):
        parser.add_argument('--tags', dest='tags', action='store', default=["general"],
                            help='specify the tag associated with the command')
        parser.set_defaults(func=self.run_command)

    def run_command(self, namespace, user_config):
        # todo
        logger.debug(f'running {self._command_name}')
        pass

