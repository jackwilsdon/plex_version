Plex Version API Changelog
==========================

1.0.7
-----
 - Override ``__dict__`` for ``PlexVersion``
 - Tidy up documentation

1.0.6
-----
 - Update changelog to cover previous versions
 - Deduplicate version number so that it is only stored inside ``plex_version`` itself

1.0.5
-----
 - Update documentation to match new API usage

1.0.4
-----
 - Add "plexpass" suffix to version string if the version is a Plex Pass version

1.0.3
-----
 - Add support for Plex Pass versions with the ``plexpass`` option for ``Client#get```

1.0.2
-----
 - Errors returned by the Plex API are now used as JSON if possible

1.0.1
-----
 - Fix bug where incorrect exception was used for invalid login details

1.0.0
-----
 - Rewrite plex_version entirely to use new Plex APIs (breaking change)

0.1.2
-----
 - Hardcode current version in ``setup.py``

0.1.1
-----
 - Add ``__len__`` method to ``VersionDownloader``
 - Add ``__version__`` and ``__author__`` properties to package

0.1.0
-----
 - Initial release
