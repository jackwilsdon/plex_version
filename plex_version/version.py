import re as _re
import collections as _collections


PLEX_MEDIA_SERVER = 1
PLEX_HOME_THEATER = 2
PLEX_MEDIA_PLAYER = 3
PLEX_MEDIA_PLAYER_EMBEDDED = 4


def _parse_version(version_string):
    matches = _re.match(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)-([A-Fa-f0-9]+)',
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
    def __init__(self, platform, distro, build, date, version_string, url):
        self._platform = platform
        self._distro = distro
        self._build = build
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
        return self[0]

    @property
    def minor_version(self):
        return self[1]

    @property
    def patch_version(self):
        return self[2]

    @property
    def build_number(self):
        return self[3]

    @property
    def commit(self):
        return self[4]

    def __str__(self):
        return '{} {} ({})'.format(self.distro, self.build,
                                   self._version_string)

    def __repr__(self):
        return str(self)

    def __getitem__(self, index):
        return self.version[index]

    def __eq__(self, other):
        return all([self[k] == other[k] for k in range(3)])

    def __gt__(self, other):
        if self == other:
            return False

        return not any([self[k] <= other[k] for k in range(3)])


__all__ = ('PlexVersion',)
