
import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.Metadata import Metadata

class ClinicalMatrixMetadata(Metadata):
    """This class describes the metadata specific to ClinicalMatrix objects.
    In addition to the metadata common to genomic objects, the clinical matrix
    metadata may contain references to the CinicalFeature metadata.
    """

    def __init__(self, filename):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  Upon creation, run the validator
        method on the new object and throw a ValidationFailed exception if
        unsuccessful.
        """
        super().__init__(filename)
        pass

    def __validate(self):
        """Validate this GenomicMatrixMetadata object, and throw a
        ValidationFailed exception if unsuccessful.
        """
        pass
        
    def clinicalFetureMetadata(self):
        """Return the clinicalFeature metadata object, or None if none is loaded.
        """
        pass

