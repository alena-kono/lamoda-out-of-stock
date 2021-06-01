class BaseAppException(Exception):
    '''Generic exception for this application.
    All custom exceptions should be inherited from this one.
    '''
    pass


class NoJsonError(BaseAppException):
    '''The exception is raised when Response object does not
    contain a valid json.
    '''
    def __init__(self):
        message = 'Response object does not contain a valid json'
        super().__init__(message)
