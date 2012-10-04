import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.DataVector import DataVector

class SampleMapVector(DataVector):
    """The SampleMap connects the samples in GenomicMatrix objects to the
    clinical data in ClinicalMatrix objects, and relates sample IDs in
    a parent-child model.  This model expresses that one patient can
    have a tumor sample and a normal sample, the tumor and normal
    biopsies can both yield multiple laboratory samples, and so forth.
    
    This data is described in a two-column file.  In the simplest case
    (with no relationships), each sample ID appears on one line in both
    columns: (sampleId sampleId)
    
    In the more general case (with parent-child relationships), there is
    also some line with the parent in the left column and the child in the
    right.  For example, in the case of one parent and one child, the file
    would look like this:
    1. parent parent
    2. parent child
    3. child child

    The overall sample map is described in a SampleMapSet object, which contains
    a set of SampleMapVector objects.  Each SampleMapVector object describes
    one relation between a two samples, or between a sample and itself.

    See Also: SampleMapSet
    """
    
#    __format__ =  {
#        "name" : "sampleMap",
#        "form" : "table",
#        "columnOrder" : [
#            "sample",
#            "aliases",
#            "chrom",
#            "chrom_start",
#            "chrom_end",
#            "strand"
#            ],
#        "primaryKey" : "sample",
#        "columnDef" : {
#            "chrom_start" : { "type" : "int", "index" : 1 },
#            "chrom_end" : { "type" : "int", "index" : 1 }
#            }
#        }

    def __init__(self, line=None):
        """Creates a new SampleMapVector object.  If line is None, an 
        empty object is returned.  Else, the contents of the SampleMapVector
        are parsed from the line, which should contain the indicated fields
        and be whitespace-delimited.  The object is validated as a
        final initialization step.  If validation fails, a ValidationFailed
        exception is thrown.
        """
        super().__init__()
        pass


    def __validate(self):
        """Validate the object.  If unsuccessful, throw a ValidationFailed
        exception.
        """

    def compare(vector1, vector2):
        """Compare the two sample map vectors, sorting by the leftmost
        column first and using additional columns to break ties.
        """
        pass

    def write(self, filehandle, delimiter="\t"):
        """Write a SampleMapVector object to the indicated filehandle.
        The data is written in tab-delimited format by default.
        """
        pass


