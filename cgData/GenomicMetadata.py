
import os
from ucscCancer.cgData.Metadata import *

class GenomicMetadata(Metadata):
    """This class describes the metadata specific to Genomic objects.
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  Run the validator
        method on the new object and throw exceptions if validation fails.
        """
        super(GenomicMetadata, self).__init__(filename)
        self._validate()
        directory = "/".join(filename.split("/")[1:-1])
        if directory == "":
            delimiter = ""
        else:
            delimiter = "/"
        sampleMap = self._contents["cgdata"]["columnKeySrc"]["@id"]
        sampleMapMetadataFile = "%s%s%s.idDAG.json" % (directory, delimiter,
                                                       sampleMap)
        if os.path.exists(sampleMapMetadataFile):
            self.sampleMapMetadataFile = sampleMapMetadataFile
        else:
            sampleMapMetadataFile = "%s%s%s_sampleMap.json" % (directory,
                                                               delimiter,
                                                               sampleMap)
            if os.path.exists(sampleMapMetadataFile):
                self.sampleMapMetadataFile = sampleMapMetadataFile
            else:
                raise IOError("Cannot find idDAG file %s from Genomic Metadata file %s" % (sampleMap, filename))
        probeMap = self._contents["cgdata"]["rowKeySrc"]["@id"]
        probeMapMetadataFile = "%s%s%s.probeMap.json" % (directory, delimiter,
                                                         probeMap)
        if os.path.exists(probeMapMetadataFile):
            self.probeMapMetadataFile = probeMapMetadataFile
        else:
            probeMapPath = "/".join(filename.split("/")[1:5]) + "/probeMap"
            probeMapMetadataFile = "%s%s%s.probeMap.json" % (directory,
                                                             delimiter,
                                                             probeMap)
            if os.path.exists(probeMapMetadataFile):
                self.probeMapMetadataFile = probeMapMetadataFile
            else:
                raise IOError("Cannot find probeMap file %s from Genomic Metadata file %s" % (probeMap, filename))


    def _validate(self):
        """Validate, and throw a ValidationFailed exception if unsuccessful.
        Every GenomicMetadata object must contain an idDag (sampleMap) and
        a probe object, must have a subtype, and the subtype must be of
        the expected type"""
        expectedTypes = ("cna", "geneExp", "miRNAExp", "protein",
                         "DNAMethylation", "siRNAViability", "RPPA",
                         "PARADIGM", "PARADIGM.palette")
        #
        # Validate the subtype
        if not self._contents.has_key('dataSubType'):
            raise ValidationFailed("GenomicMetadata file %s contains no dataSubType object" % (self._filename))
        else:
            subtype = self._contents["dataSubType"]
            if not subtype.has_key("@id"): 
                raise ValidationFailed("GenomicMetadata file %s contains a dataSubType object with no ID" % (self._filename))
            else:
                type = subtype["@id"]
                if not type in expectedTypes:
                    raise ValidationFailed("GenomicMetadata file %s contains an unexpected type of %s" % (self._filename, type))
        #
        # Validate the icDAG (sampleMap)
        if not self._contents.has_key("cgdata"):
            raise ValidationFailed("GenomicMetadata file %s contains no cgdata object" % (self._filename))
        else:
            cgData = self._contents["cgdata"]
            if not cgData.has_key("columnKeySrc"):
                raise ValidationFailed("GenomicMetadata file %s contains no columnKeySrc" % (self._filename))
            else:
                columnKeySrc = cgData['columnKeySrc']
                if not (columnKeySrc.has_key('@id')
                        and columnKeySrc.has_key('@type')):
                    raise ValidationFailed("GenomicMetadata file %s columnKeySrc is missing an id or type field" % self._filename)
                else:
                    if columnKeySrc['@type'] != "idDAG":
                        raise ValidationFailed("GenomicMetadata file %s has a columnKeySrc type of %s where idDAG was expected" % (self._filename, columnKeySrc['@type']))
            #
            # Validate the probe
            if not cgData.has_key("rowKeySrc"):
                raise ValidationFailed("GenomicMetadata file %s contains no rowKeySrc" % (self._filename))
            else:
                rowKeySrc = cgData['rowKeySrc']
                if not (rowKeySrc.has_key('@id')
                        and rowKeySrc.has_key('@type')):
                    raise ValidationFailed("GenomicMetadata file %s rowKeySrc is missing an id or type field" % self._filename)
                else:
                    if rowKeySrc['@type'] != "probe":
                        raise ValidationFailed("GenomicMetadata file %s has a rowKeySrc type of %s where probe was expected" % (self._filename, rowKeySrc['@type']))
                    

    def subtype(self):
        """Return the subtype"""
        return(self._contents["dataSubType"]["@id"])

    def probeMapMetadata(self):
        """Return a path to the probeMap metadata file"""
        return(self.probeMapMetadataFile)
    
    
    def sampleMapMetadata(self):
        """Return a path to the sampleMap metadata file"""
        return(self.sampleMapMetadataFile)
    

    def dataProducer(self, newDataProducer=None):
        """Update the data producer if a new data producer is specified
        Return the data producer, or None if not defined.
        """
        if newDataProducer != None:
            self._setValue('dataProducer', newDataProducer)
        return self._getValue('dataProducer')


    def wrangler(self, newWrangler=None):
        """
        The wrangler is the person who transformed the data into cgData format.
        Update the wrangler if a new wrangler is specified.
        Return the wrangler, or None if not defined.
        """
        if newWrangler != None:
            self._setValue('wrangler', newWrangler)
        return self._getValue('wrangler')


    def redistribution(self, newRedistribution=None):
        """
        The redistribution flag indicates if this data can be made
        available as part of a downloadable archive.
        Update the redistribution flag if a new value is specified
        Return the redistribution flag, or None if not defined.
        """
        if newRedistribution != None:
            self._setValue('redisribution', newRedistribution)
        return self._getValue('redisribution')
        pass

    def platform(self, newPlatform=None):
        """
        The platform is the type of experimental equipment with which
        the data was generated (eg. IlluminaHiSeq).
        Update the platform if a new platform is specified
        Return the platform, or None if not defined.
        """
        if newPlatform != None:
            self._setValue('platform', newPlatform)
        return self._getValue('platform')
        pass

    def articleTitle(self, newArticleTitle=None):
        """ The articleTitle is the title of the original publication
        that describes the experiment that produced the results in the
        file.  Update the articleTitle if a new platform is specified
        Return the platform, or None if not defined.  """
        if newArticleTitle != None:
            self._setValue('articleTitle', newArticleTitle)
        return self._getValue('articleTitle')
        pass

    def citation(self, newCitation=None):
        """
        The citation is the reference to the article in which the
        experiment was published.
        Update the citation if a new citation is specified
        Return the citation, or None if not defined.
        """
        if newCitation != None:
            self._setValue('citation', newCitation)
        return self._getValue('citation')
        pass

    def url(self, newUrl=None):
        """
        The url is the URL of the published article, if any.
        Update the url if a new url is specified
        Return the url, or None if not defined.
        """
        if newUrl != None:
            self._setValue('url', newUrl)
        return self._getValue('url')
        pass

    def normalized(self, newNormalized=None):
        """
        normalized describes any normalization method that
        was used to center the data (e.g. median-centered).
        Update the normalized if a new normalized is specified
        Return the normalized, or None if not defined.
        """
        if newNormalized != None:
            self._setValue('normalized', newNormalized)
        return self._getValue('normalized')
        pass

    def diseaseAbbr(self, newDisease_abbr=None):
        """
        The diseaseAbbr is the abbreviated name of the disease
        pertaining to the data, such as OV for Ovarian Cancer.
        Update the diseaseAbbr if a new value is specified
        Return the diseaseAbbr, or None if not defined.
        """
        if newDiseaseAbbr != None:
            self._setValue('disease_abbr', newDiseaseAbbr)
        return self._getValue('disease_abbr')
        pass
    





