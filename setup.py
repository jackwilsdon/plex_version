'''Plex Version API

Version information is retrieved from https://plex.tv.
'''

from os import path as _path
import setuptools as _setuptools
import setup_functions as _setup_functions


_setup_directory = _path.dirname(__file__)
_init_path = _path.join(_setup_directory, 'plex_version', '__init__.py')
_readme_path = _path.join(_setup_directory, 'README.rst')
_version = _setup_functions.get_assignment_value(_init_path, '__version__', True)
_version_tag = 'develop' if _version.endswith('.dev0') else _version
_readme = _setup_functions.get_file_content(_readme_path)


_setuptools.setup(
    name='plex_version',
    version=_version,
    description='Plex Version API',
    long_description=_readme,
    author='Jack Wilsdon',
    author_email='jack.wilsdon@gmail.com',
    url='https://github.com/jackwilsdon/plex_version',
    download_url='https://github.com/jackwilsdon/plex_version/tarball/{}'.format(_version_tag),
    packages=['plex_version'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    license='AGPL-3.0',
    keywords='plex version',
    install_requires=[
        'requests>=2,<3'
    ],
)
