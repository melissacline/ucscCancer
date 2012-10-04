from ucscCancer.cgData.Data import Data

class DataSet(Data):
    """Within the realm of cgData data, there
    are matrices of data and tables of data, where the tables consist
    of rows of pre-defined columns.  This is the base class for all
    table objects.  More formally, a table consists of rows, described
    by the DataVector class, and a collection of rows (i.e. a table)
    is described by the DataSet class"""
    
    def __init__(self):
        """Create a new data vector object"""
        super().__init__()
        pass
    
