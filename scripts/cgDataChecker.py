#!/usr/bin/env python

import json
import sys
from ucscCancer.cgData.GenomicMetadata import *


cgdir = "/inside/depot/cgrepo/cgDataFreeze2012-07-11/public/other/NCI60_public"
genomicMetadataFile = "%s/%s" % (cgdir, "NCI60exp_genomicMatrix.json")

def loadGenomicMetadata(pathname):
    """Load the genomic metadata.  Return whether the validation was
    'okay enough'"""
    okay = True
    try:
        genomicMetadata = GenomicMetadata(pathname)
    except IOError:
        print >> stderr, "Genomic metadata file", pathname, "not found"
        okay = False
    except ValueError:
        print >> stderr, "Genomic metadata file", pathname, "is not valid JSON"
        okay = False
    except ucscCancer.cgData.Metadata.ValidationFailed:
        print >> sys.stderr, sys.exc_info()[1]
    except:
        print >> sys.stderr, sys.exc_info()[1]
        okay = False
    return(genomicMetadata, okay)
        

(genomicMetadata, okayToContinue) = loadGenomicMetadata(genomicMetadataFile)

