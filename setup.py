from setuptools import find_packages, setup

setup(
    name='jcs_mediagraphic',
    packages=find_packages(include=['jcs_mediagraphic']),
    version=jcs_mediagraphic.version,
    description='Python library for MediaGraphic Group usages',
    author=jcs_mediagraphic.author,
    license=jcs_mediagraphic.license,
    install_requires=[],
)