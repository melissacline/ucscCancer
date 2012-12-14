#!/usr/bin/env bash

export PYTHONPATH=/inside/home/cline/projects/cgDataAPI:$PYTONPATH

export freezeDir="/inside/depot/cgrepo/cgDataFreeze2012-07-11/"

expDir="public/TCGA/LUAD/SNP6_genomicSegment.json"
scripts/cgDataChecker.py $freezeDir$expDir

expDir="public/other/maser2007_public/maserCGH_genomicMatrix.json"
scripts/cgDataChecker.py $freezeDir$expDir

expDir="public/other/chin2006_public/chin2006Exp_genomicMatrix.json"
scripts/cgDataChecker.py $freezeDir$expDir

expDir="public/other/NCI60_public/NCI60exp_genomicMatrix.json"
scripts/cgDataChecker.py $freezeDir$expDir
