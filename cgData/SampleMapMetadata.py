
import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.Metadata import Metadata

class SampleMapMetadata(Metadata):
    """This class describes the metadata relating to SampleMap objects. 
    """

    def __validate(self):
        """Validate this object.  Throw a ValidationFailed error if unsuccessful"""
        pass

    def clinicalMatrixMetadata(self):
        """Return a list of the one or more clinicalMatrixMetadata files
        associated with this SampleMap.  Note that there must be at least one.
        """
        pass

