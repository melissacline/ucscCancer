from ucscCancer.cgData.Data import Data

class DataMatrix(Data):
    """Within the realm of cgData data, there are matrices of data and tables of data,
    where the tables consist of rows of pre-defined columns.  This is the base class for
    all matrix data objects"""

    def __init__(self):
        """Create a new data matrix object"""
        super().__init__()
        pass
    
