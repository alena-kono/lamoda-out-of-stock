class BaseAppException(Exception):
    ''':exception: generic exception for this application.
    All custom exceptions should be inherited from this one.
    '''
    pass


class InvalidJsonError(BaseAppException):
    ''':exception: raised when Response object does not
    contain a valid json.
    '''
    def __init__(self, msg: str = '') -> None:
        if not msg:
            msg = 'Response object contains invalid json'
        super().__init__(msg)


class InvalidConfigError(BaseAppException):
    ''':exception: raised when invalid config name is passed'''
    def __init__(self, msg: str = '') -> None:
        if not msg:
            msg = 'Invalid config name is passed'
        super().__init__(msg)


class ConvertionError(BaseAppException):
    ''':exception: raised when str cannot be converted to int'''
    def __init__(self, msg: str = '') -> None:
        if not msg:
            msg = 'Str cannot be converted to int'
        super().__init__(msg)
