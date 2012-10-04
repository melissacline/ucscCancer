import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.ProbeMapVector import ProbeMapVector
from ucscCancer.cgData.DataSet import DataSet

class ProbeMapSet(DataSet):
    """This class represents a collection of ProbeMap objects, such
    as a file with ProbeMap observations.  

    Here, I'm assuming that what the documentation refers to as "ProbeMap"
    actually refers to a ProbeMapSet, a set of individual ProbeMap vectors.

    Note that while the API documentation uses the term ProbeMap
    to refer to the individual segments and a collection of segments, this
    class contains a collection of segments.  The individual segments are
    represented by the ProbeMap class

    See Also: ProbeMapVector.
    """


    def __init__(self, probeMapSetMetadata):
        """Given a probeMap set metadata object, load the
        corresponding ProbeMapSet object.  Upon creation, the new
        object is validated, and if it fails validation, a
        ValidationFailed exception is thrown.
        """
        super().__init__()
        pass
    
    def __validate(self):
        """Validate this ProbeMapSet. If unsuccessful, throw a ValidationFailed
        exception.
        """
        pass

    def nProbes(self):
        """Return the number of probes in this ProbeMapSet"""
        pass

    def probes(self):
        """Return the list of probes represented in this ProbeMapSet"""
        pass

    def sort(self, cmp=ProbeMapVector.compare):
        """Sort the probe map vectors according to the indicated comparison function"""
        pass
    
    def write(self, filename):
        """Write the ProbeMapSet object to the indicated filename"""
        pass

