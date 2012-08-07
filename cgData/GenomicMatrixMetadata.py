
import cgDataV2.Exceptions
from cgDataV2.GenomicMetadata import GenomicMetadata

class GenomicMatrixMetadata(GenomicMetadata):
    """This class describes the metadata specific to GenomicMatrix objects.
    In addition to the metadata common to genomic objects, the genomic matrix
    metadata contains references to the ProbeMap and SampleMap metadata.
    """

    def __init__(self, filename):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  Upon creation, run the validator
        method on the new object and throw a ValidationFailed exception
        if unsuccessful.
        """
        super(GenomicMetadata, self).__init__(filename)
        pass

    def __validate(self):
        """Validate this GenomicMatrixMetadata object, and throw a
        ValidationFailed exception if unsuccessful.
        """
        pass
        
    def probeMapMetadata(self, assembly):
        """Return the probeMap metadata object for the indicated genomic
        assembly, or None if none is loaded.
        """
        pass

    def sampleMapMetadata(self):
        """Return the sampleMap metadata object, or None if none is loaded.
        """
        pass

    def subtype(self, newSubtyle=None):
        """The subtype indicates the type of GenomicMatrix data.  It is one
        value in a controlled vocabulary.  The expected values include
        ('cna' for copy number data, 'geneExp' for gene expression,
        'miRNAExp' for miRNA expression, 'protein' for protein activity,
        'DNAMethylation' for DNA methylation data, 'siRNAViability' for siRNA
        knockdown viability screens, 'RPPA' for protein activity, 'PARADIGM' for
        activity estimated with Paradigm pathway analysis, and
        'PARADIGM.pathlette' for pathway activity estimated via Paradigm pathlette
        pathway analysis.

        Return the subtype value.
        """
        pass

