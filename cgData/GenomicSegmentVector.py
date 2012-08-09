import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.DataVector import DataVector

class GenomicSegmentVector(DataVector):
    """GenomicSegmentVector objects indicate which segments were
    present in the indicated samples, and with what score For example,
    copy number data can be represented as GenomicSegmentVectors.

    Each GenomicSegmentVector contains the following fields:
    - sampleId: the name of the sample in which the segment was observed
    - chrom: name of the chromosome
    - start: starting position within the chromosome or scaffold
    - end: ending position within the chromosome or scaffold.
    - strand: either '+' for forward, '-' for reverse, or '.' for both
    - score: floating point score for the segment

    Comment: in the API document, the term "GenomicSegment" seems to
    refer to a file of genomic segment observations.  But I feel like
    there are two different classes: GenomicSegmentVector objects, in
    which each object represents the observation of one segment in one
    indicated sample; and GenomicSegmentSet objects, representing a
    set of GenomicSegmentVectors that are contained together in a
    file.

    See Also: GenomicSegmentSet
    """

#    __format__ = {
#            "name" : "genomicSegment",
#            "type" : "type",
#            "form" : "table",
#            "columnOrder" : [
#                "id",
#                "chrom",
#                "chrom_start",
#                "chrom_end",
#                "strand",
#                "value"
#            ],
#            "groupKey" : "id",
#            "columnDef" : {
#                "chrom_start" : { "type" : "int" },
#                "chrom_end" :   { "type" : "int" },
#                "value" : { "type" : "float" }
#            }
#        }

    def __init__(self, line=None):
        """Creates a new GenomicSegmentVector object.  If line is
        None, an empty object is returned.  Else, the contents of the
        GenomicSegmentVector are parsed from the line, which should
        contain the indicated fields and be whitespace-delimited.
        As a final initialization step, the object is validated.  If
        validation fails, a ValidationFailed exception is thrown.
        """
        pass

    def __validate(self):
        """Validate this GenomicSegmentVector, and throw a ValidationFailed
        object if unsuccessful.  """
        pass

    def genomicSegmentVectorCompare(vector1, vector2):
        """Return the results of comparing vector1 to vector2, comparing each field
        (id, chrom, chromStart, chromEnd, strand, value) in the order indicated.
        Use numeric comparison on chromStart, chromEnd, and value, and lexical
        comparison on all other fields."""
        pass
    
    def write(self, filehandle, delimiter="\t"):
        """Write a GenomicSegmentVector object to the indicated
        filehandle.  The data is written in tab-delimited format by
        default.
        """
        pass



