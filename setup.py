#!python
# -* coding: utf-8 *-
"""
Setup script
"""
# System imports
import os
import setuptools

# Third-party imports
from pip import download, req
# Local imports


HERE = os.path.abspath(os.path.dirname(__file__))


def get_requirements(reqfile):
    path = os.path.join(HERE, reqfile)
    deps = set()
    for dep in req.parse_requirements(path, session=download.PipSession()):
        try:
            # Pip 8.1.2 Compatible
            specs = ','.join(''.join(str(spec)) for spec in dep.req.specifier)
        except AttributeError:
            # Pip 1.5.4 Compatible
            specs = ','.join(''.join(spec) for spec in dep.req.specs)
        requirement = '{name}{extras}{specs}'.format(
            name=dep.name,
            extras=(
                '[{extras}]'.format(extras=','.join(dep.extras))
                if dep.extras else ''
            ),
            specs=specs,
        )

        deps.add(requirement)
    return deps


setuptools.setup(
    name='falcone',
    description='Falcon framework tools',
    version=':versiontools:falcone:',

    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements/requirements.txt'),
    tests_require=get_requirements('requirements/test-requirements.txt'),
    setup_requires=('versiontools'),

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
