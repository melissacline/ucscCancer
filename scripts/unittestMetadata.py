#!/usr/bin/env python

import json
import os
import random
import string
import sys
import unittest
from ucscCancer.cgData.Metadata import *
from ucscCancer.cgData.Exceptions import *

class testMetadata(unittest.TestCase):
    """
    Test case for basic metadata
    """
    @staticmethod
    def randomNonexistantFilename(suffix=".json"):
        """Return the name of a random, nonexistant file"""
        while True:
            randomString = "".join(random.sample(string.ascii_lowercase,
                                                 random.randint(1,20)))
            randomFilename = "%s%s" % (randomString, suffix)
            if not os.path.exists(randomFilename):
                return(randomFilename)
    
    def setUp(self):
        """Set up the metadata object here"""

    def testFileExistException(self):
        """Test for an exception if the metadata file does not exist
        """
        filename = self.randomNonexistantFilename()
        errorCaught = False
        try:
            metaObj = Metadata(filename)
        except IOError:
            errorCaught = True
        finally:
            self.assertTrue(errorCaught)
            
    def testInvalidFileException(self):
        """Test for an exception if the metadata file is not valid JSON"""
        filename = self.randomNonexistantFilename()
        fp = open(filename, "w")
        fp.write("x")
        fp.close()
        errorCaught = False
        try:
            metaObj = Metadata(filename)
        except ValueError:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoType(self):
        """Test for an exception if the metadata file has no 'type'"""
        jsonData = '{ "version": "2012-02-02" }'
        filename = self.randomNonexistantFilename()
        fp = open(filename, "w")
        fp.write(jsonData)
        fp.close()
        errorCaught = False
        try:
            metaObj = Metadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoVersion(self):
        """Test for an exception if the metadata file has no 'type'"""
        jsonData = '{ "type": "probeMap" }'
        filename = self.randomNonexistantFilename()
        fp = open(filename, "w")
        fp.write(jsonData)
        fp.close()
        errorCaught = False
        try:
            metaObj = Metadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)

    def testRetrieveContents(self):
        """Make sure the basic contents of a json file are retrieved"""
        jsonData = '{ "type": "probeMap", "version": "2012-02-02" }'
        filename = self.randomNonexistantFilename()
        fp = open(filename, "w")
        fp.write(jsonData)
        fp.close()
        jsonObj = Metadata(filename).contents()
        self.assertTrue(jsonObj["type"] == "probeMap"
                        and jsonObj["version"] == "2012-02-02")
        

if __name__ == '__main__':
    unittest.main()
