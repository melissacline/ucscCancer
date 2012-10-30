#!/usr/bin/env python

import json
import os
import random
import string
import sys
import unittest
from ucscCancer.cgData.GenomicMetadata import *

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

    def randomFileContaining(self, contents, suffix=".json"):
        """Write the specified contents to a random nonexistant file
        and return the filename"""
        filename = self.randomNonexistantFilename(suffix=suffix)
        fp = open(filename, "w")
        fp.write(contents)
        fp.close()
        return(filename)
    
        
    def setUp(self):
        """Set up the metadata object here"""

    def testValidationErrorNoCgdata(self):
        """Test for an exception if there is no cgdata """
        jsonData = '{ "type" : "genomicMatrix", "version" : "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoColKeySrc(self):
        """if the cgdata has no columnKeySrc """
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                       "@type": "probe"}}}'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorNoRowKeySrc(self):
        """if the cgdata has no rowKeySrc """
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoRowId(self):
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicMatrix", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": { "@type": "probe"},  \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)

    def testValidationErrorNoRowType(self):        
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicMatrix", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorNoProbe(self):        
        """if the rowKeySrc type is not probe"""
        jsonData = '{ "type": "genomicMatrix", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "x"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoColId(self):        
        """if the colKeySrc has no ID"""
        jsonData = '{ "type": "genomicMatrix","version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            


    def testValidationErrorNoColType(self):        
        """if the colKeySrc has no type"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "x"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            


    def testValidationErrorNoIdDag(self):        
        """if the colKeySrc type is not idDAG"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "x"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoSubtype(self):        
        """if the rowKeySrc has no data subtype"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            


    def testValidationErrorSubtypeNoID(self):        
        """if the subtype has no ID"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"x": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorWrongSubtype(self):        
        """if the subtype is unexpected"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "x"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            


    def testRetrieveContents(self):
        """Make sure the basic contents of a json file are retrieved"""
        probeMapFile = self.randomFileContaining("x", suffix=".probeMap.json")
        probeMapName = re.sub(".probeMap.json", "", probeMapFile)
        sampleMapFile = self.randomFileContaining("y", suffix=".idDAG.json")
        sampleMapName = re.sub(".idDAG.json", "", sampleMapFile)
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "%s", \
                                                 "@type": "probe"}, \
                                   "columnKeySrc": {"@id": "%s", \
                                                    "@type": "idDAG"}} }' \
                      % (probeMapName, sampleMapName)
        filename = self.randomFileContaining(jsonData)
        gm = GenomicMetadata(filename)
        os.remove(filename)
        os.remove(probeMapFile)
        os.remove(sampleMapFile)
        self.assertTrue(gm.subtype() == "geneExp"
                        and gm.probeMapMetadata() == probeMapFile
                        and gm.sampleMapMetadata() == sampleMapFile)
                        
        


if __name__ == '__main__':
    unittest.main()
