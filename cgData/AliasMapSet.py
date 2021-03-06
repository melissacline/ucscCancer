import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.AliasMapVector import AliasMapVector
from ucscCancer.cgData.DataSet import DataSet

class AliasMapSet(DataSet):
    """An AliasMap object contains a number of vectors that link probes
    to other sets of identifiers.  For example, an alias map might map
    probes to gene names

    Assumptions:
    
    Any probe can have more than one alias in any alias map.

    See also: AliasMapVector.py
    """


    def __init__(self, aliasMapMetadata):
        """Given an alias map metadata object, load the corresponding AliasMap
        object.  Upon creation, the new object is validated, and if it fails validation,
        a ValidationFailed exception is thrown.
        """
        super().__init__()
        pass

    def __validate(self):
        """Validate this AliasMapSet, and throw a ValidationFailed exception if
        unsuccessful.
        """
        pass

    def aliases(self, probe=None):
        """Return the aliases included in this AliasMap.  If probe
        is not None, then return a list of the aliases for the
        specified probe, returning None if the probe is not in the
        alias map.  Otherwise, return a list of the aliases of all
        probes in this alias map."""
        pass

    def compareEntries(mapEntry1, mapEntry2):
        """Return the results of a lexical comparison between two alias map entries"""
        pass
    
    def probes(self):
        """Return the list of probes included in this AliasMap"""
        pass

    def sort(self, cmp=AliasMapVector.compare):
        """Sort the alias map according to the indicated comparison function"""
        pass
    
    def write(self, filename):
        """Write the AliasMap to the indicated filename."""
        pass
