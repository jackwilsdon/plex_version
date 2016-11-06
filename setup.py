'''Plex Version API

Version information is retrieved from https://plex.tv.
'''

from os import path as _path
import setuptools as _setuptools
import setup_functions as _setup_functions


setup_directory = _path.dirname(__file__)
init_path = _path.join(setup_directory, 'plex_version', '__init__.py')
readme_path = _path.join(setup_directory, 'README.rst')


_setuptools.setup(
    name='plex_version',
    version=_setup_functions.get_assignment_value(init_path, '__version__', True),
    description='Plex Version API',
    long_description=_setup_functions.get_file_content(readme_path),
    author='Jack Wilsdon',
    author_email='jack.wilsdon@gmail.com',
    url='https://github.com/jackwilsdon/plex_version',
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
