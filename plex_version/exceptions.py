class ClientError(Exception):
    pass


class IncorrectLoginError(ClientError):
    pass


__all__ = ('ClientError', 'IncorrectLoginError')
