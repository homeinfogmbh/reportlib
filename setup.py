#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name='reportlib',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info@homeinfo.de>',
    maintainer='Richard Neumann',
    maintainer_email='<r.neumann@homeinfo.de>',
    install_requires=[
        'comcatlib',
        'configlib',
        'flask',
        'marketplace',
        'mdb',
        'peewee',
        'peeweeplus',
        'tenantcalendar',
        'tenantforum',
        'wsgilib'
    ],
    packages=['reportlib'],
    description='Report management for user-generated content.'
)
