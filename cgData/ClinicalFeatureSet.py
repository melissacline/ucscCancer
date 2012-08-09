import ucscCancer.cgData.Exceptions


class ClinicalFeatureSet(object):
    
    """A ClinicalFeature object contains a set of descriptions of the
    clinical data.  The data is represented as a list of
    ClinicalFeatureVector objects, each of which has a type which is
    one of (shortTitle, longTitle, valueType, state,
    stateOrder). Certain types of features are unique within each
    ClinicalFeatureSet while others are not.  The unique features are
    (name, shortTitle, longTitle, valueType, stateOrder).  The
    non-unique features are (state)OA.

    See ClinicalFeatureVector.py
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


    def __init__(self, clinicalFeatureMetadata):
        """Given a clinical feature metadata object, load the
        corresponding ClinicalFeature object.  Upon creation, the new
        object is validated, and if it fails validation, a ValidationFailed
        exception is thrown.  """
        pass

    def __validate(self):
        """Validate this ClinicalFeature, and throw a ValidationFailed exception
        if unsuccessful.
        """
        pass

    def featuresByName(self, name):
        """Return the list of features pertaining to the named feature"""
        pass

    def featuresByType(self, type):
        """Return the list of features of the indicated type"""
        pass

    def nClinicalFeatures(self, name=None):
        """Return the number of clinical features in this object.
        If name is specified, return only the number of features relating
        to the named feature.  Otherwise, return the total number of features
        in this set.
        """
        pass

    def sort(self):
        """Sorts the set of clinical features by name, then shortTitle, and
        then in order by longTitle, valueType, state, and stateOrder.
        """
        pass
    
        
    def write(self, filename):
        """Write the ClinicalFeature object to the indicated filename"""
        pass


