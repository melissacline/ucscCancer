
import ucscCancer.cgData.Exceptions 
from ucscCancer.cgData.DataVector import DataVector

class SampleMap(DataVector):
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
    """

    def __init__(self, sampleMapMetadata):
        """Given a sample map metadata object, load the
        corresponding SampleMap object and return it.  Upon creation, the new
        object is validated, and if it fails validation, a ValidationFailed
        exception is thrown"""
        super().__init__()
        pass

    def __validate(self):
        """Validate the object.  If validation fails, throw a ValidationFailed
        exception.
        """
        
    def samples(self):
        """Return a list of the samples contained in this SampleMap."""
        pass

    def parent(self, sampleId):
        """Given a sample ID, return its parent.  If the sample ID has no parent,
        return None.
        """
        pass

    def children(self, sampleId):
        """Given a sample ID, return its children.  If the sample has no children,
        return None.
        """
        pass

    def compare(sampleMap1, sampleMap2):
        """Return the results of a lexical comparison between the
        first column in the two sample maps.  If they contain the same
        value, return the results of a lexical comparison between the
        second two columns"""
        
    def sort(self, cmp=compare):
        """Sort the sample map according to the specified comparison function."""

    def write(self, filename):
        """Write the SampleMap object to the indicated filename"""
        pass



    
        



