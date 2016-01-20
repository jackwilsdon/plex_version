from bs4 import BeautifulSoup
import requests

from . import PlexVersionParser


class VersionDownloader(object):
    def __init__(self, autodownload=False):
        self._versions = []

        if autodownload:
            self.download()

    def _add_version(self, version):
        self._versions.append(version)

    def download(self):
        raise NotImplementedError

    @property
    def versions(self):
        return self._versions

    def __contains__(self, value):
        return value in self.versions

    def __iter__(self):
        return iter(self.versions)


class PlexVersionDownloader(VersionDownloader):
    PLEX_DOWNLOAD_URL = "https://plex.tv/downloads"

    def __init__(self, autodownload=False):
        super(PlexVersionDownloader, self).__init__(autodownload)

    def _parse(self, content):
        parser = PlexVersionParser(content)
        parser.parse()

        for version in parser.versions:
            self._add_version(version)

    def download(self):
        response = requests.get(self.PLEX_DOWNLOAD_URL)
        response.raise_for_status()
        self._parse(response.content)


class PlexPassVersionDownloader(PlexVersionDownloader):
    PLEX_LOGIN_URL = "https://plex.tv/users/sign_in"
    PLEX_DOWNLOAD_URL = "https://plex.tv/downloads?channel=plexpass"

    def __init__(self, username, password, autodownload=False):
        self._username = username
        self._password = password
        self._session = requests.Session()

        super(PlexPassVersionDownloader, self).__init__(autodownload)

    def _get_authenticity_token(self):
        response = self._session.get(self.PLEX_LOGIN_URL)
        soup = BeautifulSoup(response.content, 'html.parser')
        token = soup.find("input", {"name": "authenticity_token"})

        if token is None:
            raise RuntimeError("unable to find authenticity token")

        return token["value"]

    def _login(self):
        response = self._session.post(self.PLEX_LOGIN_URL, data={
            "utf8": "\u2713",
            "authenticity_token": self._get_authenticity_token(),
            "user[login]": self._username,
            "user[password]": self._password,
            "user[remember_me]": 0
        })

        if "Sign In" in str(response.content):
            raise RuntimeError("failed to sign in - invalid details?")

    def download(self):
        self._login()
        response = self._session.get(self.PLEX_DOWNLOAD_URL)
        response.raise_for_status()
        self._parse(response.content)
