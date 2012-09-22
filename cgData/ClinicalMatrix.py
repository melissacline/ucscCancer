import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.DataMatrix import DataMatrix


class ClinicalMatrix(DataMatrix):
    """A ClinicalMatrix object contains the clinical data associated with
    a given set of samples.  In this matrix, the rows are samples and
    the columns are clinical features.  Missing values are denoted as blanks.
    """

#    __format__ = {
#        "name" : "clinicalMatrix",
#        "type" : "type",
#        "form" : "matrix",
#        "rowType" : "idMap",
#        "colType" : "clinicalFeature",
#        "valueType" : "str",
#        "nullString" : ""
#    }


    def __init__(self, clinicalMatrixMetadata):
        """Given a clinical matrix metadata object, load the
        corresponding ClinicalMatrix object.  Upon creation, the new
        object is validated, and if it fails validation, a ValidationFailed
        exception is thrown.   """
        super().__init__()
        pass

    def __validate(self):
        """Validate this ClinicalMatrix, and throw a 
        ValidationFailed exception if unsuccessful.  """
        pass


    def compareSampleIds(id1, id2):
        """Return the results of a lexical comparison between the two IDs"""
        pass
    
    def features(self):
        """Return the list of clinical features contained in this matrix"""
        pass

    def getValue(self, sampleId, clinicalFeature):
        """Get the data value for the indicated sample and clinical feature"""
        pass

    def nFeatures(self):
        """Return the number of clinical features in this matrix"""
        pass

    def nSamples(self):
        """Return the number of samples in this matrix"""
        pass

    def samples(self):
        """Return the list of samples represented in this matrix"""
        pass

    def setValue(self, sample, cliincalFeature, newValue):
        """Update the value stored for the indicated probe and sample
        """
        pass

    def sortClinicalMatrix(self, cmp=compareSampleIds):
        """Sort the clinical matrix according to the indicated comparison function"""
        pass
        
    def write(self, filename):
        """Write the CinicalMatrix object to the indicated filename"""
        pass


