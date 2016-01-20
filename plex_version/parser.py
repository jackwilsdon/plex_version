from bs4 import BeautifulSoup
import os
import re

try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse

from . import PlexVersion


def _get_links(element, prefix=None):
    parent = element.find(class_="pop-btn", recursive=False)
    links = {}

    if parent is None:
        return None

    for link in parent.findAll("a", recursive=False):
        name = link.text if prefix is None else prefix + ' ' + link.text
        address = link["href"]
        links[name] = address

    return links


def _get_version_from_address(address):
    url = urlparse(address)
    path = os.path.normpath(url.path)
    pieces = path.split(os.sep)

    if len(pieces) < 3:
        raise ValueError("unable to find version from address")

    return pieces[2]


class PlexVersionParser(object):
    def __init__(self, html):
        self._html = html
        self._soup = BeautifulSoup(self.html, 'html.parser')
        self._versions = []

    @property
    def html(self):
        return self._html

    @property
    def soup(self):
        return self._soup

    @property
    def versions(self):
        return self._versions

    def _create_version(self, version, platform, name, address):
        version = 'Unknown' if version is None else version
        platform = 'Unknown' if platform is None else platform
        name = 'Unknown' if name is None else name
        address = 'Unknown' if address is None else address

        version_object = PlexVersion(version, platform, name, address)
        self.versions.append(version_object)

    def _parse_download_link(self, platform, name, address):
        platform = re.sub(r'^Plex Media Server for ', '', platform)
        name = re.sub(r'^Download ?', '', name)
        version = _get_version_from_address(address)

        if len(name) == 0:
            name = None

        self._create_version(version, platform, name, address)

    def _parse_download_links(self, platform, links):
        for name, address in links.items():
            self._parse_download_link(platform, name, address)

    def _parse_tab(self, tab):
        platform = tab.find(class_="title").text
        links = _get_links(tab)

        if links is None:
            parent = tab.find(class_="os", recursive=False)

            if parent is None:
                print(tab.prettify())

            for element in parent.findAll("li"):
                prefix = element.find("h3").text
                links = _get_links(element, prefix)
                self._parse_download_links(platform, links)

        else:
            self._parse_download_links(platform, links)

    def _parse_tabs(self, tabs):
        for tab in tabs:
            self._parse_tab(tab)

    def _parse_section(self, section):
        tabs = section.findAll("div", id=re.compile("tabs-[0-9]+"))
        self._parse_tabs(tabs)

    def _parse_sections(self):
        sections = self.soup.findAll("div", id=re.compile("pms-.*"))

        for section in sections:
            self._parse_section(section)

    def parse(self):
        self._parse_sections()
