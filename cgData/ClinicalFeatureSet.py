import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.ClinicalFeatureSetMetadata import ClinicalFeatureSetMetadata
from ucscCancer.cgData.ClinicalFeatureVector import ClinicalFeatureVector
from ucscCancer.cgData.DataSet import DataSet

class ClinicalFeatureSet(DataSet):
    """A ClinicalFeature object contains a set of descriptions of the
    clinical data.  The data is represented as a list of
    ClinicalFeatureVector objects, each of which has a type which is
    one of (shortTitle, longTitle, valueType, state,
    stateOrder). Certain types of features are unique within each
    ClinicalFeatureSet while others are not.  The unique features are
    (name, shortTitle, longTitle, valueType, stateOrder).  The
    non-unique features are (state).
    
    See ClinicalFeatureVector.py
    """
    
    def __init__(self, clinicalFeatureMetadata):
        """Given a clinical feature metadata object, load the
        corresponding ClinicalFeature object.  Upon creation, the new
        object is validated, and if it fails validation, a ValidationFailed
        exception is thrown.  """
        super().__init__()
        pass

    def __validate(self):
        """Validate this ClinicalFeature, and throw a ValidationFailed exception
        if unsuccessful.
        """
        pass

    def features(self, name=None, type=None):
        """Return the list of features.  If name and/or type are not
        None, then return a list of all features pertaining to the
        indicated name and/or type.  Otherwise, return a list of all
        features in this feature map."""
        pass

    def metadata(self):
        """Return the metadata associated with this clinical feature set"""
        pass
    
    def nFeatures(self, name=None):
        """Return the number of clinical features in this object.
        If name is specified, return only the number of features relating
        to the named feature.  Otherwise, return the total number of features
        in this set.
        """
        pass

    def sort(self, cmp=ClinicalFeatureVector.compare):
        """Sorts the set of clinical features by the indicated sort function
        """
        pass
    
        
    def write(self, filename):
        """Write the ClinicalFeature object to the indicated filename"""
        pass


