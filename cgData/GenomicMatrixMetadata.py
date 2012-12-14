
import os
import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.GenomicMetadata import *

class GenomicMatrixMetadata(GenomicMetadata):
    """This class describes the metadata specific to GenomicMatrix objects.
    In addition to the metadata common to genomic objects, the genomic matrix
    metadata contains references to the ProbeMap and SampleMap metadata.
    """

    def _initProbeMapReference(self, directory, delimiter):
        """Record the ProbeMap metadata pathname, and throw an exception
           if it does not exist"""

        probeMap = self._contents["cgdata"]["rowKeySrc"]["@id"]
        probeMapMetadataFile1 = ("%s%s%s.probeMap.json"
                                 % (directory, delimiter, probeMap))
        if os.path.exists(probeMapMetadataFile1):
            self.probeMapMetadataFile = probeMapMetadataFile1
        else:
            probeMapPath = ("/".join(self._filename.split("/")[0:5])
                            + "/probeMap")
            probeMapMetadataFile2 = ("%s%s%s.probeMap.json"
                                     % (probeMapPath, delimiter, probeMap))
            if os.path.exists(probeMapMetadataFile2):
                self.probeMapMetadataFile = probeMapMetadataFile2
            else:
                errorMsg = (("Cannot find probeMap file %s or %s"
                             + " given GenomicMatrix metadata in %s")
                            % (probeMapMetadataFile1, probeMapMetadataFile2,
                               self._filename))
                raise IOError(errorMsg)



    def __init__(self, filename):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  Upon creation, run the validator
        method on the new object and throw a ValidationFailed exception
        if unsuccessful.
        """
        super(GenomicMatrixMetadata, self).__init__(filename)
        self._validate()
        directory = "/".join(filename.split("/")[0:-1])
        if directory == "":
            delimiter = ""
        else:
            delimiter = "/"
        self._initProbeMapReference(directory, delimiter)
        self._initSampleMapReference("columnKeySrc", directory, delimiter)


    def _validateProbeMapReference(self):
        """Validate that the metadata points to a probeMap metadata"""
        cgData = self._contents["cgdata"]
        if not cgData.has_key("rowKeySrc"):
            errorMsg = (("GenomicMetadata file %s contains no"
                         + " rowKeySrc") % (self._filename))
            raise ValidationFailed(errorMsg)
        else:
            rowKeySrc = cgData['rowKeySrc']
            if not (rowKeySrc.has_key('@id') and rowKeySrc.has_key('@type')):
                errorMsg = (("GenomicMetadata file %s rowKeySrc is"
                             + " missing an id or type field")
                            % (self._filename))
                raise ValidationFailed(errorMsg)
            else:
                if rowKeySrc['@type'] != "probe":
                    errorMsg = (("GenomicMetadata file %s has a rowKeySrc"
                                 + " type of %s where probe was expected")
                                % (self._filename,rowKeySrc['@type']))
                    raise ValidationFailed(errorMsg)

        
    def _validate(self):
        """Validate this GenomicMatrixMetadata object, and throw a
        ValidationFailed exception if unsuccessful.
        In the GenomicMatrix metadata, the cgdata must have a columnKeySrc
        and rowKeySrc.
        """
        super(GenomicMatrixMetadata, self)._validate()
        #
        # Verify that the data is of type genomicMatrix.
        assert(self._contents.has_key('type'))
        if self._contents['type'] != "genomicMatrix":
            errorMsg = ("GenomicMatrix metadata file %s has unexpected type %s"
                        + " not genomicMatrix") % (self._filename,
                                                   self._contents['type'])
            raise ValidationFailed(errorMsg)
        else:
            self._validateProbeMapReference()
            self._validateSampleMapReference("columnKeySrc")
                    



