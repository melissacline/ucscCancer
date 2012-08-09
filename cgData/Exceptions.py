
class ValidationFailed(Exception):
    """This exception is thrown when an object fails validation
    Attributes:
    - message: a message detailing the validation error
    """

    def __init__(self, message):
        self.message = message
        pass

