#!/usr/bin/env python

import json
import os
import random
import string
import sys
import unittest
from ucscCancer.cgData import Metadata
from ucscCancer.cgData.Exceptions import ChainedException

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
            metaObj = Metadata.Metadata(filename)
        except ChainedException:
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
            metaObj = Metadata.Metadata(filename)
        except ChainedException:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    

if __name__ == '__main__':
    unittest.main()
