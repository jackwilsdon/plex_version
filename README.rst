Plex Version API
================

Plex Version API is a Python library designed to allow quick and easy retrieval of the latest version of `Plex Media Server`_ from plex.tv_.

.. _Plex Homepage: https://plex.tv
.. _Plex Media Server: `Plex Homepage`_
.. _plex.tv: `Plex Homepage`_

----

Basic Usage
-----------

Retrieving a list of all public Plex versions from the API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    from plex_version import PlexVersionDownloader

    # Auto-download all versions from the server
    downloader = PlexVersionDownloader(True)

    # Output a list of all versions
    print(downloader.versions)

Expected output:
::

    [0.9.14.6.1620-e0b7243, 0.9.14.6.1620-e0b7243, 0.9.14.6.1620-e0b7243, ...]

Whilst these may appear to be duplicate versions, they are actually platform-specific versions as can be seen here:
::

    # Output a list of all versions and their platform / names
    for version in downloader:
        print("{} {} v{}".format(version.platform, version.name, version))

Expected output:
::

    Windows English v0.9.14.6.1620-e0b7243
    Windows Korean v0.9.14.6.1620-e0b7243
    Mac Unknown v0.9.14.6.1620-e0b7243
    Linux Ubuntu 64-bit v0.9.14.6.1620-e0b7243
    Linux Ubuntu 32-bit v0.9.14.6.1620-e0b7243
    Linux Fedora 64-bit v0.9.14.6.1620-e0b7243
    ...

Retrieving a list of all Plex Pass versions from the API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    from plex_version import PlexPassVersionDownloader

    # Auto-download all versions from the server
    downloader = PlexPassVersionDownloader("YOUR_PLEX_USERNAME", "YOUR_PLEX_PASSWORD", True)

    # Output a list of all versions
    print(downloader.versions)

Expected output:
::

    [0.9.15.1.1639-26325ea, 0.9.15.1.1639-26325ea, 0.9.15.1.1639-26325ea, ...]

Whilst these may appear to be duplicate versions, they are actually platform-specific versions as can be seen here:
::

    # Output a list of all versions and their platform / names
    for version in downloader:
        print("{} {} v{}".format(version.platform, version.name, version))

Expected output:
::

    Windows English v0.9.15.1.1639-26325ea
    Windows Korean v0.9.15.1.1639-26325ea
    Mac Unknown v0.9.15.1.1639-26325ea
    Linux Ubuntu 64-bit v0.9.15.1.1639-26325ea
    Linux Ubuntu 32-bit v0.9.15.1.1639-26325ea
    Linux Fedora 64-bit v0.9.15.1.1639-26325ea
    ...

Accessing the URL of a version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
::

    from plex_version import PlexVersionDownloader

    # Auto-download all versions from the server
    # This can be replaced with PlexPassVersionDownloader as a drop-in replacement
    downloader = PlexVersionDownloader(True)

    # Output a list of all version URLs
    for version in downloader:
        print(version.address)

Expected output:
::

    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/Plex-Media-Server-0.9.1406.1620-e0b7243-en-US.exe
    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/Plex-Media-Server-0.9.1406.1620-e0b7243-ko-KR.exe
    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/PlexMediaServer-0.9.14.6.1620-e0b7243-OSX.zip
    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/plexmediaserver_0.9.14.6.1620-e0b7243_amd64.deb
    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/plexmediaserver_0.9.14.6.1620-e0b7243_i386.deb
    https://downloads.plex.tv/plex-media-server/0.9.14.6.1620-e0b7243/plexmediaserver-0.9.14.6.1620-e0b7243.x86_64.rpm
