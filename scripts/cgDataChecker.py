#!/usr/bin/env python

import argparse
import json
import sys
from ucscCancer.cgData.GenomicMetadata import *





def loadGenomicMetadata(pathname):
    """Load the genomic metadata.  Return whether the validation was
    'okay enough'"""
    genomicMetadata = None
    try:
        genomicMetadata = GenomicMetadata(pathname)
    except:
        print >> sys.stderr, sys.exc_info()[1]
        okayToContinue = False
    else:
        okayToContinue = True
    return(genomicMetadata, okayToContinue)
        

parser = argparse.ArgumentParser()
parser.add_argument("genomicMetaFile",
                    help="Pathname of the genomic metadata file")
args = parser.parse_args()
(genomicMetadata, okayToContinue) = loadGenomicMetadata(args.genomicMetaFile)


