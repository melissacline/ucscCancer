import cgDataV2.Exceptions

class Metadata(object):
    """This class describes the basic metadata associated with each class.  Each
    class type has its own type of metadata, but there are some elements common to
    all metadata types
    """

    def __init__(self, filename, validate=True):
        """Given the pathname of a metadata file, return the corresponding
        metadata object.  Upon creation, run the validator
        method on the new object and throw a ValidationFailed exception
        if unsuccessful.
        """
        pass

    def __validate(self):
        """Validate this GenomicMatrixMetadata object, and throw a
        ValidationFailed exception if unsuccessful.
        """
        pass
        
    def type(self):
        """
        Return the metadata type.
        """
        pass

    def version(self, newVersion=None):
        """
        Update the version if a new version is specified
        Return the metadata version.
        """
        pass

    def shortTitle(self, newShortTitle=None):
        """
        The shortTitle is a short description of the object.
        Update the shortTitle if a new shortTitle is specified.
        Return the shortTitle if defined, or None if undefined.
        """
        pass

    def longTitle(self, newLongTitle=None):
        """
        The longTitle is a longer description of the object.
        Update the longTitle if a new longTitle is specified.
        Return the longTitle if defined, or None if undefined.
        """
        pass

    def description(self, newDescription=None):
        """
        The description is a text string detailing the object.
        Update the description if a new description is specified.
        Return the description if defined, or None if undefined.
        """
        pass

    def validate(self):
        """Validate the fields expected in all metadata objects.  Return
        True if the validation is successful, False otherwise
        """
        pass

    def write(self, filename):
        """Write the metadata object to the specified filename"""
        pass
