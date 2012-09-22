import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.Metadata import Metadata

class GenomicMetadata(Metadata):
    """This class describes the metadata specific to Genomic objects.
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a genomic metadata file, return the
        corresponding metadata object.  By default, run the validator
        method on the new object and return None if validation fails.
        """
        super().__init__(filename, validate=validate)
        pass

    def __validate(self):
        """Validate, and throw a ValidationFailed exception if unsuccessful"""
        pass
    
    def dataProducer(self, newDataProducer=None):
        """Update the data producer if a new data producer is specified
        Return the data producer, or None if not defined.
        """
        pass

    def wrangler(self, newWrangler=None):
        """
        The wrangler is the person who transformed the data into cgData format.
        Update the wrangler if a new wrangler is specified.
        Return the wrangler, or None if not defined.
        """
        pass

    def redistribution(self, newRedistribution=None):
        """
        The redistribution flag indicates if this data can be made
        available as part of a downloadable archive.
        Update the redistribution flag if a new value is specified
        Return the redistribution flag, or None if not defined.
        """
        pass

    def platform(self, newPlatform=None):
        """
        The platform is the type of experimental equipment with which
        the data was generated (eg. IlluminaHiSeq).
        Update the platform if a new platform is specified
        Return the platform, or None if not defined.
        """
        pass

    def articleTitle(self, newArticleTitle=None):
        """ The articleTitle is the title of the original publication
        that describes the experiment that produced the results in the
        file.  Update the articleTitle if a new platform is specified
        Return the platform, or None if not defined.  """
        pass

    def citation(self, newCitation=None):
        """
        The citation is the reference to the article in which the
        experiment was published.
        Update the citation if a new citation is specified
        Return the citation, or None if not defined.
        """
        pass

    def url(self, newUrl=None):
        """
        The url is the URL of the published article, if any.
        Update the url if a new url is specified
        Return the url, or None if not defined.
        """
        pass

    def normalized(self, newNormalized=None):
        """
        normalized describes any normalization method that
        was used to center the data (e.g. median-centered).
        Update the normalized if a new normalized is specified
        Return the normalized, or None if not defined.
        """
        pass

    def diseaseAbbr(self, newDisease_abbr=None):
        """
        The diseaseAbbr is the abbreviated name of the disease
        pertaining to the data, such as OV for Ovarian Cancer.
        Update the diseaseAbbr if a new value is specified
        Return the diseaseAbbr, or None if not defined.
        """
        pass
    
    def validate(self):
        """Validate the fields expected in a Genomic Metadata object.
        Return True or False depending on whether or
        not the object passed validation.
        """
        pass





