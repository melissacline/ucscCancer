from ucscCancer.cgData.Data import Data

class DataVector(Data):
    """Within the realm of cgData data, there are matrices of data and tables of data,
    where the tables consist of rows of pre-defined columns.  This is the base class for
    all vector data objects"""

    def __init__(self):
        """Create a new data vector object"""
        super().__init__()
        pass
    
