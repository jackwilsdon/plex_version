def _parse_version(version_string):
    pieces = version_string.split('.')

    if len(pieces) != 5:
        raise ValueError('invalid version string')

    major_version = int(pieces[0])
    minor_version = int(pieces[1])
    patch_version = int(pieces[2])
    pre_release_version = int(pieces[3])
    build_metadata = pieces[4]

    return (major_version,
            minor_version,
            patch_version,
            pre_release_version,
            build_metadata)


class SemanticVersion(object):
    def __init__(self, version_string):
        self._version = _parse_version(version_string)

    @property
    def version(self):
        return self._version

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
    def pre_release_version(self):
        return self[3]

    @property
    def build_metadata(self):
        return self[4]

    def __str__(self):
        return '.'.join(map(str, self.version))

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


class PlexVersion(SemanticVersion):
    def __init__(self, version_string, platform, name, address):
        super(PlexVersion, self).__init__(version_string)

        self._platform = platform
        self._name = name
        self._address = address

    @property
    def platform(self):
        return self._platform

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address
