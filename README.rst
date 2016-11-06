Plex Version API
================

Plex Version API is a Python library designed to the allow quick and easy retrieval of the latest version of Plex software from plex.tv_.

.. _Plex Homepage: https://plex.tv
.. _Plex Media Server: `Plex Homepage`_
.. _plex.tv: `Plex Homepage`_

Basic Usage
===========

Retrieving a list of all public Plex versions from the API
----------------------------------------------------------
.. code-block:: python

    import plex_version

    # Create a new client for the API
    client = plex_version.client.Client()

    # Get a list of all PMS versions
    versions = client.get(plex_version.version.PLEX_MEDIA_SERVER)

    # Print the list of versions
    print(versions)

.. code-block:: python

    [
        PlexVersion(platform=1, distro=u'freebsd', build=u'freebsd-x86_64', plexpass=False, ...),
        PlexVersion(platform=1, distro=u'english', build=u'windows-i386', plexpass=False, ...),
        PlexVersion(platform=1, distro=u'macosx', build=u'darwin-x86_64', plexpass=False, ...)
    ]

Retrieving a list of all Plex Pass versions from the API
--------------------------------------------------------
.. code-block:: python

    import plex_version

    # Create a new client for the API
    client = plex_version.client.Client()

    # Get a list of all PMS versions
    versions = client.get(plex_version.version.PLEX_MEDIA_SERVER, plexpass=True)

    # Print the list of versions
    print(versions)

.. code-block:: python

    [
        PlexVersion(platform=1, distro=u'freebsd', build=u'freebsd-x86_64', plexpass=True, ...),
        PlexVersion(platform=1, distro=u'english', build=u'windows-i386', plexpass=True, ...),
        PlexVersion(platform=1, distro=u'macosx', build=u'darwin-x86_64', plexpass=True, ...)
    ]
