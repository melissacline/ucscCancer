import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.GenomicSegmentMetadata import GenomicSegmentMetadata
from ucscCancer.cgData.GenomicSegmentVector import GenomicSegmentVector

class GenomicSegmentSet(object):
    """This class represents a collection of GenomicSegment objects, such
    as a file with GenomicSegment observations.  

    Note that while the API documentation uses the term GenomicSegment
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the GenomicSegment class.  

    Question: Would a sort method be useful?
    
    See also: GenomicSegmentVector
    """


    def __init__(self, genomicSegmentMetadata):
        """Given a genomic segment set metadata object, load the
        corresponding GenomicSegmentSet object.  The new object is
        validated.  If validation fails, a ValidationFailed exception
        is thrown.
        """
        pass

    def __validate(self):
        """Validate this GenomicSegmentSet. If unsuccessful, throw
        a ValidationFailed exception.
        """
        pass

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""
        pass

    def sampleList(self):
        """Return the list of samples represented in this GenonicSegmentSet"""
        pass

    def sort(self, cmp=GenomicSegmentVector.genomicSegmentVectorCompare):
        """Sort the genomic segments according to the indicated compare function"""
        pass
        
    def write(self, filename):
        """Write the GenomicSegmentSet object to the indicated filename"""
        pass



