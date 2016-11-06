Plex Version API
================

Plex Version API is a Python library designed to the allow quick and easy retrieval of the latest version of Plex software from plex.tv_.

.. code-block:: python

    import plex_version

    # Create a new client for the API
    client = plex_version.client.Client()

    # Get a list of all PMS versions
    versions = client.get(plex_version.version.PLEX_MEDIA_SERVER)

    # Print the list of versions
    print(versions)

.. _plex.tv: https://plex.tv
