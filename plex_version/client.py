import uuid as _uuid
import requests as _requests

from plex_version import exceptions as _exceptions
from plex_version import version as _version


class Client(object):
    PLEX_LOGIN_URL = 'https://plex.tv/users/sign_in.json'
    PLEX_PLATFORM_URL = 'https://plex.tv/api/downloads/{}.json'

    def __init__(self, username=None, password=None, timeout=5):
        self.identifier = str(_uuid.uuid4())
        self.auth_token = None
        self.versions = []
        self.timeout = timeout

        if username is not None or password is not None:
            self.login(username, password)

    def _complete_login(self, response):
        if response.status_code == 401:
            raise _exceptions.IncorrectLoginError(response.content)

        response_dict = response.json()

        try:
            self.auth_token = response_dict['user']['authentication_token']
        except KeyError:
            raise _exceptions.ClientError('invalid response from server ' +
                                          '(missing user)')

    def login(self, username, password, timeout=None):
        headers = {
            'X-Plex-Client-Identifier': self.identifier
        }

        data = {
            'user[login]': username,
            'user[password]': password
        }

        if timeout is None:
            timeout = self.timeout

        response = _requests.post(self.PLEX_LOGIN_URL,
                                  headers=headers,
                                  data=data,
                                  timeout=timeout)

        self._complete_login(response)

    def _complete_fetch_versions(self, platform, response):
        if response.status_code != 200:
            raise _exceptions.ClientError('expected 200 but got {}'.format(
                                          response.status_code))

        response_dict = {k: v for d in response.json().values()
                         for k, v in d.items()}

        for version_data in response_dict.values():
            date = version_data['release_date']
            version_string = version_data['version']

            for release_data in version_data['releases']:
                distro = release_data['distro']
                build = release_data['build']
                url = release_data['url']

                version = _version.PlexVersion(platform, distro, build, date,
                                               version_string, url)

                self.versions.append(version)

    def _fetch_versions(self, platform, timeout):
        url = self.PLEX_PLATFORM_URL.format(platform)

        headers = {
            'X-Plex-Client-Identifier': self.identifier
        }

        if self.auth_token is not None:
            headers['X-Plex-Token'] = self.auth_token

        if timeout is None:
            timeout = self.timeout

        response = _requests.get(url, headers=headers, timeout=timeout)

        self._complete_fetch_versions(platform, response)

    def _get_existing(self, platform, distro, build):
        matches = []

        for version in self.versions:
            match_count = 0

            if (platform is not None and platform == version.platform) or \
                    platform is None:
                match_count += 1

            if (distro is not None and distro == version.distro) or \
                    distro is None:
                match_count += 1

            if (build is not None and build == version.build) or \
                    build is None:
                match_count += 1

            if match_count == 3:
                matches.append(version)

        return matches

    def get(self, platform=None, distro=None, build=None, timeout=None):
        matches = self._get_existing(platform, distro, build)

        if len(matches) == 0:
            self._fetch_versions(platform, timeout)
            matches = self._get_existing(platform, distro, build)

        return matches


__all__ = ('Client',)
