
class Data(object):
    """Within the cgData realm, there is data and there is metadata.  This is the base
    class for all data objects.

    See also Metadata.pm
    """

    def __init__(self, filename):
        """Create a new data object"""
        self._filename = filename
        self._validate()

    def __validate(self):
        """Cursory validation"""
        if not os.path.exists(self._filename):
            raise IOERROR("Cannot find data file %s" % (self._filename))

    def metadata(self):
        """Return the metadata object associated with this data"""
        pass
