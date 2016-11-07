import re


PLEX_MEDIA_SERVER = 1
PLEX_HOME_THEATER = 2
PLEX_MEDIA_PLAYER = 3
PLEX_MEDIA_PLAYER_EMBEDDED = 4


def _parse_version(version_string):
    matches = re.match(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)-([A-Fa-f0-9]+)',
                       version_string)
    groups = matches.groups()

    if len(groups) != 5:
        raise ValueError('invalid version string')

    major_version = int(groups[0])
    minor_version = int(groups[1])
    patch_version = int(groups[2])
    build_number = int(groups[3])
    commit = groups[4]

    return (major_version,
            minor_version,
            patch_version,
            build_number,
            commit)


class PlexVersion(object):
    def __init__(self, platform, distro, build, plexpass, date, version_string,
                 url):
        self._platform = platform
        self._distro = distro
        self._build = build
        self._plexpass = plexpass
        self._date = date
        self._version = _parse_version(version_string)
        self._version_string = version_string
        self._url = url

    @property
    def platform(self):
        return self._platform

    @property
    def distro(self):
        return self._distro

    @property
    def build(self):
        return self._build

    @property
    def plexpass(self):
        return self._plexpass

    @property
    def date(self):
        return self._date

    @property
    def version(self):
        return self._version

    @property
    def version_string(self):
        return self._version_string

    @property
    def url(self):
        return self._url

    @property
    def major_version(self):
        return self._version[0]

    @property
    def minor_version(self):
        return self._version[1]

    @property
    def patch_version(self):
        return self._version[2]

    @property
    def build_number(self):
        return self._version[3]

    @property
    def commit(self):
        return self._version[4]

    def __str__(self):
        version_string = self._version_string

        if self.plexpass:
            version_string += ' plexpass'

        return '{} {} ({})'.format(self.distro, self.build, version_string)

    def __repr__(self):
        return ('{}(platform={}, distro={}, build={}, plexpass={}, date={}, '
                'version_string={}, url={})').format(self.__class__.__name__,
                                                     *map(repr, [
                                                         self.platform,
                                                         self.distro,
                                                         self.build,
                                                         self.plexpass,
                                                         self.date,
                                                         self.version_string,
                                                         self.url
                                                     ]))

    def __eq__(self, other):
        return repr(self) == repr(other)

    @property
    def __dict__(self):
        return {
            'platform': self.platform,
            'distro': self.distro,
            'build': self.build,
            'plexpass': self.plexpass,
            'date': self.date,
            'version_string': self.version_string,
            'url': self.url
        }


__all__ = ('PLEX_MEDIA_SERVER', 'PLEX_HOME_THEATER', 'PLEX_MEDIA_PLAYER',
           'PLEX_MEDIA_PLAYER_EMBEDDED', 'PlexVersion')
