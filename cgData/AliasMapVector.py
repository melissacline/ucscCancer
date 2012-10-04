import ucscCancer.cgData.Exceptions
from ucscCancer.cgData.DataVector import DataVector

class AliasMapVector(DataVector):
    """An AliasMapVector maps a probe to an alias, such as a gene name.

    See Also: AliasMapSet.py
    """

#    __format__ =  {
#        "name" : "aliasMap",
#        "form" : "table",
#        "columnOrder" : [
#            "alias",
#            "aliases",
#            "chrom",
#            "chrom_start",
#            "chrom_end",
#            "strand"
#            ],
#        "primaryKey" : "alias",
#        "columnDef" : {
#            "chrom_start" : { "type" : "int", "index" : 1 },
#            "chrom_end" : { "type" : "int", "index" : 1 }
#            }
#        }

    def __init__(self, line=None):
        """Creates a new AliasMapVector object.  If line is None, an 
        empty object is returned.  Else, the contents of the AliasMapVector
        are parsed from the whitespace-delimited line.
        The object is validated as a
        final initialization step.  If validation fails, a ValidationFailed
        exception is thrown.
        """
        super().__init__()
        pass


    def __validate(self):
        """Validate the object.  If unsuccessful, throw a ValidationFailed
        exception.
        """

    def compare(vector1, vector2):
        """Compare the two alias map vectors, sorting by the leftmost
        column first and using additional columns to break ties.
        """
        pass

    def write(self, filehandle, delimiter="\t"):
        """Write a AliasMapVector object to the indicated filehandle.
        The data is written in tab-delimited format by default.
        """
        pass


