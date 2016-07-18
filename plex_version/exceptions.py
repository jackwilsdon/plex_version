class ClientError(Exception):
    pass


class IncorrectLoginError(ClientError):
    pass


class InvalidPlatformError(ClientError):
    pass


__all__ = ('ClientError', 'IncorrectLoginError', 'InvalidPlatformError')
