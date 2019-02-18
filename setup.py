#!python
# -* coding: utf-8 *-
"""
Setup script
"""
# System imports
import os
import setuptools

# Local imports
import falcone


setuptools.setup(
    name='falcone',
    description='Falcon framework tools',
    version=falcone.__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[],
    author='David Garaña',
    author_email='david@dgarana.com',
    url='http://dgarana.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
