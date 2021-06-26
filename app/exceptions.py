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


class ConvertionError(BaseAppException):
    '''Raised when str cannot be converted to int'''
    def __init__(self, message: str) -> None:
        if not message:
            message = 'str cannot be converted to int'
        super().__init__(message)
