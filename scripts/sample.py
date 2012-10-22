#!/usr/bin/env python

import json
import os
import random
import string
import sys
import unittest
from ucscCancer.cgData import Metadata
from ucscCancer.cgData.Exceptions import ChainedException

cgdir = "/inside/depot/cgrepo/cgDataFreeze2012-07-11/public/other/NCI60_public"
genomicMetadata = "%s/%s" % (cgdir, "NCI60exp_genomicMatrix.json")
newMetadata = Metadata.Metadata(genomicMetadata)
