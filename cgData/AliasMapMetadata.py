import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.Metadata import Metadata

class AliasMapMetadata(Metadata):
    """This class describes the metadata relating to AliasMap objects.  In addition
    to the common metadata, AliasMap metadata specifies the genomic assembly.
    """

    def __validate(self):
        """Validate this object, and throw a ValidationFailed exception if
        unsuccessful.
        """
        pass

    def assembly(self, newAssembly=None):
        """Update the assembly if a new value is specified.
        Return the assembly, or None if not defined.
        """
        pass
