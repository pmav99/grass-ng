from cleo import Application as BaseApplication

from .commands import BatchCommand
from .commands import CreateCommand
from .commands import ExecCommand
from .commands import GUICommand
from .commands import TUICommand

from .. import __version__


class Application(BaseApplication):
    """ Grass next generation """

    def __init__(self):
        super(Application, self).__init__("grass_ng", __version__)

        for command in self.get_default_commands():
            self.add(command)

    def get_default_commands(self) -> list:
        commands = [
            BatchCommand(),
            CreateCommand(),
            ExecCommand(),
            GUICommand(),
            TUICommand(),
        ]
        return commands
