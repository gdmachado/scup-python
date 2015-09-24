class ScupPythonError(Exception):
    """ Base class for exceptions raised by scup-python. """


class ScupError(ScupPythonError):
    """ Exception for Scup-related errors. """
    def __init__(self, message=None, code=None, error_data=None):
        self.message = message
        self.code = code
        self.error_data = error_data

        if self.code:
            message = '[{}] {}'.format(self.code, self.message)

        super(ScupError, self).__init__(message)

class ScupClientError(ScupPythonError):
    """ Exception for client-related errors. """
    def __init__(self, message=None, code=None, error_data=None):
        self.message = message
        self.code = code
        self.error_data = error_data

        if self.code:
            message = '[{}] {}'.format(self.code, self.message)

        super(ScupClientError, self).__init__(message)
        
class HTTPError(ScupPythonError):
    """ Exception for transport errors. """