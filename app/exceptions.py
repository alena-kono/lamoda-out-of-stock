class BaseAppException(Exception):
    '''Generic exception for this application.
    All custom exceptions should be inherited from this one.
    '''
    pass


class NoJsonError(BaseAppException):
    '''Raised when Response object does not
    contain a valid json.
    '''
    def __init__(self) -> None:
        message = 'Response object does not contain a valid json'
        super().__init__(message)


class InvalidConfigError(BaseAppException):
    '''Raised when invalid config name is passed'''
    def __init__(self) -> None:
        message = 'Invalid config name is passed'
        super().__init__(message)
