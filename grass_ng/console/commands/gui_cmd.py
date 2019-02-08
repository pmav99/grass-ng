from .command import Command


class GUICommand(Command):
    """
    Start a Graphical User Interface (GUI) session.

    gui
    """

    help = "The <info>gui</> command starts the GUI session."

    def handle(self):
        self.line("<error>Inside the GUI session!</error>")
        self.line("")
