from __future__ import absolute_import


class ClientError(Exception):
    pass


class IncorrectLoginError(ClientError):
    pass


__all__ = ('ClientError', 'IncorrectLoginError')
