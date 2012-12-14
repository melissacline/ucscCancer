#!/usr/bin/env python

import argparse
import json
import re
import sys
from ucscCancer.cgData.GenomicMatrixMetadata import *
from ucscCancer.cgData.GenomicSegmentMetadata import *





def loadGenomicMatrixMeta(pathname):
    """Load the genomic matrix metadata.  Return a validation flag"""
    genomicMetadata = None
    try:
        genomicMetadata = GenomicMatrixMetadata(pathname)
    except:
        print >> sys.stderr, sys.exc_info()[1]
        okay = False
    else:
        okay = True
    return(genomicMetadata, okay)
        

def loadGenomicSegmentMeta(pathname):
    """Load the genomic segment metadata.  Return a vaildation flag"""
    genomicMetadata = None
    try:
        genomicMetadata = GenomicSegmentMetadata(pathname)
    except:
        print >> sys.stderr, sys.exc_info()[1]
        okay = False
    else:
        okay = True
    return(genomicMetadata, okay)
        

parser = argparse.ArgumentParser()
parser.add_argument("genomicMetaFile",
                    help="Pathname of the genomic metadata file")
args = parser.parse_args()
if re.search("genomicMatrix", args.genomicMetaFile):
    (genomicMatrixMetadata, okay) = loadGenomicMatrixMeta(args.genomicMetaFile)
else:
    (genomicSegmentMetadata, okay) = loadGenomicSegmentMeta(args.genomicMetaFile)
