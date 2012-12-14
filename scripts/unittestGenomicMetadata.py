#!/usr/bin/env python

import json
import os
import random
import re
import string
import sys
import unittest
from ucscCancer.cgData.GenomicMetadata import *
from ucscCancer.cgData.GenomicMatrixMetadata import *
from ucscCancer.cgData.GenomicSegmentMetadata import *

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

    def createFileContaining(self, filename, contents):
        """Create a file containing the specified contents"""
        fp = open(filename, "w")
        fp.write(contents)
        fp.close()
    

    def randomFileContaining(self, contents, suffix=".json"):
        """Write the specified contents to a random nonexistant file
        and return the filename"""
        filename = self.randomNonexistantFilename(suffix=suffix)
        self.createFileContaining(filename, contents)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoCgdata2(self):
        """Test for an exception if there is no cgdata """
        jsonData = '{ "type" : "genomicSegment", "version" : "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoRowKeySrc2(self):
        """if the cgdata has no rowKeySrc """
        jsonData = '{ "type": "genomicSegment", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)

    def testValidationErrorNoRowId2(self):
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicSegment", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": { "@type": "idDAG"},  \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorNoRowType2(self):        
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicSegment", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorWrongRowType(self):        
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicMatrix", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "idDAG"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorWrongRowType2(self):        
        """if the rowKeySrc has no ID"""
        jsonData = '{ "type": "genomicSegment", "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "probeMap"}, \
                                   "columnKeySrc": {"@id": "x", \
                                                    "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            


    def testValidationErrorNoIdDag2(self):        
        """if the colKeySrc type is not idDAG"""
        jsonData = '{ "type": "genomicSegment", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "x"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            

    def testValidationErrorNoSubtype2(self):        
        """if the rowKeySrc has no data subtype"""
        jsonData = '{ "type": "genomicSegment", \
                       "version": "2012-02-02", \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                  "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
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
            metaObj = GenomicMatrixMetadata(filename)
        except ucscCancer.cgData.Metadata.ValidationFailed:
            errorCaught = True
        finally:
            os.remove(filename)
            self.assertTrue(errorCaught)
            
    def testValidationErrorWrongSubtype2(self):        
        """if the subtype is unexpected"""
        jsonData = '{ "type": "genomicMatrix", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "x"}, \
                       "cgdata": { "rowKeySrc": {"@id": "x", \
                                                 "@type": "idDAG"}} }'
        filename = self.randomFileContaining(jsonData)
        errorCaught = False
        try:
            metaObj = GenomicSegmentMetadata(filename)
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
        gm = GenomicMatrixMetadata(filename)
        os.remove(filename)
        os.remove(probeMapFile)
        os.remove(sampleMapFile)
        self.assertTrue(gm.subtype() == "geneExp"
                        and gm.probeMapMetadata() == probeMapFile
                        and gm.sampleMapMetadata() == sampleMapFile)
                        
        

    def testRetrieveContents2(self):
        """Make sure the basic contents of a json file are retrieved"""
        sampleMapFile = self.randomFileContaining("y", suffix=".idDAG.json")
        sampleMapName = re.sub(".idDAG.json", "", sampleMapFile)
        jsonData = '{ "type": "genomicSegment", \
                       "version": "2012-02-02", \
                       "dataSubType" : {"@id": "geneExp"}, \
                       "cgdata": { "rowKeySrc": {"@id": "%s", \
                                                 "@type": "idDAG"}} }' \
                      % (sampleMapName)
        filename = self.randomFileContaining(jsonData)
        gm = GenomicSegmentMetadata(filename)
        os.remove(filename)
        os.remove(sampleMapFile)
        self.assertTrue(gm.subtype() == "geneExp"
                        and gm.sampleMapMetadata() == sampleMapFile)
                        
        


if __name__ == '__main__':
    unittest.main()
