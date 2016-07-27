'''Plex Version API

Version information is retrieved from https://plex.tv.
'''

from os import path as _path
import setuptools as _setuptools
from setup_functions import get_file_content


setup_directory = _path.dirname(__file__)
readme_path = _path.join(setup_directory, 'README.rst')


_setuptools.setup(
    name='plex_version',
    version='1.0.5',
    description='Plex Version API',
    long_description=get_file_content(readme_path),
    author='Jack Wilsdon',
    author_email='jack.wilsdon@gmail.com',
    url='https://github.com/jackwilsdon/plex_version',
    license='AGPL-3.0',
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
    keywords='plex version',
    packages=['plex_version'],
    install_requires=[
        'requests>=2,<3'
    ]
)
