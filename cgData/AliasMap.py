import cgDataV2.Exceptions

class AliasMap(object):
    """An AliasMap object links probes to other sets of identifiers.  For
    example, an alias map might map probes to gene names

    Question: can a probe have more than one alias in a single AliasMap?
    """

#    __format__ =  {
#            "name" : "aliasMap",
#            "type" : "type",
#            "form" : "table",
#            "columnOrder" : [
#            "probe",
#            "alias"
#            ],
#            "groupKey" : "probe"
#            }

    def __init__(self, aliasMapMetadata):
        """Given an alias map metadata object, load the corresponding AliasMap
        object.  Upon creation, the new object is validated, and if it fails validation,
        a ValidationFailed exception is thrown.
        """

    def __validate(self):
        """Validate this AliasMap, and throw a ValidationFailed exception if
        unsuccessful.
        """
        pass

    def aliasList(self):
        """Return the list of aliases included in this AliasMap"""
        pass

    def aliasThisProbe(self, probe):
        """Return the alias for the indicated probe, or None if it is not in this
        AliasMap.
        """
        pass

    def compareAliasMapEntries(mapEntry1, mapEntry2):
        """Return the results of a lexical comparison between two alias map entries"""
        pass
    
    def probeList(self):
        """Return the list of probes included in this AliasMap"""
        pass

    def sortAliasMap(self, cmp=compareAliasMapEntries):
        """Sort the alias map according to the indicated sort function"""
        pass
    
    def write(self, filename):
        """Write the AliasMap to the indicated filename."""
        pass
