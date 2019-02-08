from .command import Command


class ExecCommand(Command):
    """
    This is the exec command.

    exec
    """

    help = "The <info>exec</> command does exec whatever that is."

    def handle(self):
        self.line("<warning>This is exec!</warning>")
        self.line("")
