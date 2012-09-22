import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.DataVector import DataVector

class ClinicalFeatureVector(DataVector):
    """A ClinicalFeature object contains a vector describing a clinical feature.
    It has three pieces: name, type, and value.  Name is the name of the 
    clinical feature, type is one of (shortTitle, longTitle, valueType,
    state, stateOrder), and value is the feature value.  The value is of arbitrary
    format.

    See ClinicalFeatureSet.py
    """

#    __format__ = {
#        "name" : "clinicalFeature",
#        "type" : "type",
#        "form" : "feature",
#        "rowType" : "idMap",
#        "colType" : "clinicalFeature",
#        "valueType" : "str",
#        "nullString" : ""
#    }


    def __init__(self, line=None):
        """Creates a new ClincialFeatureVector object.  If line is
        None, an empty object s returned.  Else, the contents of the
        ClinicalFeatureVector are parsed from the line, which should
        be whitespace-delimited.  Upon creation, the new object is
        validated, and if it fails validation, a ValidationFailed
        exception is thrown.  """
        super().__init__()
        pass

    def __validate(self):
        """Validate this ClinicalFeatureVector, and throw a ValidationFailed exception
        if unsuccessful.
        """
        pass

    def compare(vector1, vector2):
        """Compare the two clinical feature vectors, sorting by name,
        then shortTitle, and then in order by longTitle, valueType,
        state, and stateOrder.  """
        pass

    def write(self, filenhandle):
        """Write the ClinicalFeatureVector object to the indicated filehandle,
        which should be open for writing"""
        pass


