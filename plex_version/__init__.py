from plex_version.client import Client
from plex_version.exceptions import ClientError, IncorrectLoginError
from plex_version.version import (PLEX_HOME_THEATER, PLEX_MEDIA_PLAYER,
                                  PLEX_MEDIA_PLAYER_EMBEDDED,
                                  PLEX_MEDIA_SERVER, PlexVersion)

__version__ = '1.1.1'

__all__ = ('Client', 'ClientError', 'IncorrectLoginError', 'PLEX_MEDIA_SERVER',
           'PLEX_HOME_THEATER', 'PLEX_MEDIA_PLAYER',
           'PLEX_MEDIA_PLAYER_EMBEDDED', 'PlexVersion')
