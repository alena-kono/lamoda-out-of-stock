from app.exceptions import BaseAppException


class AccessTokenError(BaseAppException):
    '''Access token is invalid or missing'''
    pass
