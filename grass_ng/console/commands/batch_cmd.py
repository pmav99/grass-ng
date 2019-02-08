from .command import Command


class BatchCommand(Command):
    """
    Start GRASS GIS in batch mode.

    batch
    """

    help = "The <info>batch</> command starts GRASS GIS in batch mode."

    def handle(self):
        self.line("<error>Inside the batch mode!</error>")
        self.line("")
