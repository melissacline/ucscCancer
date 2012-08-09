
class Data(object):
    """Within the cgData realm, there is data and there is metadata.  This is the base
    class for all data objects.

    See also Metadata.pm
    """

    def __init__(self):
        """Create a new data object"""
        pass

    def metadata(self):
        """Return the metadata object associated with this data"""
        pass
