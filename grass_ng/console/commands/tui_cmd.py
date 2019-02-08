from .command import Command


class TUICommand(Command):
    """
    Start a Text User Interface (TUI) session.

    tui
    """

    help = "The <info>tui</> command starts a Text User Interface (TUI) session."

    def handle(self):
        self.line("<error>Inside the TUI session!</error>")
        self.line("")
