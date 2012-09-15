
import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.GenomicMatrixMetadata import GenomicMatrixMetadata
from ucscCancer.cgData.DataMatrix import DataMatrix
import sys

class GenomicMatrix(DataMatrix):
    """GenomicMatrix objects contain sets of experimental observations.
    They operate on files that are structured as matrices, with the
    rows representing probes and the columns representing samples.
    Each cell, representing the intersection of one probe and one
    sample, represents one single experimental observation
    """
#    __format__ = {
#        "name" : "genomicMatrix",
#        "type" : "type",
#        "form" : "matrix",
#        "rowType" : "probeMap",
#        "colType" : "sampleMap",
#        "valueType" : "float",
#        "nullString" : "NA",
#        "links" : {
#            "dataSubType" : {}
#            }
#        }

    def __init__(self, genomicMatrixMetadata):
        """Given a genomic matrix metadata object, load and return the
        corresponding GenomicMatrix object.  Upon creation, the new
        object is validated, and if it fails validation, a
        ValidationFailed exception is thrown """
        super(DataMatrix, self).__init__()
        pass

    def __validate(self):
        """Validate this GenomicMatrix. If unsuccessful, throw a ValidationFailed
        exception.
        """
        pass

    def compareProbeIds(id1, id2):
        """Return the results of a lexical comparison between the two probe IDs"""
        pass
    
    def getValue(self, probe, sample):
        """Get the data value for the indicated probe and sample"""
        pass

    def nProbes(self):
        """Return the number of probes in this GenomicMatrix"""
        pass

    def nSamples(self):
        """Return the number of samples in this GenomicMatrix"""

    def observations(self, probe=None, sample=None):
        """Given a probe and/or sample, return a vector of the
        experimental observations from the GenomicMatrix for this probe
        and/or sample.  Return None if either the probe or sample is
        not in this sample matrix.  If both probe and sample are
        None, then return a matrix of all observations.
        """
        pass

    def probes(self):
        """Return the list of probes represented in this GenomicMatrix
        """
        pass

    def samples(self):
        """Return the list of samples represented in this GenonicMatrix"""
        pass

    def setValue(self, probe, sample, newValue):
        """Update the value stored for the indicated probe and sample
        """
        pass

    def sort(self, cmp=compareProbeIds):
        """Sort the genomic matrix according to the indicated comparison
        function"""
        pass
    
    def write(self, filename):
        """Write the GenomicMatrix object to the indicated filename"""
        pass

