from .command import Command


class FromGeofileSubCommand(Command):
    """
    Create a new location/mapset from a geofile

    from-geofile
        {geofile : The path to the geofile}
    """

    help = "The <info>from-geofile</> command, creates a new Location/Mapset from a geofile"

    def handle(self):
        self.line("The geofile you gave is: %s", self.argument("geofile"))

class FromEPSGSubCommand(Command):
    """
    Create a new location/mapset from an EPSG code.

    from-epsg
        {epsg : The EPSG code}
    """

    help = "The <info>from-geofile</> command, creates a new Location/Mapset from an EPSG code."

    def handle(self):
        msg = "The EPSG code you gave is: %s" % self.argument("epsg")
        self.line(msg)




class CreateCommand(Command):
    """
    Create a new Location/Mapset.

    create
        {--epsg : The EPSG code to use}
        {--geofile : The path to the geofile to use}
        {--xy : 
    """

    help = (
        "The <info>create</> command creates a new Location/Mapset. "
        "You need to specify exactly one of <info>--epsg</>, <info>--geofile</> "
        "and <info>--xy</>\n\n"
        "Examples"
    )


    # commands = [FromGeofileSubCommand(), FromEPSGSubCommand()]

    def handle(self):  # type: () -> int
        return self.call("help", self._config.name)
