from app.exceptions import AppError


class AccessTokenError(AppError):
    '''Access token is invalid or missing'''
    pass
