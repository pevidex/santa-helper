import json


class UserCommand:
    def __init__(self, name, description, command_str, tags):
        self.name = name
        self.description = description
        self.command = command_str
        self.tags = tags

    def __iter__(self):
        yield from {
            "name": self.name,
            "description": self.description,
            "command": self.command,
            "tags": self.tags
        }.items()

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return self.__str__()

    def print_command(self, is_verbose: bool = False):
        # todo print in a fancier way
        print(self.__str__())
        pass

    @staticmethod
    def from_json(json_dct):
        return UserCommand(json_dct['name'], json_dct['description'], json_dct['command'], json_dct['tags'])


class UserConfig:
    def __init__(self, commands):
        self._commands = commands

    def __iter__(self):
        yield from {
            "commands": self._commands
        }.items()

    def __str__(self):
        return json.dumps(self.to_json())

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        commands = []
        for command in self._commands:
            commands.append(command.__dict__)

        return {'commands': commands}

    @staticmethod
    def from_json(json_dct):
        return UserConfig([UserCommand.from_json(cmd) for cmd in json_dct['commands']])

    def add_command(self, name, description, command_str, tags):
        self._commands.append(UserCommand(name, description, command_str, tags))

    def list_commands(self, is_verbose: bool = False):
        if len(self._commands) == 0:
            print("No available commands commands. Add a new one by running 'python main.py insert-command'") # todo
            return
        print("List of available commands:")
        [cmd.print_command(is_verbose) for cmd in self._commands]
