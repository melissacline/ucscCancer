import ucscCancer.cgData.Exceptions 
import json
import re
import sys


class ValidationFailed(Exception):
    """This exception is thrown when an object fails validation
    Attributes:
    - message: a message detailing the validation error
    - value: an optional value
    """


class Metadata(object):
    """This class describes the basic metadata associated with each class.  Each
    class type has its own type of metadata, but there are some elements common to
    all metadata types
    """

    def __init__(self, filename):
        """Given the pathname of a metadata file, return the corresponding
        metadata object.  Upon creation, run the validator
        method on the new object and throw a ValidationFailed exception
        if unsuccessful.
        """
        self._filename = filename
        fp = open(filename)
        self._contents = json.loads(fp.read())
        for key in self._contents.keys():
            #
            # Some .json keys begin with an @ sign, which represents ???.
            # The caller should not have to know which fields have @ signs
            # and which don't.  For each key that begins with an @ sign,
            # create a secondary key consisting of the same string without
            # the @ sign, and having the same value.
            if re.search("^@", key):
                secondaryKey = re.sub("^@", "", key)
                self._contents[secondaryKey] = self._contents[key]
        self._validate()
                

    def _validate(self):
        """Validate this metadata object, and throw a
        ValidationFailed exception if unsuccessful.
        """
        if not self._contents.has_key('type'):
            raise ValidationFailed("Metadata file %s contains no type field" % (self._filename))
        
        if not self._contents.has_key('version'):
            raise ValidationFailed("Metadata file %s contains no version field" %
                                   (self._filename))

    def _setValue(self, field, value):
        """Update the contents of the indicated field with the indicated value"""
        self._contents[field] = value

    def _getValue(self, field):
        """Get the metadata value for the indicated field (or key)"""
        return self._contents[field]

    def contents(self):
        """Return the full .json data representing the object"""
        return self._contents
    
    def type(self):
        """
        Return the metadata type.
        """
        return self._getValue('type')

    def version(self, newVersion=None):
        """
        Update the version if a new version is specified
        Return the metadata version.
        """
        if newVersion != None:
            self._setValue('version', newVersion)
        return self._getValue('version')
    

    def shortTitle(self, newShortTitle=None):
        """
        The shortTitle is a short description of the object.
        Update the shortTitle if a new shortTitle is specified.
        Return the shortTitle if defined, or None if undefined.
        """
        if newVersion != None:
            self._setValue('shortTitle', newShortTitle)
        return self._getValue('shortTitle')


    def longTitle(self, newLongTitle=None):
        """
        The longTitle is a longer description of the object.
        Update the longTitle if a new longTitle is specified.
        Return the longTitle if defined, or None if undefined.
        """
        if newLongTitle != None:
            self._setValue('longTitle', newLongTitle)
        return self._getValue('longTitle')


    def description(self, newDescription=None):
        """
        The description is a text string detailing the object.
        Update the description if a new description is specified.
        Return the description if defined, or None if undefined.
        """
        if newDescription != None:
            self._setValue('description', newDescription)
        return self._getValue('description')



    def write(self, filename):
        """Write the metadata object to the specified filename"""
        pass

    def data(self):
        """Return the data object associated with this metadata"""
        pass
