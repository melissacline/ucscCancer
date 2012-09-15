.. cgData documentation master file, created by
   sphinx-quickstart on Thu Jun 14 18:05:28 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the documentation for the cgData API!
================================================

Within the cgData system, there is data and there is metadata.  The
data and metadata files are stored in the same directory as each
other, and are linked by a naming convention. Given any metadata
object, you can obtain its data object and vise versa.  The metadata
also points to certain related metadata objects, as described below.

The entry point to the system is the genomic metadata.  As well as
identifying the genomic data (whether a GenomicMatrix or
GenomicSegmentSet object), it identifies the ProbeMapSetMetadata and
SampleMapMetadata, which in turn identify the ProbeMapSet and
SampleMap objects respectively.  The SampleMapMetadata identifies one
or more ClinicalMatrixMetadata sets (each of which in turn identifies
a ClinicalMatrix).  Each ClinicalMatrixMetadata object may identify a
ClinicalFeatureSetMetadata object.

The metadata is the entry point for each object.  First, the metadata
object is initialized.  Then, each object is initialized with its
metadata object passed as an argument to the constructor.  This
metadata contains the name of the object's filename, along with other
mandatory metadata fields such as version and type and the myriad of
optional fields.  

Each object is loaded into memory in its entirety.  However, there is
no requirement that all objects are contained in memory at once.  Even
the metadata can be loaded without the corresponding data.

Each object contains a validation method.  This validation
method is called by the constructor as a final step.  If the object fails
validation, then a ValidationFailed exception is thrown.

  

Contents:

.. toctree::
   :maxdepth: 2

   classes
   scripts

    


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

