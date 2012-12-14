import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.GenomicMetadata import *

class GenomicSegmentMetadata(GenomicMetadata):
    """This class describes the metadata specific to GenomicSegment objects.
    In addition to the metadata common to genomic objects, the genomic segment
    metadata describes the assembly
    """

    def __init__(self, filename,):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  
        """
        super(GenomicSegmentMetadata, self).__init__(filename)
        self._validate()
        directory = "/".join(filename.split("/")[0:-1])
        if directory == "":
            delimiter = ""
        else:
            delimiter = "/"
        self._initSampleMapReference("rowKeySrc", directory, delimiter)


    def _validate(self):
        """Validate, and throw a ValidationFailed exception if unsuccessful"""
        #
        # Verify that the data is of type genomicSegment.
        super(GenomicSegmentMetadata, self)._validate()
        assert(self._contents.has_key('type'))
        if self._contents['type'] != "genomicSegment":
            errorMsg = (("GenomicSegment metadata file %s has unexpected type"
                         + " of %s, not genomicSegment")
                        % (self._filename, self._contents['type']))
            raise ValidationFailed(errorMsg)
        else:
            self._validateSampleMapReference("rowKeySrc")


    
    def assembly(self, newAssembly=None):
        """Update the assembly if a new value is specified.
        Return the assembly, or None if not defined.
        """
        pass

